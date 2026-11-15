# Worked example and operational meaning

## Four-cycle worked example

Take vertices $`0,1,2,3`$ and edges, in order,

```math
(01),(03),(12),(23).
```

Orient each edge from its smaller endpoint to its larger endpoint and put $`+1`$ at the tail, $`-1`$ at the head. Delete root column $`0`$, as in the general proof. The graph is regular of degree two, its normalized-Laplacian gap is one, and it has four spanning trees.

The reduced incidence determinants are:

| Sorted tree edge list | Reduced determinant | Signed amplitude, after one common global phase choice |
| --- | --- | --- |
| $`\{01,03,12\}`$ | $`+1`$ | $`+1/2`$ |
| $`\{01,03,23\}`$ | $`-1`$ | $`-1/2`$ |
| $`\{01,12,23\}`$ | $`-1`$ | $`-1/2`$ |
| $`\{03,12,23\}`$ | $`-1`$ | $`-1/2`$ |

For example, the first reduced matrix is

```math
\begin{pmatrix}
-1&0&0\\
0&0&-1\\
1&-1&0
\end{pmatrix},
```

whose determinant is $`+1`$. The polar transport and exterior power produce exactly these determinant amplitudes. The sign circuit flips the other three branches and leaves the first unchanged, yielding

```math
|\mathrm{UST}(C_4)\rangle
=\frac12\bigl(
|01,03,12\rangle+|01,03,23\rangle
+|01,12,23\rangle+|03,12,23\rangle
\bigr).
```

This is a coherent state on edge lists. Measuring it returns a uniformly random deleted edge of the cycle. Keeping it unmeasured permits interference with later tree-dependent operations. Every sorting, rooting and graph-access work register is cleaned in the ideal circuit; the approximate theorem bounds the complete output state.

## Reflections and tree-dependent operations

Let $`U_G`$ be the clean preparation circuit and let $`|\Omega_G\rangle=|\mathrm{UST}(G)\rangle|0_{\mathrm{work}}\rangle`$. If

```math
\|U_G|0\rangle-|\Omega_G\rangle\|\leq\eta,
```

then $`U_G(2|0\rangle\langle0|-I)U_G^\dagger`$ is an approximate reflection about $`|\Omega_G\rangle`$. Its operator-norm error is at most $`2\eta`$: the difference of the two rank-one projectors has norm equal to the sine of their angle, which is at most their Euclidean state distance. The reflection costs one preparation, one inverse and the all-zero phase test. The [resource account](resources.md) includes these operations.

A coherent circuit evaluating a property of the endpoint list can therefore be combined with this reflection in amplitude amplification. That property circuit, its workspace, the marked probability and the accumulated preparation error must also be charged. No particular rare-tree search, tree-counting speedup or practical application advantage follows merely from having the preparation primitive.

## What the gap buys

The gap enters through a one-particle singular value, $`\sigma_{\min}\geq\sqrt{\gamma/2}`$. Polar transport consequently costs soft $`O(\gamma^{-1/2})`$ calls per particle. The method does not explore a classical walk's exponentially many possible histories or store a table of its spanning trees. Its state dimension is large because an edge list has many possible values, while the circuit acts on only soft $`O(n)`$ qubits.

For fixed positive gap and a polylogarithmic-cost graph circuit, the resulting quantum gate and query bounds are near-linear in the number of vertices. Generic dense-graph qsampling upper bounds have a larger preprocessing cost. This is a comparison under a structural graph promise; it does not refute their general weighted-graph lower bounds. Complete graphs also have special-purpose encodings, so they should not be used to claim that the present circuit beats every earlier algorithm on every dense instance.

Ordinary classical spanning-tree sampling on constant-gap regular graphs is already near-linear, for example through random-walk cover-time bounds. The coherent state and its reusable inverse are the capability studied here. A table supplied as raw classical input still needs a paid reversible access implementation; succinct graph access and arbitrary free data loading are different assumptions.

## Boundaries

The theorem concerns unweighted regular connected graphs, a known gap lower bound, controlled reversible sorted graph access, finite accuracy, and endpoint-encoded positive tree states. Sorted neighbour indices, or an additional paid inverse-index interface, make clean endpoint conversion possible. It includes finite-error cleanup and an endpoint-output lower bound at constant gap. General weighted or irregular graphs, optimal gap dependence, geometric locality, error-correction overhead and hardware crossover are outside the proved account. The classical phase compiler's cost is reported separately for general gap parameters.
