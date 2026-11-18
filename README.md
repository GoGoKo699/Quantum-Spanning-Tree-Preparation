# Quantum Spanning Tree Preparation

**Prepare a clean, positive superposition of weighted spanning trees using sorted local graph access.**

For a connected simple graph with positive edge weights, let $`w(T)=\prod_{e\in T}w_e`$ be the weight of tree $`T`$ and let $`Z_w`$ be the sum of these weights over all spanning trees. The preparation circuit outputs

```math
|\pi_w\rangle=\sum_{T\text{ spanning tree of }G}\sqrt{\frac{w(T)}{Z_w}}\,|T\rangle,
```

where $`|T\rangle`$ stores the sorted list of vertex endpoint pairs. The output and all circuit work registers jointly approximate the target state with zero work to error at most $`\epsilon`$. The circuit can be inverted for coherent use.

Let $`n`$ be the number of vertices, $`\kappa=w_{\max}/w_{\min}`$ the supplied weight-range bound, and $`\gamma`$ a known lower bound on either the weighted or unweighted normalized-Laplacian gap. The [weighted preparation theorem](science/weighted_preparation.md) uses $`\widetilde O(n\sqrt{\kappa/\gamma})`$ queries to coherent degrees and sorted weighted adjacency lists. It charges the oracle implementation, finite-precision arithmetic and graph-independent phase compilation. The graph can be irregular. The [regular unweighted construction](science/model.md) also supports a supplied sorted rotation map and uses $`\widetilde O(n/\sqrt{\gamma})`$ rotation calls.

On a [dense hard family](science/weight_contrast_lower_bound.md), both normalized gaps are bounded below by a constant. For integer $`8\le\kappa\le n/2`$ in that family, one coherent sample requires $`\Omega(n\sqrt{\kappa})`$ quantum queries and one classical sample requires $`\Omega(n\kappa)`$ expected queries at fixed small error. Measuring the preparation circuit gives a classical sample within the same quantum query upper bound, yielding a quadratic separation in weight contrast up to logarithmic factors. The separation concerns the supplied local-oracle model. Gap dependence and physical runtime have separate resource requirements.

## Why the construction works

The degree-rooted vertex state spans the kernel of the weighted incidence block. Preparing the antisymmetric state of all modes perpendicular to this single missing mode supplies the input to polar transport. After transport, the determinants vanish for non-trees and give the square roots of the tree weights, up to normalization and a sign. Reversible rooting and sorting remove that sign and erase the circuit records. Sorted neighbor order supplies the inverse port lookup for endpoint output.

## Read the science

| Question | Authoritative account |
| --- | --- |
| How do the results fit together? | [Scientific overview](science/README.md) |
| How does the compiler handle weights and irregular degrees? | [Weighted preparation and resource theorem](science/weighted_preparation.md) |
| Why is square-root weight contrast necessary? | [Quantum and classical weight-query lower bounds](science/weight_contrast_lower_bound.md) |
| What does the regular unweighted specialization assume? | [Model and theorem](science/model.md), [polar transport](science/polar_transport.md), [resources](science/resources.md) |
| How are determinants and sorting records produced coherently? | [Clean coherent preparation](science/coherent_preparation.md) |
| How are tree signs computed and removed? | [Reversible sign cleanup](science/sign_cleanup.md) |
| Why does the unweighted query cost have a linear vertex term? | [Cubic-graph lower bound](science/lower_bound.md) |
| What happens on a four-cycle? | [Worked example and interpretation](science/interpretation.md) |
| How does this compare with existing algorithms? | [Related work](references/related_work.md) and [bibliography](references/references.bib) |

The [LLM reading guide](llms.txt) maps scientific questions to the same sources.

## Learn the construction

The educational anchor is **Andrew M. Childs, _Lecture Notes on Quantum Algorithms_, 17 April 2025**. The [learning route](learning/README.md) introduces the construction through a small graph. The [source-to-project bridge](learning/anchor_bridge.md) connects the notes to the proof, and the [30-milestone map](learning/milestones.md) follows 14 background targets and 16 targets that assemble the method and its bounds.

## Reproduce the finite checks

The reproducible checks cover incidence normalization, determinant amplitudes, coherent sorting and rooting conventions, and the lower-bound families. The analytical arguments give the all-size guarantees. [Verification commands and scope](verification/README.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
