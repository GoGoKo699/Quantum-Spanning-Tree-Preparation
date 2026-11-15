# Learning the spanning-tree preparation algorithm

A spanning tree connects every vertex of a graph without a cycle. The task here is to prepare a pure quantum state that gives every spanning tree the same positive amplitude, while returning the circuit's working registers to zero. That clean output can be kept coherent and used with the preparation circuit's inverse.

Begin with the [worked four-cycle route](anchor_bridge.md#a-four-cycle-from-input-to-clean-output). It follows one graph through the output state, local graph access, polar transport, determinant signs and cleanup. The [30-milestone map](milestones.md) then organizes the full account into background and the algorithm's narrative.

## One selected anchor

The educational anchor is **Andrew M. Childs, _Lecture Notes on Quantum Algorithms_, 17 April 2025**. The [author's source page](https://www.cs.umd.edu/~amchilds/qa/) identifies the notes; the dated [author-hosted text](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) is the version used here. The [bridge](anchor_bridge.md#how-the-anchor-connects-to-this-project) points to the relevant sections and supplies the graph, determinant and cleanup steps specific to this result.

The notes provide the algorithmic foundations. The project supplies the complete spanning-tree construction. Primary research citations remain in [related work](../references/related_work.md); they identify imported proof ingredients rather than additional educational anchors.

## Reader routes

| Route | Start | What it develops |
| --- | --- | --- |
| Concrete example | [Four-cycle route](anchor_bridge.md#a-four-cycle-from-input-to-clean-output) | Why equal tree probabilities are insufficient, how determinant signs arise, and why work must be cleaned |
| Full conceptual map | [M01–M30](milestones.md) | Fourteen background targets followed by sixteen targets assembling the algorithm and its boundaries |
| Mathematical construction | [Model](../science/model.md), then [science index](../science/README.md) | Exact assumptions, theorem, proofs and resource accounting |
| Checks and examples | [Verification](../verification/README.md) | What the reproducible finite checks establish and where the proofs are needed |

The background phase starts with a single graph, a register and a reversible operation, then joins them into the language of graph oracles, spectral gaps and singular-value transformations. The narrative phase starts with the incidence map and assembles the occupied vertex subspace, clean permutation resource, edge-state transport, positive sign correction and final resource claim. Its last targets bring those pieces together; the map is not a list of thirty independent topics.

## The complete claim in one place

For a connected, simple, unweighted regular graph on $`n`$ vertices, assume a known lower bound $`\gamma>0`$ on its normalized-Laplacian gap. Conventional endpoint output uses a rotation map whose ports follow increasing neighbor order, or sorted adjacency-list access. Access to an arbitrary classical edge table is not supplied for free.

The preparation uses

$$
O\!\left(n\gamma^{-1/2}\log\frac n\epsilon\right)
$$

rotation calls, up to the stated extra logarithmic conversion factor for sorted adjacency-list queries. If one clean rotation circuit costs $`C_R`$ gates and $`S_R`$ scratch qubits, the quantum cost is

$$
\widetilde O\!\left(n\gamma^{-1/2}(C_R+1)\right)
\quad\text{gates},\qquad
\widetilde O(n)+O(S_R)
\quad\text{qubits}.
$$

The work return and output error are one joint-state guarantee. The classical phase-compilation cost $`C_{\mathrm{phase}}`$ is also charged: at fixed positive gap it is polylogarithmic in the size and accuracy parameters, while a shrinking-gap total-time claim must retain it explicitly. See [resources](../science/resources.md) for the complete conventions.

At constant gap and inexpensive supplied graph access, this gives a nearlinear circuit for a clean positive tree state. Classical random-tree sampling on such graphs is already nearlinear. The coherent state, its inverse and the explicit cleanup are the capability established here.

[Return to the project](../README.md)

