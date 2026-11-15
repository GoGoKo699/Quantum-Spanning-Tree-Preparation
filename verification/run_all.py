#!/usr/bin/env python3
"""Deterministic finite checks supporting the written spanning-tree compiler.

This is a dense small-instance mathematical check, not a QSVT circuit compiler,
gate benchmark, general proof, or hosted-rendering check.  Requires only NumPy.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np


TOL = 3e-10


def require(condition, message):
    if not bool(condition):
        raise AssertionError(message)


def small(value, message, tolerance=TOL):
    require(float(value) <= tolerance, f"{message}: {value!r} > {tolerance}")


def norm(matrix):
    return float(np.linalg.norm(matrix, 2))


def integer_det(matrix):
    """Exact fraction-free elimination, independent of floating-point minors."""
    a = [[int(x) for x in row] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign, previous = 1, 1
    for k in range(n - 1):
        pivot_row = next((j for j in range(k, n) if a[j][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                require(numerator % previous == 0, "Bareiss exact division")
                a[i][j] = numerator // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def is_tree(n, edges):
    if len(edges) != n - 1:
        return False
    parent = list(range(n))

    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for u, v in edges:
        if not (0 <= u < n and 0 <= v < n) or u == v:
            return False
        a, b = find(u), find(v)
        if a == b:
            return False
        parent[a] = b
    return len({find(v) for v in range(n)}) == 1


def incidence(n, edges):
    b = np.zeros((len(edges), n), dtype=int)
    for e, (u, v) in enumerate(edges):
        b[e, u], b[e, v] = 1, -1
    return b


def complete_graph(n):
    return list(itertools.combinations(range(n), 2))


def cycle_graph(n):
    return sorted({tuple(sorted((v, (v + 1) % n))) for v in range(n)})


def cube_graph():
    return [(u, u ^ (1 << j)) for u in range(8) for j in range(3)
            if u < (u ^ (1 << j))]


def graph_cases():
    return [
        ("K2", 2, complete_graph(2), 1),
        ("C3", 3, cycle_graph(3), 3),
        ("K4", 4, complete_graph(4), 16),
        ("C5", 5, cycle_graph(5), 5),
        ("K3_3", 6, [(u, v) for u in range(3) for v in range(3, 6)], 81),
        ("cube", 8, cube_graph(), 384),
        ("K5", 5, complete_graph(5), 125),
        ("K6", 6, complete_graph(6), 1296),
    ]


def fourier(n):
    labels = np.arange(n)
    return np.exp(2j * np.pi * labels[:, None] * labels[None, :] / n) / math.sqrt(n)


def port_matrices(n, edges, seed):
    """Permuted ports test algebra, not efficient clean endpoint conversion.

    The endpoint-output compiler requires sorted ports or sorted adjacency. Dense
    access to this test's arc list does not implement that promised input model.
    """
    neighbors = [[] for _ in range(n)]
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    degrees = {len(row) for row in neighbors}
    require(len(degrees) == 1, "regular graph required by this compiler")
    d = degrees.pop()
    require(d > 0, "nonzero degree")
    rng = np.random.default_rng(seed)
    for row in neighbors:
        rng.shuffle(row)
    arcs = [(u, v) for u, row in enumerate(neighbors) for v in row]
    lookup = {arc: i for i, arc in enumerate(arcs)}
    reverse = np.array([lookup[(v, u)] for u, v in arcs], dtype=int)
    require(np.array_equal(reverse[reverse], np.arange(n * d)), "R involution")
    require(np.all(reverse != np.arange(n * d)), "simple graph has no fixed arc")
    r = np.eye(n * d)[reverse]
    v = np.zeros((n * d, n))
    for u in range(n):
        v[u*d:(u+1)*d, u] = 1 / math.sqrt(d)
    a = (v - r @ v) / 2
    # Householder is an explicit known unitary preparing the uniform d-coin.
    e0 = np.eye(d)[:, 0]
    target = np.ones(d) / math.sqrt(d)
    delta = e0 - target
    ud = np.eye(d) if np.linalg.norm(delta) < TOL else (
        np.eye(d) - 2 * np.outer(delta, delta) / np.dot(delta, delta))
    hc = np.array([[1, 1], [1, -1]]) / math.sqrt(2)
    hc_arc = np.kron(hc, np.eye(n * d))
    select = np.zeros((2*n*d, 2*n*d))
    select[:n*d, :n*d] = np.eye(n*d)
    select[n*d:, n*d:] = r
    unitary = hc_arc @ select @ hc_arc @ np.kron(np.eye(2), np.kron(np.eye(n), ud))
    projected = unitary[n*d:, np.arange(n) * d]
    small(norm(unitary.T @ unitary - np.eye(2*n*d)), "encoding unitary")
    small(norm(projected - a), "projected block equals incidence map")
    canonical = [i for i in range(n*d) if i < reverse[i]]
    folded_edges = [arcs[h] for h in canonical]
    fold = np.zeros((len(canonical), n*d))
    for e, h in enumerate(canonical):
        fold[e, h], fold[e, reverse[h]] = 1/math.sqrt(2), -1/math.sqrt(2)
    b = incidence(n, folded_edges)
    small(norm(fold @ a - b / math.sqrt(2*d)), "folded normalization")
    return {"degree": d, "a": a, "fold": fold, "b": b,
            "edges": folded_edges, "r": r, "v": v, "arcs": arcs,
            "reverse": reverse, "port_orders": neighbors}


def polar_data(n, edges, seed):
    data = port_matrices(n, edges, seed)
    a, b = data["a"], data["b"]
    u, singular, vh = np.linalg.svd(a, full_matrices=False)
    active = singular > 1e-11
    require(int(np.sum(active)) == n - 1, "connected incidence rank")
    w = (u[:, active] @ vh[active, :])
    s = np.ones(n) / math.sqrt(n)
    projector = np.eye(n) - np.outer(s, s)
    small(norm(w.T @ w - projector), "polar initial projector")
    small(norm(a @ s), "known uniform null vector")
    d = data["degree"]
    laplacian = b.T @ b
    small(norm(a.T @ a - laplacian/(2*d)), "A* A normalization")
    eigen = np.linalg.eigvalsh(laplacian / d)
    gamma = float(eigen[1])
    small(abs(float(min(singular[active])) - math.sqrt(gamma/2)), "singular gap")
    q = fourier(n)[:, 1:]
    x = data["fold"] @ w @ q
    small(norm(x.conj().T @ x - np.eye(n-1)), "folded occupied orbitals")
    data.update({"w": w, "q": q, "x": x, "gamma": gamma,
                 "singular": singular[active], "u_active": u[:, active],
                 "vh_active": vh[active, :], "laplacian": laplacian})
    return data


def check_minors():
    reports, cached = [], {}
    for case, n, edges, known_count in graph_cases():
        data = polar_data(n, edges, seed=1234+n)
        cached[case] = (n, data)
        count = integer_det(data["laplacian"][:-1, :-1])
        require(count == known_count, f"{case} independent matrix-tree count")
        tree_count, non_tree_max, amplitude_error, global_phases = 0, 0.0, 0.0, []
        total_probability = 0.0
        for subset in itertools.combinations(range(len(edges)), n-1):
            rows = list(subset)
            determinant = np.linalg.det(data["x"][rows, :])
            total_probability += abs(determinant)**2
            selected_edges = [data["edges"][j] for j in rows]
            root_det = integer_det(data["b"][rows, :-1])
            tree = is_tree(n, selected_edges)
            require((root_det != 0) == tree, f"{case} independent cycle/determinant test")
            if tree:
                require(root_det in (-1, 1), "tree unimodular determinant")
                tree_count += 1
                amplitude_error = max(amplitude_error, abs(abs(determinant)-1/math.sqrt(count)))
                global_phases.append(determinant / root_det)
            else:
                non_tree_max = max(non_tree_max, abs(determinant))
        require(tree_count == count, f"{case} enumeration matches matrix-tree count")
        phase_error = max(abs(z-global_phases[0]) for z in global_phases)
        small(amplitude_error, f"{case} uniform tree amplitudes")
        small(non_tree_max, f"{case} non-tree minors vanish")
        small(phase_error, f"{case} only rooted-incidence signs vary")
        small(abs(total_probability-1), f"{case} Cauchy-Binet normalization")
        reports.append({"graph": case, "vertices": n, "degree": data["degree"],
                        "port_test_scope": "one-particle encoding, folding and minor identities; no endpoint-erasure cost",
                        "gap": data["gamma"], "trees": count,
                        "tree_amplitude_error": amplitude_error,
                        "non_tree_minor_max": non_tree_max,
                        "phase_spread": phase_error,
                        "probability_sum_error": abs(total_probability-1)})
    return reports, cached


def bitonic_parity(values):
    size = 1 << (max(1, len(values))-1).bit_length()
    sentinel_start = max(values, default=0)+1
    a = list(values) + list(range(sentinel_start, sentinel_start+size-len(values)))
    parity = 0

    def merge(start, length, increasing):
        nonlocal parity
        if length < 2:
            return
        half = length // 2
        for i in range(start, start+half):
            if (a[i] > a[i+half]) == increasing:
                a[i], a[i+half] = a[i+half], a[i]
                parity ^= 1
        merge(start, half, increasing)
        merge(start+half, half, increasing)

    def sort(start, length, increasing):
        if length > 1:
            half = length // 2
            sort(start, half, True)
            sort(start+half, half, False)
            merge(start, length, increasing)

    sort(0, size, True)
    require(a[:len(values)] == sorted(values), "fixed bitonic comparator schedule")
    return parity


def tree_sign_euler(n, edges, root=None):
    """Euler tour plus sorting-based batched pointer joins; no random-access model."""
    root = n-1 if root is None else root
    require(is_tree(n, edges), "Euler sign routine supplied a tree")
    arcs = [arc for u, v in edges for arc in ((u, v), (v, u))]
    lookup = {arc: i for i, arc in enumerate(arcs)}
    outgoing = [[] for _ in range(n)]
    for i, (u, v) in enumerate(arcs):
        outgoing[u].append((v, i))
    successor = [0] * len(arcs)
    for row in outgoing:
        row.sort()
        for j, (_, arc_id) in enumerate(row):
            successor[arc_id ^ 1] = row[(j+1) % len(row)][1]
    start = outgoing[root][0][1]
    terminal = successor.index(start)
    # Independent literal traversal checks both single-cycle and chronological rank.
    ordered, current = [], start
    for _ in arcs:
        ordered.append(current)
        current = successor[current]
    require(current == start and len(set(ordered)) == len(arcs), "one Euler cycle")
    expected_rank = {arc_id: i for i, arc_id in enumerate(ordered)}
    successor[terminal] = terminal
    distance = [0 if i == terminal else 1 for i in range(len(arcs))]
    repeated_keys_seen = False
    for _ in range((len(arcs)-1).bit_length()):
        records = [(i, 0, i, successor[i], distance[i]) for i in range(len(arcs))]
        records += [(successor[i], 1, i, 0, 0) for i in range(len(arcs))]
        records.sort(key=lambda row: (row[0], row[1], row[2]))
        repeated_keys_seen |= len(set(successor)) < len(successor)
        replies, payload, key = [], None, None
        for record_key, kind, origin, succ, dist in records:
            if kind == 0:
                key, payload = record_key, (succ, dist)
            else:
                require(key == record_key, "join finds unique data record")
                replies.append((origin, *payload))
        replies.sort()
        distance = [distance[i] + replies[i][2] for i in range(len(arcs))]
        successor = [row[1] for row in replies]
    rank = [len(arcs)-1-value for value in distance]
    require(all(rank[i] == expected_rank[i] for i in range(len(arcs))), "pointer-doubling ranks")
    children, negative = [], 0
    for e, (u, v) in enumerate(edges):
        child = v if rank[2*e] < rank[2*e+1] else u
        children.append(child)
        negative ^= int(child == v)  # Incidence row is + at u, - at v.
    require(sorted(children) == [v for v in range(n) if v != root], "one edge per nonroot child")
    sign = -1 if (bitonic_parity(children) ^ negative) else 1
    return sign, children, repeated_keys_seen


def bfs_children(n, edges, root):
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    parent, queue = {root: None}, [root]
    for u in queue:
        for v in adjacency[u]:
            if v not in parent:
                parent[v] = u
                queue.append(v)
    return [v if parent[v] == u else u for u, v in edges]


def prufer_tree(n, sequence):
    degrees = [1] * n
    for v in sequence:
        degrees[v] += 1
    edges = []
    for v in sequence:
        leaf = next(u for u in range(n) if degrees[u] == 1)
        edges.append((leaf, v))
        degrees[leaf] -= 1
        degrees[v] -= 1
    ends = [u for u in range(n) if degrees[u] == 1]
    edges.append(tuple(ends))
    return edges


def check_tree_signs():
    tested, repeated = 0, 0
    for n in range(2, 7):
        for sequence in itertools.product(range(n), repeat=n-2):
            edges = prufer_tree(n, sequence)
            # Exercise noncanonical row orientations and row permutations.
            edges = [(v, u) if (j+tested) % 3 == 0 else (u, v)
                     for j, (u, v) in enumerate(edges)]
            shift = tested % len(edges)
            edges = edges[shift:] + edges[:shift]
            sign, children, joins_repeated = tree_sign_euler(n, edges)
            require(children == bfs_children(n, edges, n-1), "Euler orientation versus BFS")
            require(sign == integer_det(incidence(n, edges)[:, :-1]), "Euler sign versus exact determinant")
            repeated += int(joins_repeated)
            tested += 1
    require(tested == 1441, "all labelled trees n=2,...,6 enumerated")
    require(repeated > 100, "absorbing-terminal repeated join keys exercised")
    return {"labelled_trees": tested, "maximum_vertices": 6,
            "cases_with_repeated_join_keys": repeated,
            "checks": ["Euler cycle", "pointer-join ranks", "BFS orientation", "exact determinant"]}


def apply_axis(matrix, tensor, axis):
    return np.moveaxis(np.tensordot(matrix, tensor, axes=(1, axis)), 0, axis)


def inversion_sign(values):
    inversions = sum(values[i] > values[j] for i in range(len(values))
                     for j in range(i+1, len(values)))
    return -1 if inversions % 2 else 1


def uniform_householder(length):
    target = np.ones(length) / math.sqrt(length)
    zero = np.eye(length)[:, 0]
    delta = zero-target
    return np.eye(length) if norm(delta) < TOL else (
        np.eye(length)-2*np.outer(delta, delta)/np.dot(delta, delta))


def check_end_to_end(cached):
    reports = []
    for case in ("K4", "C5", "K3_3"):
        n, data = cached[case]
        particles, m = n-1, len(data["edges"])
        permutations = list(itertools.permutations(range(particles)))
        signs = [inversion_sign(p) for p in permutations]
        tensor = np.zeros((n,) * particles, dtype=complex)
        for permutation, sign in zip(permutations, signs):
            tensor[tuple(j+1 for j in permutation)] = sign / math.sqrt(math.factorial(particles))
        # Actual sequence: known antisymmetric orbital labels -> Fourier -> polar/fold.
        for axis in range(particles):
            tensor = apply_axis(fourier(n), tensor, axis)
        for axis in range(particles):
            tensor = apply_axis(data["fold"] @ data["w"], tensor, axis)
        small(abs(float(np.vdot(tensor, tensor).real)-1), "many-particle unit norm")
        subsets = list(itertools.combinations(range(m), particles))
        sorted_flags = np.zeros((len(subsets), len(permutations)), dtype=complex)
        amplitudes = np.zeros(len(subsets), dtype=complex)
        for j, subset in enumerate(subsets):
            amplitudes[j] = np.linalg.det(data["x"][list(subset), :])
            for k, (permutation, sign) in enumerate(zip(permutations, signs)):
                ordered = tuple(subset[i] for i in permutation)
                sorted_flags[j, k] = sign * tensor[ordered]
        resource = np.ones(len(permutations))/math.sqrt(len(permutations))
        factor_error = float(np.linalg.norm(sorted_flags-amplitudes[:, None]*resource[None, :]))
        small(factor_error, "sorting records independent of tree subset")
        cleaned = sorted_flags @ uniform_householder(len(permutations))
        garbage_norm = float(np.linalg.norm(cleaned[:, 1:]))
        small(garbage_norm, "inverse universal permutation resource cleans records")
        positive = cleaned[:, 0].copy()
        tree_rows = []
        for j, subset in enumerate(subsets):
            edges = [data["edges"][i] for i in subset]
            if is_tree(n, edges):
                positive[j] *= tree_sign_euler(n, edges)[0]
                tree_rows.append(j)
        expected = np.zeros(len(subsets), dtype=complex)
        expected[tree_rows] = 1/math.sqrt(len(tree_rows))
        phase = np.vdot(expected, positive)
        phase /= abs(phase)
        final_error = float(np.linalg.norm(positive-phase*expected))
        small(final_error, "final positive sorted-tree q-sample")
        reports.append({"graph": case, "ordered_tensor_entries": int(tensor.size),
                        "output_encoding": "sorted canonical-arc subsets; endpoint interpretation uses the explicit test graph",
                        "permutation_resource_dimension": len(permutations),
                        "record_factorization_error": factor_error,
                        "residual_garbage_norm": garbage_norm,
                        "final_state_error_up_to_global_phase": final_error})
    return reports


def odd_bounded_polynomial(singular, order):
    """p(s)=integral_0^s(1-t^2)^k dt / integral_0^1(...).

    A stable recurrence evaluates an explicit bounded odd polynomial. Its degree
    is NOT advertised as the optimal QSVT sign-approximation degree.
    """
    singular = np.asarray(singular, dtype=float)
    integral, normalization = singular.copy(), 1.0
    for k in range(1, order+1):
        integral = (singular*(1-singular**2)**k+2*k*integral)/(2*k+1)
        normalization *= 2*k/(2*k+1)
    return integral/normalization


def check_approximation_and_leakage(cached):
    n, data = cached["K3_3"]
    polynomial_reports = []
    for order in (1, 4, 12, 32):
        grid = np.linspace(-1, 1, 1001)
        values = odd_bounded_polynomial(grid, order)
        require(np.max(abs(values)) <= 1+1e-12, "test polynomial bounded on unit interval")
        small(np.max(abs(values+values[::-1])), "test polynomial odd")
        p = odd_bounded_polynomial(data["singular"], order)
        require(np.max(p) <= 1+1e-12, "singular-response evaluation within roundoff of contraction")
        p = np.clip(p, -1, 1)  # Roundoff at the exact endpoint p(1)=1.
        delta = max(0.0, float(np.max(1-p)))
        # Full dilation includes orthogonal failure flags, not just a good block.
        single_dilation_error = float(np.max(np.sqrt(2-2*p)))
        many_dilation_error = math.sqrt(max(0, 2-2*float(np.prod(p))))
        require(single_dilation_error <= math.sqrt(2*delta)+TOL, "full single-particle leakage budget")
        require(many_dilation_error <= math.sqrt(2*(n-1)*delta)+TOL, "occupied-wedge dilation budget")
        polynomial_reports.append({"degree": 2*order+1, "good_block_error": delta,
                                   "single_dilation_state_error": single_dilation_error,
                                   "many_particle_dilation_error": many_dilation_error})
    # A generic small unitary error creates genuine non-tree leakage. Sign cleanup
    # leaves that leakage present; it cannot silently project it away.
    m, particles = len(data["edges"]), n-1
    rng = np.random.default_rng(20261115)
    h = rng.normal(size=(m, m)) + 1j*rng.normal(size=(m, m))
    h = (h+h.conj().T)/2
    h /= norm(h)
    eig, basis = np.linalg.eigh(h)
    subsets = list(itertools.combinations(range(m), particles))
    ideal = np.array([np.linalg.det(data["x"][list(s), :]) for s in subsets])
    is_tree_mask = np.array([is_tree(n, [data["edges"][i] for i in s]) for s in subsets])
    phase_signs = np.array([tree_sign_euler(n, [data["edges"][i] for i in s])[0]
                           if tree else (-1 if j % 2 else 1)
                           for j, (s, tree) in enumerate(zip(subsets, is_tree_mask))])
    leakage_reports = []
    for theta in (1e-4, 1e-2):
        perturbation = (basis*np.exp(1j*theta*eig)) @ basis.conj().T
        perturbed_x = perturbation @ data["x"]
        noisy = np.array([np.linalg.det(perturbed_x[list(s), :]) for s in subsets])
        distance = float(np.linalg.norm(noisy-ideal))
        cleaned_distance = float(np.linalg.norm(phase_signs*noisy-phase_signs*ideal))
        non_tree_probability = float(np.sum(abs(noisy[~is_tree_mask])**2))
        require(non_tree_probability > 0, "generic perturbation actually reaches non-trees")
        small(abs(cleaned_distance-distance), "total phase correction preserves approximation error")
        require(distance <= particles*theta+TOL, "independent-particle unitary hybrid bound")
        small(abs(float(np.vdot(noisy, noisy).real)-1), "perturbed exterior state norm")
        leakage_reports.append({"one_particle_rotation_angle": theta,
                                "non_tree_probability": non_tree_probability,
                                "state_error_before_cleanup": distance,
                                "state_error_after_cleanup": cleaned_distance})
    return {"bounded_polynomial_dilation": polynomial_reports, "generic_unitary_leakage": leakage_reports}


def check_irregular_boundary():
    n, edges = 4, [(0, 1), (0, 2), (0, 3)]
    try:
        port_matrices(n, edges, 0)
    except AssertionError as error:
        require("regular graph" in str(error), "irregular input rejected for stated reason")
    else:
        raise AssertionError("irregular graph silently accepted")
    # If one naively uses a locally normalized coin on an irregular graph, the
    # null vector is sqrt(degree), so the advertised uniform-complement input fails.
    degrees = np.array([3, 1, 1, 1], dtype=float)
    arcs = [(u, v) for u, v in edges for u, v in ((u, v), (v, u))]
    lookup = {arc: i for i, arc in enumerate(arcs)}
    r = np.eye(len(arcs))[[lookup[(v, u)] for u, v in arcs]]
    v = np.zeros((len(arcs), n))
    for i, (u, _) in enumerate(arcs):
        v[i, u] = 1/math.sqrt(degrees[u])
    a = (v-r@v)/2
    uniform_residual = float(np.linalg.norm(a @ (np.ones(n)/math.sqrt(n))))
    actual_null = np.sqrt(degrees)/math.sqrt(sum(degrees))
    small(np.linalg.norm(a @ actual_null), "irregular weighted null vector")
    require(uniform_residual > 0.1, "irregular counterexample is quantitatively nontrivial")
    # Disconnected regular graphs have larger nullity and cannot use n-1 orbitals.
    disconnected = [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5)]
    data = port_matrices(6, disconnected, 19)
    rank = int(np.linalg.matrix_rank(data["a"], tol=1e-11))
    require(rank == 4, "two components yield rank n-2")
    return {"irregular_graph": "four-vertex star", "uniform_null_residual": uniform_residual,
            "disconnected_regular_rank": rank,
            "limits": "Regularity and connectivity are actual input promises."}


def hidden_bit_graph(base_n, base_edges, bits):
    """Cubic base: subdivide every edge and attach the five-vertex K4 gadget."""
    require(len(bits) == len(base_edges), "one bit per base edge")
    edges, bridges, permutations = [], [], []
    next_vertex = base_n
    for (u, v), bit in zip(base_edges, bits):
        z, a, b, c, d, p = range(next_vertex, next_vertex+6)
        next_vertex += 6
        gadget = [(a, c), (a, d), (b, c), (b, d), (c, d), (a, p), (b, p)]
        mapping = {a: p, p: a} if bit else {}
        transform = lambda x: mapping.get(x, x)
        edges.extend([(u, z), (z, v)])
        edges.extend((transform(x), transform(y)) for x, y in gadget)
        bridge = (z, transform(p))
        edges.append(bridge)
        bridges.append(bridge)
        permutations.append(mapping)
    return next_vertex, edges, bridges


def connected_without(n, edges, omitted):
    adjacency = [[] for _ in range(n)]
    for j, (u, v) in enumerate(edges):
        if j != omitted:
            adjacency[u].append(v)
            adjacency[v].append(u)
    reached, queue = {0}, [0]
    for u in queue:
        for v in adjacency[u]:
            if v not in reached:
                reached.add(v)
                queue.append(v)
    return len(reached) == n


def check_lower_gadgets():
    reports = []
    for name, base_n, base_edges in (("K4", 4, complete_graph(4)), ("cube", 8, cube_graph())):
        patterns = [tuple(0 for _ in base_edges), tuple(1 for _ in base_edges),
                    tuple(j % 2 for j in range(len(base_edges)))]
        gaps = []
        for bits in patterns:
            n, edges, bridges = hidden_bit_graph(base_n, base_edges, bits)
            b = incidence(n, edges)
            laplacian = b.T @ b
            require(np.all(np.diag(laplacian) == 3), "hidden-bit graph is cubic")
            eigen = np.linalg.eigvalsh(laplacian/3)
            require(eigen[1] > 0, "hidden-bit graph connected")
            require(n == 10*base_n, "fixed tenfold vertex blowup")
            gaps.append(float(eigen[1]))
            base_b = incidence(base_n, base_edges)
            base_gamma = float(np.linalg.eigvalsh(base_b.T @ base_b/3)[1])
            conservative_bound = 1/(432+76/base_gamma)
            require(eigen[1] >= conservative_bound-TOL, "finite gadget gap above written conservative bound")
            for bit, bridge, edge in zip(bits, bridges, base_edges):
                index = edges.index(bridge)
                require(not connected_without(n, edges, index), "bridge in every spanning tree")
                z, a, _, _, _, p = range(base_n+6*base_edges.index(edge), base_n+6*base_edges.index(edge)+6)
                decoded = int(bridge[1] == a)
                require(decoded == bit and bridge[0] == z, "forced bridge reveals bit")
        small(max(gaps)-min(gaps), "bit relabeling preserves complete spectrum")
        reports.append({"base": name, "base_vertices": base_n, "output_vertices": 10*base_n,
                        "bits": len(base_edges), "tested_patterns": len(patterns),
                        "base_normalized_gap": base_gamma, "normalized_gap": gaps[0],
                        "written_conservative_gap_bound": conservative_bound,
                        "gap_spread_across_bits": max(gaps)-min(gaps),
                        "forced_bridge_checks": len(base_edges)*len(patterns)})
    return reports


def run():
    minors, cached = check_minors()
    return {
        "status": "passed",
        "scope": "Deterministic dense small-instance mathematical support, not an all-size or circuit certification.",
        "numpy_version": np.__version__,
        "tolerance": TOL,
        "incidence_polar_and_minors": minors,
        "sign_routine": check_tree_signs(),
        "end_to_end_states": check_end_to_end(cached),
        "approximation_and_leakage": check_approximation_and_leakage(cached),
        "promise_boundaries": check_irregular_boundary(),
        "hidden_bit_lower_gadgets": check_lower_gadgets(),
        "not_verified": ["optimal-degree QSVT synthesis", "elementary gate counts or device execution",
                         "efficient clean endpoint conversion for arbitrary port orders (the endpoint theorem requires sorted access)",
                         "arbitrary-size gap theorem or quantum query lower bound",
                         "full reversible bit-level sorting/list-ranking circuit",
                         "hosted mathematical rendering or release readiness"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="write the complete deterministic report to this path")
    args = parser.parse_args()
    report = run()
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print("PASS: incidence/polar/minors; 1,441 labelled-tree signs; three end-to-end states;")
    print("      dilation/leakage, promise boundaries, and two cubic hidden-bit gadget families.")
    if args.json:
        print(f"JSON report: {args.json}")


if __name__ == "__main__":
    main()
