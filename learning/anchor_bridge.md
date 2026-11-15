# From quantum-algorithm foundations to a clean tree state

Selected anchor: Andrew M. Childs, Lecture Notes on Quantum Algorithms (17 April 2025).

The [author's source page](https://www.cs.umd.edu/~amchilds/qa/) identifies the notes. This bridge explains the project through one four-vertex graph before locating the background in that source. The [milestone map](milestones.md) gives the complete conceptual route; the [science index](../science/README.md) gives direct access to the proofs.

## A four-cycle from input to clean output

Imagine four junctions, labelled $`0,1,2,3`$, connected by four links. The sorted edge list is

$$
(01),(03),(12),(23).
$$

Here $`01`$ means the unordered endpoint pair $`\{0,1\}`$, written with its smaller endpoint first. The links form a cycle. Removing any one link leaves all four junctions connected and creates no cycle, so there are exactly four spanning trees.

### 1. Specify the output before the algorithm

A tree register stores three endpoint pairs in sorted order. Different lists are different computational-basis states, denoted by kets such as $`|01,03,12\rangle`$. The desired state is

$$
|\operatorname{UST}(C_4)\rangle
=\frac12\left(
|01,03,12\rangle+
|01,03,23\rangle+
|01,12,23\rangle+
|03,12,23\rangle
\right).
$$

A quantum amplitude determines a measurement probability through its squared magnitude. Every amplitude here is $`1/2`$, so each tree is observed with probability $`1/4`$.

Relative signs matter before measurement. A state with amplitudes $`+1/2,-1/2,-1/2,-1/2`$ has the same four measurement probabilities, but later interference can distinguish it from the desired positive state. The construction first reaches that signed state and then removes its relative signs.

The target also includes a work register in state $`|0\rangle`$. For example, a reversible random sampler might instead produce a superposition of seed-and-tree pairs. Distinct seeds can remain correlated with the same tree; ignoring the seed need not leave a pure tree state. This algorithm must undo its records, not merely leave them unmeasured.

### 2. Supply the graph through a paid reversible interface

Every vertex of the cycle has two neighbors, so its degree is $`d=2`$. A port $`(v,k)`$ identifies vertex $`v`$ and one of its two incident links. The ports at each vertex follow increasing neighbor order. The sorted neighbor lists are:

| Vertex | Port 0 neighbor | Port 1 neighbor |
| --- | --- | --- |
| 0 | 1 | 3 |
| 1 | 0 | 2 |
| 2 | 1 | 3 |
| 3 | 0 | 2 |

The rotation map $`R`$ takes a port to the other port of the same edge. For example, $`R(0,1)=(3,0)`$ and applying $`R`$ again returns $`(0,1)`$. Its action is reversible and can be applied to a superposition of ports.

The theorem charges the implementation of this map. A sorted adjacency-list oracle can construct the reverse index by binary search. If ports arrive in arbitrary order, the polar part can keep canonical port labels as its output; clean conversion to endpoint pairs needs an additional paid inverse-index locator. The endpoint theorem does not assume such a locator is free.

For a larger graph, a succinct reversible graph circuit may be inexpensive. A raw table of all edges is a different input and still needs a paid coherent-access implementation. The four-cycle makes the access rule visible, not costless.

### 3. Turn a vertex mode into an oriented edge mode

A vertex state is a list of amplitudes, one for each vertex. Uniform-port loading $`V`$ replaces each vertex label by an equal superposition of its incident ports. Applying $`(I-R)/2`$ then takes the difference between the two ends of an edge. The resulting map is

$$
A=\frac{I-R}{2}V.
$$

The subtraction makes edge orientation visible. If a vertex mode has the same amplitude at both ends of every edge, its differences vanish. In a connected graph the only such mode is the uniform vector

$$
|s\rangle=\frac12\left(|0\rangle+|1\rangle+|2\rangle+|3\rangle\right)
$$

for this example.

Let $`P`$ be the simple random-walk matrix: its entry $`P_{uv}`$ is $`1/d`$ when $`u`$ and $`v`$ are adjacent, and zero otherwise. The exact identity

$$
A^\dagger A=\frac{I-P}{2}
$$

connects the edge-difference map to the graph spectrum. The dagger denotes the adjoint: here $`A^\dagger`$ maps edge modes back to vertex modes. An adjoint is an inverse for a unitary map; the present map $`A`$ is not unitary. The identity tells us how much $`A`$ stretches or shrinks each vertex direction.

For the cycle, $`I-P`$ has eigenvalues $`0,1,1,2`$. Its normalized-Laplacian gap is therefore $`\gamma=1`$, the smallest positive eigenvalue. The nonzero singular values of $`A`$, which are its stretching factors, are $`1/\sqrt2,1/\sqrt2,1`$. The zero singular value belongs to $`s`$.

The project needs the gap of $`I-P`$, not a gap in the absolute values of the random-walk eigenvalues. Thus the cycle's eigenvalue $`-1`$ for $`P`$ is allowed.

### 4. Preserve directions while equalizing their lengths

The polar isometry $`W`$ keeps the input-to-output directions of $`A`$ and replaces every nonzero singular value by one. On $`s^\perp`$, the space orthogonal to the uniform vector, it therefore preserves lengths and inner products. The zero mode is excluded from the occupied input space.

QSVT, quantum singular-value transformation, implements this operation through a bounded polynomial that approximates the sign function away from zero. Its query cost depends on the inverse of the smallest nonzero singular value. Since that value is at least $`\sqrt{\gamma/2}`$, one particle costs order $`\gamma^{-1/2}`$, with logarithmic accuracy factors.

This is an inherited algorithmic primitive. The graph-specific work is constructing its projected-unitary access at the right normalization and making sure every occupied input mode lies in the supported subspace. [Polar transport](../science/polar_transport.md) provides that construction and its full-state error bound, including leakage outside the signal block.

### 5. Fill the entire uniform-complement subspace

There are $`n-1=3`$ independent vertex directions orthogonal to $`s`$. Choose an orthonormal basis of that subspace and place one particle in each basis direction. The general compiler constructs the basis with a graph-independent Householder reflection, a reflection mapping one known basis vector to $`s`$ while preserving the valid vertex space. It does not compute the graph's eigenvectors.

The particles are encoded in three separate label registers. Antisymmetrization gives a minus sign whenever two particle registers are exchanged. For three distinct labels $`x_1<x_2<x_3`$, the normalized antisymmetric state contains all six orderings with their permutation signs and a common magnitude $`1/\sqrt6`$. This is the first-quantized representation of a Slater determinant.

Applying the same one-particle isometry $`W`$ to all three registers transports their occupied subspace into the edge space. Antisymmetry makes the amplitude of a sorted edge subset a determinant of its three occupied edge orbitals. This determinant rule is established fermionic linear algebra; it is the connection used by the compiler.

There are four three-edge subsets in the cycle, and every one is a tree. In a general graph, a non-tree subset of $`n-1`$ edges has rank-deficient incidence rows and its determinant amplitude vanishes. The matrix-tree identity normalizes the remaining tree amplitudes to equal magnitude.

### 6. Remove the particle-order records cleanly

Sorting the particle labels collects all permutations of one edge set into its sorted list. A reversible sorting network must record each conditional swap, or the operation would lose information and fail to be unitary.

The crucial fact is that the swap-record superposition depends only on the particle count and the fixed sorting network, not on which distinct labels were sorted. The compiler prepares this universal record resource before querying the graph. After edge transport and final sorting, the same resource factors from the tree state, so its inverse preparation returns it to zero.

This statement requires the records to factor as a quantum state. Merely finding the same distribution of records would not prove that they can be uncomputed. The [coherent-preparation proof](../science/coherent_preparation.md) writes the factorization explicitly and uses a coherent fixed-point circuit to prepare the resource. No graph-dependent sorting record is discarded.

### 7. Correct the determinant signs

Orient each cycle edge from its smaller endpoint to its larger endpoint. Its incidence row has $`+1`$ at the tail, $`-1`$ at the head, and zero elsewhere. Delete the column of root vertex $`0`$.

For the first tree, with edges $`01,03,12`$ in that order, the reduced incidence matrix is

$$
\overline B_T=
\begin{pmatrix}
-1&0&0\\
0&0&-1\\
1&-1&0
\end{pmatrix},
\qquad
\det\overline B_T=+1.
$$

After one common global phase choice, the polar/exterior-power construction gives:

| Sorted tree | Rooted incidence determinant | Signed amplitude | Positive target amplitude |
| --- | --- | --- | --- |
| $`01,03,12`$ | $`+1`$ | $`+1/2`$ | $`+1/2`$ |
| $`01,03,23`$ | $`-1`$ | $`-1/2`$ | $`+1/2`$ |
| $`01,12,23`$ | $`-1`$ | $`-1/2`$ | $`+1/2`$ |
| $`03,12,23`$ | $`-1`$ | $`-1/2`$ | $`+1/2`$ |

The circuit computes each tree's determinant sign, applies that sign as a phase, then reverses the computation. Since the square of either $`+1`$ or $`-1`$ is $`+1`$, every amplitude becomes positive.

It computes a sign without evaluating a large determinant. Root the tree at zero. For each edge, identify its child endpoint, the endpoint farther from the root. The sign is the product of the incidence entries at these children, multiplied by the parity of the permutation that sorts the child labels.

For $`T=\{01,03,12\}`$, the child labels in edge order are $`(1,3,2)`$. The three incidence entries are all $`-1`$, with product $`-1`$. Sorting the children requires an odd permutation, whose sign is also $`-1`$. Their product is $`+1`$, agreeing with the matrix above.

For general trees, fixed sorting networks and Euler-tour pointer doubling compute the children and permutation parity in nearlinear gates up to logarithms. The computation and its inverse clean the entire sign workspace. The [sign-cleanup chapter](../science/sign_cleanup.md) proves the phase formula and the reversible implementation.

### 8. Keep the output and cost in the same statement

The example ends with the four positive amplitudes and clean work registers. Measuring returns one uniformly random tree. Keeping the state coherent also keeps the possibility of reversing its preparation or constructing a reflection from the preparation and its inverse.

For general $`n`$ and requested joint-state error $`\epsilon`$, the rotation-call bound is

$$
O\!\left(n\gamma^{-1/2}\log\frac n\epsilon\right).
$$

The factor $`n`$ counts the occupied particle registers. The inverse square root of the gap comes from the one-particle polar transform. The logarithm pays for sufficiently accurate transforms so that their combined error remains at most $`\epsilon`$.

The [resource statement](../science/resources.md) also charges:

| Quantity | Meaning |
| --- | --- |
| $`C_R`$ | Gate cost of one clean graph rotation |
| $`S_R`$ | Workspace required by that supplied circuit, reused between calls |
| $`C_{\mathrm{phase}}`$ | Classical cost of compiling the QSVT phases |
| Sorting and sign work | Ordinary reversible gates and retained scratch, later uncomputed |
| Endpoint conversion | Neighbor lookup and inverse index location under the stated access promise |

The quantum gate count is $`\widetilde O(n\gamma^{-1/2}(C_R+1))`$ and peak space is $`\widetilde O(n)+O(S_R)`$. For fixed positive gap, polynomial-time phase compilation adds only polylogarithmic cost. For a shrinking gap, its actual $`C_{\mathrm{phase}}`$ must remain in a total implementation-time claim.

The four-cycle is a worked example, not an advantage benchmark. Ordinary classical tree sampling is already nearlinear on constant-gap regular graphs. The established capability is a clean positive coherent state under the stated graph access and gap promises. The [endpoint lower bound](../science/lower_bound.md) matches the vertex dependence up to logarithms at fixed gap; optimal dependence on a shrinking gap is not proved.

## How the anchor connects to this project

Read the selected parts when the corresponding object appears in the example. Reading the entire source is not a prerequisite.

| Childs section | Foundation used here | Project-specific continuation |
| --- | --- | --- |
| §1.4, reversible computation | Preserve information in a circuit and later uncompute it | Clean graph lookup, sorting records and sign workspace |
| §2.1, subadditivity of errors | Bound a circuit's error by its component errors | Joint output/work guarantee across all particles |
| Chapter 18, discrete-time walks | Graph states, local shifts and the connection to Markov spectra | The incidence identity $`A^\dagger A=(I-P)/2`$ |
| §28.3, linear combinations of unitaries | Implement sums through coherent control | Construct the projected difference $`(I-R)V/2`$ |
| §§29.1–29.3, block encoding, QSP and qubitization | Encode an operator and transform its spectrum polynomially | Rectangular singular-vector polar transport with gap-dependent cost |

The notation is translated in the [model](../science/model.md): $`n`$ counts vertices, $`d`$ is graph degree, $`\gamma`$ is the normalized-Laplacian gap, and $`\epsilon`$ is the complete output-state tolerance. The letter $`A`$ denotes a rectangular vertex-to-port map, not a quantum adjacency matrix.

The source's block-encoding language is extended to two different projected input and output spaces. That rectangular step uses the primary QSVT/polar research results cited in [related work](../references/related_work.md). The source is an entry point, not a claim that its Hermitian examples alone prove the graph transform.

## Steps supplied by the project

Four bridges are essential to the result and are developed locally:

1. **Graph incidence to polar transport.** The projected graph circuit has unit normalization, a known kernel, and nonzero singular gap at least $`\sqrt{\gamma/2}`$.
2. **One-particle maps to tree amplitudes.** Filling $`s^\perp`$, antisymmetrizing and applying the map on each register gives determinant amplitudes; the matrix-tree identity identifies and normalizes the trees.
3. **A reusable universal permutation resource.** Coherent resource preparation, factorization and its inverse clean all permutation records.
4. **Signed trees to positive endpoint trees.** Rooting, sign computation, sorted-access endpoint conversion and their inverses implement the required positive-amplitude encoding.

These are proof dependencies, not four extra textbook assignments. The research literature is credited where its primitives enter, and the [30 milestones](milestones.md) join the foundations and local derivations into one complete account.

[Learning index](README.md) · [Scientific statement](../science/model.md) · [Verification](../verification/README.md)

