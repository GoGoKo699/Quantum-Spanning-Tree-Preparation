#!/usr/bin/env python3
"""Check this repository's learning structure and local navigation.

This bounded structural check does not certify scientific statements, teaching
quality, external websites, mathematical rendering, or release readiness.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


EXPECTED_IDS = [f"M{i:02d}" for i in range(1, 31)]
EXPECTED_PHASES = ["background/preliminaries"] * 14 + ["narrative/innovation"] * 16
MILESTONE_HEADING = re.compile(r"^#{1,6}\s+(M\d{2})\b[^\n]*$", re.MULTILINE)
INLINE_LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+[^\n)]*)?\)")
REFERENCE_LINK = re.compile(r"^\s*\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", re.MULTILINE)
EXPLICIT_ANCHOR = re.compile(r"<(?:a|span)\b[^>]*\b(?:id|name)=[\"']([^\"']+)[\"']", re.IGNORECASE)
ANCHOR_DATE = re.compile(r"\b(?:17\s+Apr(?:il)?\.?\s+2025|2025-04-17)\b", re.IGNORECASE)


def without_fences(text):
    """Leave code contents out of Markdown link/heading checks."""
    result, fence_character, fence_length = [], None, 0
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence_character is None:
                fence_character, fence_length = marker[0], len(marker)
            elif marker[0] == fence_character and len(marker) >= fence_length:
                fence_character, fence_length = None, 0
            result.append("")
        else:
            result.append(line if fence_character is None else "")
    return "\n".join(result)


def heading_slug(heading):
    heading = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", heading)
    heading = re.sub(r"<[^>]*>", "", heading)
    # GitHub's ordinary prose-heading convention. Explicit IDs are preferable for
    # unusual mathematical headings, which this checker does not try to render.
    heading = heading.strip().lower()
    heading = re.sub(r"[^\w\-\s]", "", heading, flags=re.UNICODE)
    return re.sub(r"\s", "-", heading)


def anchors(text):
    visible = without_fences(text)
    result = set(EXPLICIT_ANCHOR.findall(visible))
    counts = {}
    for match in re.finditer(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", visible, re.MULTILINE):
        base = heading_slug(match.group(1))
        count = counts.get(base, 0)
        counts[base] = count + 1
        result.add(base if count == 0 else f"{base}-{count}")
    return result


def links(text):
    visible = without_fences(text)
    matches = [(match.start(), match.group(1).strip("<>"))
               for expression in (INLINE_LINK, REFERENCE_LINK)
               for match in expression.finditer(visible)]
    return [target for _, target in sorted(matches)]


def read_text(path):
    return path.read_text(encoding="utf-8")


def check_learning(root, errors):
    milestone_path = root / "learning/milestones.md"
    bridge_path = root / "learning/anchor_bridge.md"
    overview_path = root / "learning/README.md"
    for path in (milestone_path, bridge_path, overview_path):
        if not path.is_file():
            errors.append(f"Required learning file is missing: {path.relative_to(root)}")
    if any(not path.is_file() for path in (milestone_path, bridge_path, overview_path)):
        return {"status": "missing_files"}

    milestone_text = without_fences(read_text(milestone_path))
    headings = list(MILESTONE_HEADING.finditer(milestone_text))
    observed_ids = [match.group(1) for match in headings]
    if observed_ids != EXPECTED_IDS:
        errors.append(f"Milestone IDs must occur once in order M01..M30; found {observed_ids}")

    records, dependency_graph, observed_phases = [], {}, []
    for i, heading in enumerate(headings):
        identity = heading.group(1)
        body_end = headings[i+1].start() if i+1 < len(headings) else len(milestone_text)
        body = milestone_text[heading.end():body_end]
        phase_matches = re.findall(r"^Phase:\s*(.*?)\s*$", body, re.MULTILINE)
        dependency_matches = re.findall(r"^Prerequisites:\s*(.*?)\s*$", body, re.MULTILINE)
        if len(phase_matches) != 1:
            errors.append(f"{identity}: exactly one plain Phase field is required")
        phase = phase_matches[0] if phase_matches else None
        observed_phases.append(phase)
        if len(dependency_matches) != 1:
            errors.append(f"{identity}: exactly one plain Prerequisites field is required")
        dependencies = []
        if dependency_matches:
            value = dependency_matches[0].strip()
            if value.lower() != "none":
                if not re.fullmatch(r"M\d{2}(?:,\s*M\d{2})*", value):
                    errors.append(f"{identity}: prerequisites must be 'none' or a comma-separated ID list")
                dependencies = re.findall(r"M\d{2}", value)
        if len(set(dependencies)) != len(dependencies):
            errors.append(f"{identity}: repeated prerequisite")
        for dependency in dependencies:
            if dependency not in observed_ids:
                errors.append(f"{identity}: unresolved prerequisite {dependency}")
            elif observed_ids.index(dependency) >= i:
                errors.append(f"{identity}: prerequisite {dependency} must precede this milestone")
        if not links(body):
            errors.append(f"{identity}: no navigable source pointer was found")
        dependency_graph[identity] = dependencies
        records.append({"id": identity, "phase": phase, "prerequisites": dependencies})

    if observed_phases != EXPECTED_PHASES:
        errors.append("This project's selected allocation must be M01..M14 background/preliminaries, "
                      "then M15..M30 narrative/innovation")

    # This independent graph check remains useful if the order rule is changed.
    visiting, visited = set(), set()

    def visit(identity):
        if identity in visiting:
            errors.append(f"Prerequisite cycle includes {identity}")
            return
        if identity in visited or identity not in dependency_graph:
            return
        visiting.add(identity)
        for dependency in dependency_graph[identity]:
            visit(dependency)
        visiting.remove(identity)
        visited.add(identity)

    for identity in dependency_graph:
        visit(identity)

    bridge_text = read_text(bridge_path)
    selected = re.findall(r"^\s*(?:\*\*)?Selected anchor:(?:\*\*)?\s*(.+)$",
                          bridge_text, re.MULTILINE | re.IGNORECASE)
    if len(selected) != 1:
        errors.append("learning/anchor_bridge.md must have exactly one Selected anchor field")
    anchor_line = selected[0] if selected else ""
    for pattern, label in ((r"\bChilds\b", "Childs"),
                           (r"Lecture Notes on Quantum Algorithms", "the selected source title")):
        if not re.search(pattern, anchor_line, re.IGNORECASE):
            errors.append(f"Selected anchor field must identify {label}")
    if not ANCHOR_DATE.search(anchor_line):
        errors.append("Selected anchor field must retain the chosen 17 April 2025 version")
    # Additional bibliography entries are legitimate; only a second declaration
    # of the educational selection conflicts with the settled one-source route.
    for path in (overview_path, milestone_path):
        for line in re.findall(r"^\s*(?:\*\*)?Selected anchor:(?:\*\*)?\s*(.+)$",
                               read_text(path), re.MULTILINE | re.IGNORECASE):
            if "childs" not in line.lower() or not ANCHOR_DATE.search(line):
                errors.append(f"Conflicting selected-anchor declaration in {path.relative_to(root)}")
    return {"milestone_count": len(observed_ids), "ids": observed_ids,
            "phase_allocation": {"background/preliminaries": observed_phases.count("background/preliminaries"),
                                 "narrative/innovation": observed_phases.count("narrative/innovation")},
            "acyclic_dependencies": not any("cycle" in error for error in errors),
            "records": records, "selected_anchor": anchor_line}


def check_navigation(root, errors):
    markdown_paths = sorted(root.rglob("*.md"))
    content = {path: read_text(path) for path in markdown_paths}
    anchor_cache = {path: anchors(text) for path, text in content.items()}
    graph = {path: set() for path in markdown_paths}
    local_count, external_targets = 0, set()
    for path, text in content.items():
        for target in links(text):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                if parsed.scheme not in ("https", "http", "mailto"):
                    errors.append(f"Unsupported link scheme in {path.relative_to(root)}: {target}")
                elif parsed.scheme in ("https", "http") and not parsed.netloc:
                    errors.append(f"Malformed external link in {path.relative_to(root)}: {target}")
                external_targets.add(target)
                continue
            local_count += 1
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            try:
                destination.relative_to(root)
            except ValueError:
                errors.append(f"Local link leaves repository in {path.relative_to(root)}: {target}")
                continue
            if destination.is_dir():
                destination = destination / "README.md"
            if not destination.is_file():
                errors.append(f"Missing local target in {path.relative_to(root)}: {target}")
                continue
            if parsed.fragment and destination.suffix.lower() == ".md":
                wanted = unquote(parsed.fragment)
                available = anchor_cache.setdefault(destination, anchors(read_text(destination)))
                if wanted not in available:
                    errors.append(f"Missing local anchor in {path.relative_to(root)}: {target}")
            if destination in graph:
                graph[path].add(destination)

    start = root / "README.md"
    reachable, queue = ({start}, [start]) if start in graph else (set(), [])
    if start not in graph:
        errors.append("Root README.md is missing")
    for path in queue:
        for destination in graph[path]:
            if destination not in reachable:
                reachable.add(destination)
                queue.append(destination)
    required = [path for path in markdown_paths if path.parent.name in ("science", "learning")]
    required += [root / "verification/README.md", root / "references/related_work.md"]
    for path in required:
        if path not in reachable:
            errors.append(f"Reader page is not reachable from README.md: {path.relative_to(root)}")
    # The LLM route uses ordinary path names in prose, rather than only Markdown.
    llms = root / "llms.txt"
    if not llms.is_file():
        errors.append("llms.txt is missing")
    else:
        for target in re.findall(r"(?<![\w/])((?:science|learning|verification|references)/[\w./-]+\.(?:md|bib))",
                                 read_text(llms)):
            if not (root / target).is_file():
                errors.append(f"Missing llms.txt route: {target}")
    return {"markdown_files": len(markdown_paths), "local_links_checked": local_count,
            "reachable_reader_pages": [str(path.relative_to(root)) for path in sorted(reachable)],
            "external_link_targets_syntax_checked": len(external_targets),
            "external_http_reachability_checked": False}


def check_public_content(root, errors):
    prohibited_names = {"coaching", "checkpoints", "handoffs", "learner_state", "portfolio"}
    offending_paths = []
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part.lower() in prohibited_names for part in relative.parts) or re.search(
                r"(?:game[_-]?checkpoint|coaching[_-]?guide)", relative.name, re.IGNORECASE):
            offending_paths.append(str(relative))
    if offending_paths:
        errors.append(f"Private coaching/process paths found: {offending_paths}")
    markers = ("game_brief", "exploration_deadline_utc", "pending_decision", "learner_state", "Camelot")
    hits = []
    for path in sorted(root.rglob("*.md")):
        text = read_text(path)
        for marker in markers:
            if marker in text:
                hits.append({"file": str(path.relative_to(root)), "marker": marker})
    if hits:
        errors.append(f"Private process markers need removal or explicit review: {hits}")
    return {"prohibited_path_hits": offending_paths, "private_marker_hits": hits,
            "boundary": "Bounded path/marker scan only; semantic public/private review remains manual."}


def run(root):
    errors = []
    learning = check_learning(root, errors)
    navigation = check_navigation(root, errors)
    public_content = check_public_content(root, errors)
    checked_paths = sorted(root.rglob("*.md")) + [root / "llms.txt"]
    hashes = {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
              for path in checked_paths if path.is_file()}
    return {"status": "passed" if not errors else "failed", "errors": errors,
            "learning": learning, "navigation": navigation, "public_content": public_content,
            "checked_files_sha256": hashes,
            "manual_review_boundary": "This script does not assess scientific qualifiers, proof validity, "
                                      "anchor suitability, explanation quality or personal-content meaning.",
            "hosted_math_or_visual_review_claimed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="write the bounded structural report")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    report = run(root)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    if report["errors"]:
        print("FAIL: learning/navigation structure")
        for error in report["errors"]:
            print(f"- {error}")
        return 1
    print("PASS: M01..M30, 14/16 phases, prerequisites, selected Childs version, and local reader navigation.")
    print("      Scientific meaning, external HTTP reachability and hosted rendering require separate review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
