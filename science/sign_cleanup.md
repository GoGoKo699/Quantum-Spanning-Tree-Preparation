# Removing the incidence signs coherently

The incidence-polar construction first produces a signed spanning-tree state. This chapter gives a reversible circuit that removes those signs in

```math
O\!\left(n\log ^4(n+2)\right)
\quad\text{elementary gates and}\quad
O\!\left(n\log ^3(n+2)\right)
\quad\text{scratch qubits}.
```

The circuit uses fixed wires, sorting networks and ordinary reversible arithmetic. It has no QRAM or data-dependent memory-access instruction. The bounds include computation and uncomputation; they do not optimize logarithms or constants.

## Input, orientation and the exact phase

Vertices are labelled $`0,\ldots,n-1`$, and the root is vertex $`0`$. Assume $`n\geq2`$; the one-vertex empty tree needs no sign correction. The input is a list of $`n-1`$ edges in the **actual final output order**. Each edge has a fixed orientation and a row of the incidence matrix $`B`$, with $`+1`$ at the tail and $`-1`$ at the head. For the usual endpoint label $`e=(u,v)`$, $`u<v`$, the orientation is $`u\to v`$. Write $`\bar B_T`$ for the incidence submatrix on these ordered tree edges with the root column deleted.

For an edge $`e`$, let $`c(e)`$ be its child endpoint when the tree is rooted at $`0`$, and put

```math
s_e=B_{e,c(e)}\in\{+1,-1\}.
```

The children, in input-edge order, are a permutation of $`1,\ldots,n-1`$. Let $`\sigma`$ sort that list into increasing order. Then

```math
\boxed{\det\bar B_T
=\mathrm{sgn}(\sigma)\prod_{e\in T}s_e.}
\tag{1}
```

To prove (1), multiply row $`e`$ by $`s_e`$, then reorder the rows by their child labels. The resulting matrix is $`I-K`$, where $`K_{v,w}=1`$ if $`w\neq0`$ is the parent of $`v`$. Every parent chain reaches the root, so $`K`$ is nilpotent and $`\det(I-K)=1`$. Row scaling and row permutation give (1). Thus the desired phase is the parity of the child-label sorting permutation, XOR the number of negative $`s_e`$.

The sign of a permutation is the parity of the transpositions actually performed by any sorting network. Recording and XORing each comparator's conditional-swap bit therefore gives $`\mathrm{sgn}(\sigma)`$, without evaluating a determinant.

## A fixed-network lookup primitive

We will repeatedly need all lookups $`F(q_i)`$ for a table with one record $`(j,F(j))`$ per key $`j`$. Several queries may have the same key. A reversible **batched join** implements these lookups as follows.

1. Make one data record $`(j,\mathrm{data},F(j))`$ for every table key, and one query record $`(q_i,\mathrm{query},i)`$ for every origin $`i`$.
2. Sort all records by $`(\mathrm{key},\mathrm{type})`$, with the data record before its queries.
3. Broadcast the data payload through its equal-key run by a fixed parallel-prefix circuit.
4. Sort by $`(\mathrm{type},\mathrm{origin})`$, so the query records form a fixed contiguous block in origin order. Copy their answers into fresh output registers.

All sorts retain their comparator bits. All copies and prefix histories are retained until reversal. The primitive is therefore a unitary compute operation, even though the logical table lookup is not itself injective.

Here is an explicit prefix broadcast. Initially a data record has `valid=1` and its payload; a query has `valid=0`. At prefix round $`a`$, record $`i`$ keeps its own valid payload if it already has one. Otherwise it takes the payload from the previous round's record $`i-2^a`$, provided that record is valid and has the same key. Values are written into fresh registers. After $`\lceil\log_2 N\rceil`$ rounds, every query has its data payload. Equal keys at the two endpoints of a sorted interval imply equal keys throughout that interval, which proves the propagation rule. The unique data record for a key is first in the run, so there is no ambiguity. In particular, this works when many query keys coincide; it does **not** require the query map to be a permutation.

A bitonic network on $`N=O(n)`$ records of $`O(\log n)`$ bits uses $`O(N\log^2N)`$ comparators, each costing $`O(\log n)`$ gates. A sort therefore costs $`O(n\log^3 n)`$ gates and retains $`O(n\log^2n)`$ comparator bits. The above prefix circuit uses $`O(n\log^2 n)`$ gates and history qubits. Consequently one complete join costs

```math
O(n\log^3 n)\text{ gates},\qquad
O(n\log^2 n)\text{ retained scratch}.
\tag{2}
```

Padding to the next power of two uses tagged dummy records with a sentinel key and does not change these bounds. The tags distinguish dummy records from every valid data/query record.

## Rooting a tree by an Euler tour

Expand the $`n-1`$ edges into $`L=2(n-1)`$ directed arcs. Give the two arcs of edge $`i`$ the fixed IDs $`2i`$ and $`2i+1`$, so reversal is simply XOR with $`1`$. Sort arcs by $`(\mathrm{tail},\mathrm{head},\mathrm{id})`$, thereby fixing a cyclic neighbor ordering at each vertex. If $`g=(v\to u)`$, let $`\mathrm{next}_v(g)`$ be the next outgoing arc in that cyclic order, wrapping at the last arc of a run.

For an arc $`h=(u\to v)`$, define

```math
P(h)=\mathrm{next}_v(\bar h),
\tag{3}
```

where $`\bar h`$ is its reversal. This Euler-tour permutation is one cycle on all $`L`$ arcs when the input is a tree. One proof removes a leaf: reinserting its two arcs inserts the leaf visit at one corner of the smaller tree's cycle, preserving a single cycle. The single-edge tree starts the induction.

The successor table in (3) is constructed without a variable-address read. In sorted outgoing-arc order, broadcast the first ID in each equal-tail run. The following record gives the cyclic successor except at the run's last record, which uses that broadcast first ID. For every outgoing record $`g`$, emit the pair

```math
(\bar g,\mathrm{next}_{\mathrm{tail}(g)}(g)).
```

Sorting these pairs by their first field restores the successor table to fixed arc-ID order. Reversal is a fixed bit operation, so every key occurs once.

Let $`a`$ be the root's first outgoing arc. Its predecessor is

```math
z=\overline{g_{\max}},
```

where $`g_{\max}`$ is the last outgoing arc in the root run. A boundary flag `tail=0` and `next-tail≠0` selects this unique record. A fixed XOR reduction of its flagged ID extracts $`g_{\max}`$. Such reductions copy computational-basis bit values coherently; they do not measure the tree. The root has at least one incident edge on every promised input.

Break the cycle at $`z`$: initialize

```math
\mathrm{succ}_0(h)=
\begin{cases}h,&h=z,\\P(h),&h\ne z,\end{cases}
\qquad
d_0(h)=\begin{cases}0,&h=z,\\1,&h\ne z.\end{cases}
```

Perform $`q=\lceil\log_2 L\rceil`$ simultaneous pointer-doubling rounds,

```math
\begin{aligned}
\mathrm{succ}_{j+1}(h)&=\mathrm{succ}_{j}(\mathrm{succ}_{j}(h)),\\
d_{j+1}(h)&=d_j(h)+d_j(\mathrm{succ}_{j}(h)).
\end{aligned}
\tag{4}
```

Use the batched join (2), keyed by $`\mathrm{succ}_j(h)`$, to obtain the right-hand-side values. The terminal becomes the target of many pointers; the repeated-key broadcast proof is why (4) remains valid after the first round. Fresh arrays preserve simultaneous-update semantics.

After round $`j`$, $`\mathrm{succ}_j(h)`$ advances by $`\min\{2^j,\ell(h)\}`$ positions along the broken cycle, and $`d_j(h)=\min\{2^j,\ell(h)\}`$, where $`\ell(h)`$ is the distance from $`h`$ to $`z`$. This invariant follows immediately by induction from (4). Hence $`d_q(h)=\ell(h)`$, and the chronological rank from $`a`$ is $`L-1-d_q(h)`$.

For the two arcs of any tree edge, the earlier one points from parent to child. Removing the edge separates a root-side component from a child-side component. A tour starting at the root cannot visit the child-side before first crossing from the root-side. Thus the child is the head of the arc with the **larger distance to $`z`$**. The two distances differ on a tree, so the comparison is unambiguous.

## Complete reversible phase circuit

```text
SIGN-PHASE(ordered edges e[0..n-2], endpoints and fixed orientations)
    Build both directed arcs, with IDs 2i and 2i+1.
    Sort outgoing arcs; compute cyclic-next IDs by equal-tail prefix broadcast.
    Build P(reverse(g)) = cyclic-next(g); sort back by arc ID.
    Extract z = reverse(last outgoing arc at root 0).
    Set succ[h] = z if h=z else P(h), and dist[h] = 0 if h=z else 1.
    Repeat ceil(log2(2(n-1))) times, writing fresh arrays:
        Join key succ[h] to table (h, succ[h], dist[h]).
        succ_new[h] = joined_successor[h].
        dist_new[h] = dist[h] + joined_distance[h].
    For each edge i, compare dist[2i] and dist[2i+1].
        child[i] = head of the arc with greater distance.
        neg[i] = 1 exactly when incidence(e[i], child[i]) = -1.
    Sort (child[i], i), XORing the conditional-swap bits into parity.
    phase_bit = parity XOR XOR_i neg[i].
    Apply a Z phase controlled by phase_bit.
    Reverse every computation, join, sort, copy and endpoint calculation.
```

On a promised tree, the phase is exactly $`\det\bar B_T`$ by (1). Every scratch register returns to its initial value. Applied to the signed determinant state, this multiplies each coefficient by the same sign and leaves the positive uniform tree state, up to its common global phase.

## Total unitary, error and label conventions

No gate is defined only on trees. Fixed sorting networks, comparisons, CNOT copies, and additions with retained operands are reversible on every bit string. Arc IDs are fixed literals, so successor keys remain in the fixed arc-ID domain even if the supplied endpoints describe a disconnected graph, repeated edges or a cycle. If the root run is missing, the fixed reduction returns the default ID $`0`$. Ties in child or endpoint comparisons use the fixed arc/edge ID as a secondary key. Arithmetic uses $`O(\log(n+2))`$-bit words and fixed modular addition; on promised trees there is no overflow. On other inputs the circuit imposes some deterministic phase and then uncomputes normally. Its meaning there is unrestricted, and it never assumes that malformed data can be erased.

This total-circuit convention also handles the small non-tree component caused by approximate polar transport. If $`\lVert\widetilde\psi-\psi_{\mathrm{tree}}\rVert\leq\delta`$, applying the same unitary sign circuit preserves that distance. There is no postselection on being a tree and no amplification of leakage.

Equation (1) must use the actual edge-row order presented to this circuit. An order change by a permutation $`\rho`$ changes the incidence minor by $`\mathrm{sgn}(\rho)`$. If labels are converted before inverse antisymmetrization, the resulting fermionic permutation is already represented in the determinant amplitude, and computing (1) in the new output order corrects it. If an already sorted list is relabelled and re-sorted without a fermionic sign, include the re-sorting parity explicitly. For lexicographically sorted adjacency lists, converting canonical port labels to canonical endpoint pairs preserves their order; nevertheless the endpoint conversion and any reverse-port search remain charged elsewhere in the algorithm.

If endpoints are already present, this circuit makes no graph queries. When its input stores canonical ports only, obtaining endpoints costs $`O(n)`$ rotation-map queries before the routine, followed by their inverse to erase the endpoint workspace. These costs are distinct from the gate bound for sign computation.

## Resource proof and verification boundary

There are $`O(\log n)`$ rounds of (4). Each round performs a constant number of fixed sorts and one prefix broadcast on $`O(n)`$ records, giving $`O(n\log^3 n)`$ gates and $`O(n\log^2 n)`$ retained history by (2). All rounds are kept for reversal, so the total scratch is $`O(n\log^3 n)`$. The Euler successor construction, root selection, child comparisons and final parity sort cost at most $`O(n\log^3 n)`$ additional gates and $`O(n\log^2 n)`$ scratch. Reversal doubles these costs. This proves the stated $`O(n\log^4(n+2))`$ gate and $`O(n\log^3(n+2))`$ workspace bounds for all $`n\geq2`$.

The fixed sorting-network method is inherited from the coherent sorting techniques used in [Berry et al., Section II and Appendix B](https://arxiv.org/abs/1711.10460). The tree-specific phase identity, Euler rooting construction and batched-join account above supply the sign-cleanup argument. A separate finite logical check enumerated every query array of length $`L`$ over $`L`$ keys for $`L=1,\ldots,5`$: all 3,413 arrays, including repeated keys, gave the correct prefix-broadcast answers. This checks the classical bit-value logic, not a compiled reversible gate circuit. Small-tree enumeration checks are also supporting examples; the all-$`n`$ claims follow from the proofs in this chapter.
