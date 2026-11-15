# Model and main capability

The task is to prepare a coherent uniform superposition of all spanning trees of an implicitly supplied graph. A classical random tree is obtained by measuring this state, but preparing the pure superposition also supplies a reversible setup circuit. The result below concerns that stronger output.

## Graph, access and output

Let $`G=(V,E)`$ be a connected, simple, unweighted, $`d`$-regular undirected graph, with $`V=\{0,\ldots,n-1\}`$ and $`n\ge 2`$. Write $`P`$ for the simple random-walk matrix and promise a known lower bound

```math
\lambda_2(I-P)\ge \gamma>0.
```

This is the normalized-Laplacian gap. Bipartite graphs are allowed: no lower bound on the absolute random-walk gap is needed. The graph has $`m=nd/2`$ edges.

A port is a pair $`h=(v,k)`$ with $`0\le k\lt d`$, with the ports at each vertex indexed in increasing neighbor order. This ordering is needed for the clean conventional endpoint output; the polar construction itself also works with arbitrary port labels if those labels are retained as the output encoding. The coherent rotation map $`R`$ takes a port to the other port of the same edge:

```math
R(v,k)=(w,\ell),\qquad R^2=I.
```

The map has no fixed points on valid ports. On padded invalid labels, extend it by the identity. This makes the oracle a total unitary. Its compiled reversible-circuit gate cost is denoted by $`C_R`$ and its clean workspace requirement by $`S_R`$. The supplied implementation returns this workspace to zero on every call. Both resources are charged below; the same workspace is reused serially.

An equivalent sufficient interface is coherent access to lexicographically sorted adjacency lists. The oracle returns the $`k`$th neighbor of $`v`$. Given $`(v,k)`$, one query obtains $`w`$ and reversible binary search in $`w`$'s sorted list obtains the reverse index $`\ell`$ using $`O(\log(d+1))`$ queries. Computing the map in an ancillary register, swapping input and output, and computing it again implements the in-place involution cleanly. Thus each rotation call costs $`O(\log(d+1))`$ sorted-list queries and polynomially many logarithmic-size gates. Sorted lists are an input promise, not a preprocessing step performed for free.

The input interface is an explicitly charged circuit or oracle; it supplies neither a stored graph table nor QRAM built by the algorithm. If the graph is available only as an unstructured classical table, coherent access to that table is an additional implementation problem and is not free under this theorem.

Encode an edge by its endpoint pair $`(u,v)`$ with $`u\lt v`$, and a tree by its lexicographically sorted list of $`r=n-1`$ endpoint pairs. With $`\tau(G)`$ the number of spanning trees, the target is

```math
|\mathrm{UST}(G)\rangle
=\frac{1}{\sqrt{\tau(G)}}\sum_{T\text{ spanning tree of }G}|T\rangle.
```

All amplitudes are positive in this encoding. The target is stronger than a signed Slater state or a mixed distribution over trees with an unerased random seed.

## Main theorem

**Theorem.** For every graph and gap promise above, and every $`0\lt \epsilon\lt 1/10`$, there is a reversible preparation circuit $`\mathcal U_{G,\epsilon}`$ such that, up to an irrelevant global phase,

```math
\left\Vert \mathcal U_{G,\epsilon}|0\rangle
-|\mathrm{UST}(G)\rangle|0\rangle_{\mathrm{work}}\right\Vert \le\epsilon.
```

It uses

```math
O\!\left(n\gamma^{-1/2}\log\frac{n}{\epsilon}\right)
```

rotation-map calls, $`\widetilde O(n\gamma^{-1/2}(C_R+1))`$ quantum gates, and $`\widetilde O(n)+O(S_R)`$ total qubits. The algorithm's non-oracle workspace is soft-linear; potentially large workspace of the supplied oracle is not included in that adjective. Here the soft notation hides logarithmic factors in $`n`$, $`1/\epsilon`$, and the precision used to synthesize the one-particle circuit. Classical phase compilation is accounted for separately in [resources](resources.md); for fixed positive $`\gamma`$, its cost is polynomial in logarithms and does not change the nearlinear end-to-end bound. Under sorted adjacency-list access the displayed query count acquires an additional $`O(\log(d+1))`$ factor.

The norm convention implies trace distance at most $`\epsilon`$ for the output, and hence total variation distance at most $`\epsilon`$ after measuring the tree register. The work register is approximately returned to zero in the same joint-state guarantee. In particular, the circuit and its inverse are available for subsequent coherent use; no graph-dependent record is discarded.

The construction is proved in [polar transport](polar_transport.md), [coherent preparation](coherent_preparation.md), and [sign cleanup](sign_cleanup.md). The complete bound, including bit precision and ordinary gates, is collected in [resources](resources.md).

## What changes under the gap promise

For a family with a fixed positive normalized gap, a positive spanning-tree q-sample is prepared with nearlinear cost in the number of vertices, without graph-dependent preprocessing. The graph can be dense: the cost does not contain an extra factor of $`\sqrt d`$ or $`d`$ beyond the cost of its supplied oracle.

This is not a claim of a classical-output speedup on regular expanders. Classical random-walk tree samplers already have nearlinear bounds on such graphs. The contribution is the clean coherent state and the explicit circuit route to it. The theorem does not cover arbitrary weighted graphs, irregular graphs with unpaid degree-state preparation, or an unknown gap certified for free. It claims no matching lower bound for its full gap dependence.

## Inherited ingredients

The method uses established singular-value transformation and polar-decomposition algorithms, the Slater-determinant/DPP correspondence, the matrix-tree theorem, and sorting-network antisymmetrization. The algorithmic addition studied here is their implicit graph realization together with positive sign removal and a clean, fully charged preparation circuit. See [related work](../references/related_work.md) for the direct comparison, including the general weighted q-sampler of Hamoudi, Tanasa and Sridhara.
