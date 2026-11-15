# From graph incidence to coherent trees

A spanning tree is a connected, cycle-free set of $n-1$ edges. A uniform classical sample returns one such set. Here the output is the quantum state with the same positive amplitude on every spanning tree, encoded as a sorted edge list, and with every work register returned to zero. A clean preparation unitary also gives its inverse and a reflection about the output state. Conventional endpoint output uses the sorted-access promise in the [model](model.md); an arbitrary port ordering alone does not supply a cheap inverse neighbour-index lookup.

The [model and theorem](model.md) state the exact promises and costs. This page explains how the proofs fit together.

## The one-particle ingredient

Let $P$ be the simple random-walk matrix of a connected regular graph. A uniform port isometry $V$ and the graph-rotation involution $R$ implement

```math
A=\frac{I-R}{2}V,
\qquad A^\dagger A=\frac{I-P}{2}.
```

The uniform vertex vector is its only null vector. The remaining singular values are at least $\sqrt{\gamma/2}$ when the normalized-Laplacian gap is at least $\gamma$. Quantum singular-value transformation turns $A$ into its polar isometry on that known complement. [Polar transport](polar_transport.md) gives the actual projected-unitary encoding, orientation folding and leakage bound. No degree-dependent normalization penalty is inserted.

## The many-particle determinant

Write $B$ for an oriented edge-by-vertex incidence matrix, $L=B^\dagger B$, and $Q$ for any efficiently generated orthonormal basis of the uniform vertex complement. After folding arcs into edges, the transported columns are

```math
C=BQ(Q^\dagger LQ)^{-1/2},
\qquad C^\dagger C=I_{n-1}.
```

An antisymmetric state occupying all $n-1$ columns has sorted edge-subset amplitude $\det C_S$. For a non-tree subset of $n-1$ edges, the incidence rank is deficient and this determinant vanishes. For a tree, the matrix-tree theorem and the unit magnitude of a reduced incidence determinant give

```math
\det C_T=e^{i\theta}\frac{\det \overline B_T}{\sqrt{\tau(G)}},
\qquad \det\overline B_T\in\{-1,1\},
```

where $\theta$ is independent of the tree and $\overline B_T$ deletes one fixed root column. Thus the only tree-dependent phase is a sign that can be computed from the tree itself.

[Clean coherent preparation](coherent_preparation.md) proves both the determinant identity and the complete circuit. Its graph-independent permutation resource is reused by the same fixed sorting network before and after transport. The resource is unprepared coherently, rather than discarded as a random seed.

## A sign that is cheap to compute

Root the input tree at a fixed vertex. Each edge has one child endpoint. The determinant sign is the parity of the permutation ordering edges by child label, multiplied by the signs of their child incidence entries. Euler-tour list ranking finds those child endpoints through fixed sorting-network joins. Compute the sign, apply its phase and reverse the computation.

[Sign cleanup](sign_cleanup.md) supplies the all-size proof, pseudocode and soft-linear gate and workspace bounds, including total unitary behavior on malformed lists. A [four-cycle example](interpretation.md#four-cycle-worked-example) shows an actual negative branch and its correction.

## Accuracy and the charged comparison

The one-particle singular-value approximation is chosen tightly enough to bound the full dilation leakage, not only its successful block. Errors then add over the $n-1$ particles and the reversible processing. [Resources](resources.md) accounts for graph queries, ordinary gates, input-interface implementation, signal-processing phase compilation, workspace and controlled inverses.

The [lower-bound family](lower_bound.md) consists of constant-gap cubic graphs with hidden labels on forced bridges. Every endpoint-encoded tree reveals all hidden bits. Oracle interrogation therefore requires $\Omega(n)$ queries even at constant gap and constant error. This establishes the vertex scaling, while leaving sharp gap dependence open.

The [related-work account](../references/related_work.md) credits polar QSVT, fermionic antisymmetrization, determinant samplers and the matrix-tree theorem. The resulting contribution is the charged local-oracle compiler into a clean positive tree state; general-purpose qsampling and classical sampling have different resource comparisons.
