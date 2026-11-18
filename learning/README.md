# Learning the spanning-tree preparation algorithm

A spanning tree connects every vertex of a graph without a cycle. The task here is to prepare a pure quantum state whose positive amplitudes have squares proportional to the products of the edge weights in each tree. Equal edge weights give a uniform tree state. The circuit returns its work registers to zero in the same accuracy guarantee, so the tree state can be kept coherent and the preparation inverted.

Begin with the [worked four-cycle route](anchor_bridge.md#a-four-cycle-from-input-to-clean-output). Follow the circuit on a uniform cycle, then [add one weighted diagonal](anchor_bridge.md#one-weighted-diagonal-changes-the-input-state) and see how it changes the occupied subspace and tree amplitudes. The [30-milestone map](milestones.md) traces the construction and the query lower bounds.

## One selected anchor

The educational anchor is **Andrew M. Childs, _Lecture Notes on Quantum Algorithms_, 17 April 2025**. The [author's source page](https://www.cs.umd.edu/~amchilds/qa/) identifies the notes; the dated [author-hosted text](https://www.cs.umd.edu/~amchilds/qa/qa.pdf) is the version used here. The [bridge](anchor_bridge.md#how-the-anchor-connects-to-this-project) points to the relevant sections and supplies the graph, determinant and cleanup steps specific to this result.

The notes provide the algorithmic foundations. The project supplies the complete spanning-tree construction. Primary research citations remain in [related work](../references/related_work.md); they identify imported proof ingredients rather than additional educational anchors.

## Reader routes

| Route | Start | What it develops |
| --- | --- | --- |
| Concrete example | [Four-cycle route](anchor_bridge.md#a-four-cycle-from-input-to-clean-output) | How one weighted diagonal changes the null mode and tree amplitudes, and why the sign and sorting work must be cleaned |
| Full conceptual map | [M01–M30](milestones.md) | Fourteen background targets followed by sixteen targets assembling the algorithm and its boundaries |
| Mathematical construction | [Weighted preparation](../science/weighted_preparation.md) | Exact assumptions, theorem, proofs and resource accounting |
| Sharp contrast dependence | [Weight-query lower bounds](../science/weight_contrast_lower_bound.md) | A dense example that separates quantum and classical weight queries even when both normalized gaps stay positive |
| Checks and examples | [Verification](../verification/README.md) | What the reproducible finite checks establish and where the proofs are needed |

The background phase introduces graph oracles, spectral gaps and singular-value transformations through the running example. The narrative phase builds the weighted incidence map, prepares the excluded degree-rooted mode as an omitted vertex, and follows the occupied modes through polar transport, sorting and sign correction. Its last targets derive the query separation on a new family of graphs.

## The complete claim in one place

Start with a connected simple graph on $`n`$ vertices, positive weights in a supplied range $`[w_{\min},w_{\max}]`$ and a known lower bound $`\gamma>0`$ on either the weighted or unweighted normalized-Laplacian gap. The graph access provides ordinary vertex degrees, plus neighbors and edge weights in sorted port order. Write $`\kappa=w_{\max}/w_{\min}`$ for the promised contrast.

The preparation uses the following number of coherent queries.

```math
\widetilde O\!\left(n\sqrt{\frac{\kappa}{\gamma}}\right).
```

The bound includes the one-time degree-state preparation, the polar transport on $`n-1`$ registers and the endpoint conversion. The quantum gate and workspace accounting also charges the supplied oracle circuits, reversible arithmetic on their finite-bit inputs, and sorting and sign correction. The precision budget covers the tree and work registers together. The [resource proof](../science/weighted_preparation.md#joint-error-and-resource-accounting) spells out the logarithmic factors and charges classical phase compilation separately.

For dense examples with fixed normalized gaps and growing contrast in the stated range, one quantum tree sample needs $`\Omega(n\sqrt{\kappa})`$ queries and one classical tree sample needs $`\Omega(n\kappa)`$ expected queries in the same access model. The separation concerns queries on that family. See the [weight-query lower bounds](../science/weight_contrast_lower_bound.md) and the [regular unweighted baseline](../science/model.md).

[Return to the project](../README.md)

