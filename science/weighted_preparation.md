# Weighted spanning trees on irregular graphs

On a regular graph, the incidence map kills the uniform vertex state. On an irregular graph, the corresponding null vector has amplitudes proportional to square roots of degrees. Preparing one copy of that vector suffices to specify the entire occupied fermionic subspace. Edge weights then enter through a local rotation before the incidence polar transformation.

## Access model and theorem

Let $`G=(V,E)`$ be a connected simple graph on $`n\ge2`$ labelled vertices. Each edge has an exactly specified positive weight $`w_e`$ in a fixed-point representation with $`b`$ bits. Supply bounds $`0\lt w_{\min}\le w_e\le w_{\max}`$, with $`\kappa=w_{\max}/w_{\min}`$. The bounds use the same representation or are given at sufficient precision as outward bounds. The coherent graph interface returns the number $`d_v`$ of neighbours of a vertex, or a sorted port's neighbour and weight. The two ends of an edge give the same weight. As in the [regular model](model.md), access extends reversibly to padded labels.

Put $`D=\mathrm{diag}(d_v)`$, let $`B`$ be the oriented edge-by-vertex incidence, and put $`W=\mathrm{diag}(w_e)`$. Write $`L_0=B^\dagger B`$, $`L_w=B^\dagger W B`$ and $`D_w=\mathrm{diag}(\sum_{e\ni v}w_e)`$. Supply a positive lower bound $`\gamma`$ on the second eigenvalue of either $`D^{-1/2}L_0D^{-1/2}`$ or $`D_w^{-1/2}L_wD_w^{-1/2}`$. If both bounds are supplied, use the larger one. These gaps do not require a bound on the absolute random-walk spectrum.

**Theorem.** For $`0\lt\epsilon\lt1/10`$, the preparation unitary outputs, up to global phase and joint norm error $`\epsilon`$, the state

```math
|\pi_w\rangle |0\rangle_{\rm work}
=
\frac{1}{\sqrt{Z_w}}
\sum_{T\text{ spanning tree}} \sqrt{\prod_{e\in T} w_e}\,
|T\rangle |0\rangle_{\rm work},
\qquad
Z_w=\sum_{T\text{ spanning tree}}\prod_{e\in T}w_e.
```

The output encodes a tree as its sorted endpoint list. The number of sorted local queries is $`\widetilde O(n\sqrt{\kappa/\gamma})`$. The inverse uses the same resources. One may also attach each edge weight to its endpoint pair coherently in $`O(n\log n)`$ additional sorted local queries.

## The normalized incidence block

Compute $`d_v`$, prepare a uniform coin on ports $`0,\ldots,d_v-1`$, and uncompute the degree. The range-preparation circuit of the [regular construction](coherent_preparation.md#a-known-basis-of-the-correct-vertex-subspace) works with a quantum control for the upper bound. At each bit, the number of completions of a prefix is the size of its interval intersected with $`[0,d_v)`$. Compute the two counts, rotate by the square root of their ratio, and reverse the count circuit. Defaults on empty intervals and padded labels make the operation total.

Let $`V`$ be this variable-length coin isometry. Query a weight, rotate a flag so its success amplitude is $`\sqrt{w_e/w_{\max}}`$, and reverse the weight query. On valid ports, the diagonal success block $`F`$ commutes with the port reversal $`R`$ because the two directions of each edge have the same weight. Use the [controlled reversal](polar_transport.md#an-explicit-projected-unitary-encoding) after the weight flag, leaving the flag untouched. The joint success projection selects $`(I-R)FV/2`$. Fold the antisymmetric port pair into a canonical edge and the same orientation state for every edge. The resulting one-particle block is

```math
A=\frac{1}{\sqrt{2w_{\max}}}W^{1/2}BD^{-1/2}.
```

The circuit performs the polar transformation in the port representation and folds each output slot once, after that transformation. The displayed block is its folded form. The input and success projectors use only the designated register values and have explicit reflections. The degree, reversal, weight and folding subroutines admit inverses. Each call uses $`O(\log n)`$ local queries including the reversible search for the reverse port. Invalid port labels can be left fixed by reversal, with a designated default flag rotation. The output on such labels is immaterial to the ideal block and their leakage under synthesis is covered by the joint norm error.

The matrix has operator norm at most one, since $`V`$ is an isometry and the flag and antisymmetric projections are contractions. Its kernel is the line spanned by

```math
|s_D\rangle=\frac{\sum_{v}\sqrt{d_v}|v\rangle}{\sqrt{\sum_v d_v}}.
```

For the unweighted gap promise, $`L_w\succeq w_{\min}L_0`$ gives the lower bound on all nonzero eigenvalues of $`A^\dagger A`$. For the weighted gap promise, $`D_w\succeq w_{\min}D`$ gives, for every nonzero $`x`$,

```math
\frac{x^\dagger L_w x}{x^\dagger D x}
\ge w_{\min}\frac{x^\dagger L_w x}{x^\dagger D_w x}.
```

Apply the generalized eigenvalue min-max principle before choosing any orthogonal complement. In either case the smallest positive singular value of $`A`$ is at least $`\sqrt{\gamma/(2\kappa)}`$. The weighted-gap route uses the unweighted degrees in the circuit. The weighted degrees enter only in the proof of the singular-value bound.

## Prepare the missing vertex once

Start with a uniform vertex and rotate a flag with success amplitude $`\sqrt{d_v/(n-1)}`$, uncomputing the degree. The good component is $`|s_D\rangle`$ with a fixed flag. Its success probability is $`2m/[n(n-1)]\ge 2/n`$, where $`m`$ is the number of edges. Coherent fixed-point amplitude amplification with this lower bound prepares the good component to joint norm error $`O(\epsilon)`$ in $`O(\sqrt n\log(1/\epsilon))`$ degree calls. The success phase is one scalar and the fixed flag can be flipped back. This use of [fixed-point amplification](https://doi.org/10.1103/PhysRevLett.113.210501) needs no graph-dependent success probability as input.

Given $`v`$, write the increasing list of all labels except $`v`$, apply the phase $`(-1)^v`$ for zero-based labels, and erase the hole register. The XOR of the listed labels and the fixed XOR of all valid labels equals the missing label. XOR it into the hole register to clear it without another graph query. The per-label map is reversible even though the list is populated in superposition.

Apply the existing [clean antisymmetrizer](coherent_preparation.md#a-universal-clean-permutation-resource) to that sorted list. The resulting exterior state is the signed sum of all basis wedges with one vertex omitted, with coefficient $`\langle v|s_D\rangle`$ and sign $`(-1)^v`$. Equivalently, it is the Hodge dual of the real vector $`s_D`$. In a real orthonormal basis starting with $`s_D`$, that dual is the unit wedge of the other $`n-1`$ basis vectors, up to orientation. It therefore occupies exactly the right singular subspace on which the polar factor is isometric. The algorithm prepares one missing-vertex state, with no list of graph-dependent orbitals.

## From the polar factor to positive weights

Apply the [polar transformation](polar_transport.md#the-polar-isometry-and-its-full-state-error) to the $`n-1`$ slots, fold the ports, and convert them into endpoints. For an orthonormal matrix $`Q`$ spanning the orthogonal complement of $`s_D`$, denote the transported orthonormal columns by $`C`$. The ideal edge-space wedge has sorted-set coefficient $`\det C_S`$.

The columns of $`C`$ span the same cut space as $`W^{1/2}\overline B`$, where $`\overline B`$ deletes one fixed root column from $`B`$. Indeed, $`D^{-1/2}`$ is invertible and deleting the root column preserves the image of $`B`$ by connectivity. Thus $`C=W^{1/2}\overline B M`$ for one invertible matrix $`M`$. For every edge subset $`S`$ of size $`n-1`$,

```math
\det C_S=\det M\,\det \overline B_S\,\sqrt{\prod_{e\in S}w_e}.
```

A non-tree has $`\det\overline B_S=0`$, and each tree has determinant of magnitude one. Normalization gives $`|\det M|=Z_w^{-1/2}`$. The common orientation phase is irrelevant. The remaining signs are the ordinary reduced-incidence signs, so the [rooted sign circuit](sign_cleanup.md) applies unchanged to the edge labels. Sorted endpoint conversion and erasure of the permutation record use the same [sorting identity](coherent_preparation.md#a-universal-clean-permutation-resource) for every term in the input wedge.

## Joint error and resource accounting

Set $`r=n-1`$. Choose the bounded odd polynomial for the polar block with error $`\delta=\Theta((\epsilon/r)^2)`$ on the positive singular interval. Its degree is

```math
D_{\rm pol}=O\!\left(\sqrt{\kappa/\gamma}\log\frac{n}{\epsilon}\right).
```

The successful block overlaps the ideal isometry by at least $`1-\delta`$ uniformly on the supported input subspace. The corresponding full-unitary one-slot error is at most $`\sqrt{2\delta}`$, including the flags and other leakage. The same bound holds on an entangled reference. In a slot-by-slot hybrid, every unprocessed ideal slot remains orthogonal to $`s_D`$. Allocate a fixed fraction of the error budget to the $`r`$ polar calls, one to the amplified hole, one to preparation and erasure of the permutation resource, and one to gate synthesis. Subsequent reversible operations preserve the norm budget. Endpoint conversion can append weights using reversible binary search and clean uncomputation.

There are $`O(rD_{\rm pol})`$ uses of the ideal incidence block, each with at most $`O(\log n)`$ local queries. Preparing the hole uses $`O(\sqrt n\log(1/\epsilon))`$ degree queries. Port folding, endpoint conversion and optional weight attachment use $`O(n\log n)`$ local queries in total. All fit the theorem's soft query count.

For gates, let $`C_{\rm loc}`$ and $`S_{\rm loc}`$ bound the costs of the supplied clean local query circuits. A per-rotation arithmetic/synthesis precision of $`p=O(\log[n(D_{\rm pol}+1)/\epsilon]+\log(b+2))`$ bits, with a sufficiently large constant, covers the elementary gates per block and the amplification sequence. The weight ratios are computed from the supplied $`b`$-bit data to the required additional working precision. Square roots and angles to additive operator error use polynomial-size reversible arithmetic in $`b,p,\log n`$. Near the endpoints one can compute the sine and cosine amplitudes to higher precision before computing the angle, avoiding a uniform derivative assumption there. All flags and degree/weight registers are included in the error accounting. Consequently the quantum gate bound is

```math
\widetilde O\!\left(
n\sqrt{\kappa/\gamma}\,[C_{\rm loc}+\mathrm{poly}(b,p,\log n)]
\right).
```

The non-oracle work is $`\widetilde O(n) + \mathrm{poly}(b,p,\log n)`$ bits or qubits, plus $`O(S_{\rm loc})`$ reused for the local oracle. Optional weight labels occupy an additional $`O(nb)`$ output bits. The classical phase-compilation cost for the polar and fixed-point sequences is kept explicit, as in the [regular resource account](resources.md). This theorem charges the given sorted access and its implementation. An unsorted table or a graph-dependent data structure for providing that access has its own cost.

At constant gap and bounded contrast the quantum circuit is near-linear for efficiently supplied local access and logarithmic weight precision. The [dense lower bounds](weight_contrast_lower_bound.md) prove the cost in weight contrast necessary on a fixed-gap family. They leave the optimal dependence on a shrinking gap open.
