# Quantum Spanning Tree Preparation

**Prepare an equal, positive superposition of a graph's spanning trees using local graph access.**

For a connected unweighted regular graph with $`n`$ vertices, normalized-Laplacian gap at least $`\gamma`$, and sorted coherent neighbour access, the construction prepares

```math
|\mathrm{UST}(G)\rangle
=\frac{1}{\sqrt{\tau(G)}}\sum_{T\text{ spanning tree of }G}|T\rangle
```

with cleaned work registers and error at most $`\epsilon`$. A tree is stored as its sorted list of vertex endpoint pairs. The cost is $`\widetilde O(n/\sqrt{\gamma})`$ coherent graph-rotation calls and $`\widetilde O(n)`$ non-oracle qubits. Elementary gates cost $`\widetilde O((C_R+1)n/\sqrt{\gamma})`$, where $`C_R`$ is the implementation cost of one graph-rotation call. Input-oracle construction and classical signal-processing compilation are charged separately in the [resource theorem](science/resources.md).

The endpoint encoding requires ports indexed by increasing neighbour label, or a separately supplied and paid inverse-index locator. The [model](science/model.md) also gives the conversion from sorted adjacency-list queries to rotation calls. Arbitrarily ordered ports suffice for the polar map, but their indices cannot be erased by an unpaid inverse lookup.

At fixed positive gap, the quantum circuit cost is nearly linear when graph access has polylogarithmic implementation cost. A [query lower bound](science/lower_bound.md) proves that linear dependence on $`n`$ is necessary on an infinite family of constant-gap cubic graphs. The dependence on a vanishing gap is not claimed optimal.

## Why the construction works

The graph's incidence map turns vertex amplitudes into edge differences. Its polar isometry carries a known orthogonal vertex subspace into the graph's cut space. Applying this map to a first-quantized fermionic state produces determinants: non-tree edge subsets cancel, and every spanning tree has the same amplitude magnitude. A reversible rooting-and-sorting circuit computes and removes the remaining incidence-determinant sign.

The result is a clean preparation circuit with an inverse. It can therefore supply coherent tree samples and reflections about the prepared state. The construction uses no internal QRAM, dense orthogonalization, or determinant-dependent postselection. The supplied graph-access circuit remains an explicit resource.

## Read the science

Start with the [scientific overview](science/README.md), or choose a question.

| Question | Authoritative account |
| --- | --- |
| What is the exact input, output and error guarantee? | [Model and preparation theorem](science/model.md) |
| How does local graph access implement the polar incidence map? | [Polar transport](science/polar_transport.md) |
| How are fermionic sorting records prepared and erased coherently? | [Clean coherent preparation](science/coherent_preparation.md) |
| How can the tree signs be removed without QRAM? | [Reversible sign cleanup](science/sign_cleanup.md) |
| What is paid in queries, gates, compilation and workspace? | [Resource accounting](science/resources.md) |
| Why is the vertex dependence unavoidable? | [Endpoint-output lower bound](science/lower_bound.md) |
| What happens on a four-cycle, and what does the result enable? | [Worked example and interpretation](science/interpretation.md) |
| Which ingredients and comparisons are inherited? | [Related work](references/related_work.md) and [bibliography](references/references.bib) |

The [LLM reading guide](llms.txt) maps scientific questions to these same sources.

## Learn the construction

The single educational anchor is **Andrew M. Childs, _Lecture Notes on Quantum Algorithms_, 17 April 2025**. Start with the [four-cycle learning route](learning/README.md), use the [source-to-project bridge](learning/anchor_bridge.md), then follow the [30-milestone map](learning/milestones.md): 14 background targets and 16 targets assembling the construction, complete costs and endpoint lower bound. The final targets synthesize the actual capability and its limitations.

## Scope of the advance

The central capability is coherent preparation of a **positive** tree superposition, including its clean inverse, on gap-promised regular graphs. In the dense regime covered by its formal theorem, the [current general-purpose tree qsampler](https://arxiv.org/abs/2609.40314) has a one-sample query cost of $`\widetilde O(\sqrt{mn})`$ including preprocessing, for $`m`$ edges. The present bound specializes to $`\widetilde O(n)`$ at constant gap, including dense regular graphs, and explicitly counts the ordinary circuit work. The [comparison](references/related_work.md) explains the different promises and inherited ingredients.

Ordinary classical spanning-tree sampling on well-connected regular graphs already admits near-linear methods. This work makes no classical-output sampling advantage, arbitrary weighted or irregular graph theorem, practical crossover, or gap-optimality claim. A generic graph table is not treated as a free reversible lookup circuit.

## Reproduce the finite checks

Follow the commands and tested boundaries in [verification](verification/README.md). The checks examine incidence normalization, tree amplitudes, clean sorting conventions, reversible rooting and hidden-bit lower-bound gadgets. Finite computations support the analytical proofs; they do not certify arbitrary-size correctness or a hardware speedup.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
