# From polar transport to a positive tree superposition

The polar map supplies orthonormal edge orbitals. Filling all $`n-1`$ vertex modes orthogonal to the uniform vector produces their Slater determinant. Two further tasks must be handled coherently: compressing particle permutations into a sorted edge list, and removing the graph-dependent determinant sign. This page proves the first task, the tree amplitudes, and the complete error composition. The sign circuit is given in [sign cleanup](sign_cleanup.md).

## A known basis of the correct vertex subspace

The vertex register is padded to a power of two. A generic state-preparation unitary whose first column is the uniform valid-range state would not be sufficient: its other columns might leave the valid $`n`$-dimensional space. Use instead the explicit Householder reflection

$$
H_s=I-2|v_s\rangle\langle v_s|,
\qquad
|v_s\rangle=\frac{|0\rangle-|s\rangle}{\sqrt{2-2/\sqrt n}}.
$$

It maps $`|0\rangle`$ to $`|s\rangle`$, and preserves the valid vertex space because $`v_s`$ is supported there. Thus

$$
Q=\bigl[H_s|1\rangle\ \cdots\ H_s|n-1\rangle\bigr]
$$

has orthonormal columns spanning $`s^\perp`$. This works for arbitrary $`n\ge2`$.

The state $`v_s`$ has one amplitude at zero and a second, equal amplitude at every nonzero valid label. Its squared mass at zero is $`(1-1/\sqrt n)/2`$, and the remaining mass $`(1+1/\sqrt n)/2`$ is uniform over $`1,\ldots,n-1`$, with negative amplitude. It is prepared without a table by binary-prefix rotations. At a prefix, its probability weight is the distinct zero-label weight, if that label is present, plus the common nonzero-label weight times the number of valid nonzero completions. The conditional probability for the next bit is the ratio of these explicit weights.

There are only two exceptional prefixes at any depth: the prefix containing zero and the prefix straddling the upper boundary $`n`$. Every other reachable prefix contains a full interval of equally weighted nonzero labels, so its next bit uses a Hadamard. Apply that base Hadamard and correct it by a known controlled rotation at each exceptional prefix. The exceptional prefix strings and their rotation angles are determined classically from $`n`$; there are only $`O(\log n)`$ of them, rather than $`n`$ stored amplitudes. Equality to a known prefix is tested with $`O(\log n)`$ elementary reversible gates. A final phase is negative on nonzero labels. This gives $`O(\log^2 n)`$ reversible gates and $`O(\log n)`$ prescribed rotations before synthesis, with logarithmic work returned to zero. The same construction, omitting the zero label's exceptional weight, prepares a uniform known range such as the coin state.

Each prescribed rotation is synthesized to a sufficient fraction of $`\eta`$, so the state-preparation error is at most $`\eta`$. This construction is polynomial in $`\log n`$ and $`\log(1/\eta)`$ and uses no quantum-addressed data table. On prefixes with zero ideal probability, choose any fixed continuation; that choice supplies a total unitary extension.

If $`U_v`$ prepares this state, then $`U_v(I-2|0\rangle\langle0|)U_v^\dagger`$ implements $`H_s`$. A preparation error at most $`\eta`$ gives an operator-norm reflection error at most $`4\eta`$, by the difference of the two rank-one projectors. The ideal reflection is used in the proof; the compiled approximation is included in the final hybrid bound.

## A universal clean permutation resource

Put $`r=n-1`$. Fix one sorting-network topology on the records, for example a bitonic network after padding the record count to the next power of two. Padding records have distinct fixed priority tags that sort above every logical record, in the same fixed order in the key, vertex and edge versions. Only the $`r`$ logical records are permuted. Use a common padded word width and the same comparator layout for all versions; the padding words return to their known values. Each comparator records whether it swapped its two entries. Use a deterministic tie convention. Let $`C`$ be the number of comparators.

For any strictly increasing tuple $`x=(x_1,\ldots,x_r)`$ and any permutation $`\pi`$, reversible sorting gives

$$
S|\pi x\rangle|0^C\rangle
=|x\rangle|\rho(\pi)\rangle.
$$

The record $`\rho(\pi)`$ depends only on the relative ranks of the entries, not their numerical values or their bit width. Distinct permutations have distinct records because the sort is reversible. The parity of the actual comparator transpositions is the parity of $`\pi`$.

Define $`T`$ by applying the sort and then the phase $`(-1)^{\text{number of recorded swaps}}`$. With

$$
\operatorname{Alt}|x\rangle
=\frac1{\sqrt{r!}}\sum_{\pi\in S_r}\operatorname{sgn}(\pi)|\pi x\rangle,
\qquad
|\mathcal R\rangle=\frac1{\sqrt{r!}}\sum_{\pi\in S_r}|\rho(\pi)\rangle,
$$

the two signs cancel, giving the exact identity

$$
T\operatorname{Alt}|x\rangle|0^C\rangle
=|x\rangle|\mathcal R\rangle. \tag{1}
$$

It holds by linearity for every superposition of distinct sorted tuples. In particular, the record on the right is independent of the set encoded by $`x`$. This is the sorting-network antisymmetrization mechanism of [Berry and collaborators](https://doi.org/10.1038/s41534-018-0071-5), with its universal work state kept explicit.

Here is an efficient, entirely coherent preparation of the needed resource. Choose a power of two $`M\ge2r^2`$, prepare $`r`$ independent uniform $`M`$-ary keys, and sort them reversibly with the same network, without the parity phase. The probability of distinct keys is

$$
p=\frac{M(M-1)\cdots(M-r+1)}{M^r}\ge1-\frac{r(r-1)}{2M}\ge\frac34.
$$

Conditioned on distinct keys, the sorted keys and comparator record factor exactly:

$$
|\mathcal F\rangle|\mathcal R\rangle,
\qquad
|\mathcal F\rangle
=\binom Mr^{-1/2}\sum_{0\le a_1<\cdots<a_r<M}|a_1,\ldots,a_r\rangle.
$$

Every sorted set of keys has exactly one original input ordering for each permutation, all with equal positive amplitude. This proves the factorization, rather than assuming that an unobserved seed can be erased.

The distinctness projector is implemented by checking adjacent sorted keys for equality. Reflections about the initial all-zero state and this good subspace give coherent fixed-point amplitude amplification. Since $`p\ge3/4`$, a unitary $`K_\eta`$ using $`O(\log(1/\eta))`$ calls to the key-preparation circuit and its inverse satisfies

$$
\|K_\eta|0\rangle-|\mathcal F\rangle|\mathcal R\rangle\|\le\eta. \tag{2}
$$

Ancillas used to compute the predicate are uncomputed. Equation (2) permits a harmless global good-sector phase to be absorbed into the mathematical definition of $`K_\eta`$; its physical value cancels when the same circuit's inverse is applied below, so it need not be learned. This is a coherent fixed-point construction, not a measured retry loop; its inverse is available. The fixed-point primitive is inherited from [Yoder, Low and Chuang](https://arxiv.org/abs/1409.3305). Its only data here are the known particle count and key range, and it never queries the graph.

The special case $`r=1`$ has no comparator record and no collisions; it is included by taking the sorting circuit to be the identity.

## Preparation and cleanup circuit

Initialize the sorted particle tuple $`(1,\ldots,r)`$ in vertex registers. Prepare $`\mathcal F,\mathcal R`$ with $`K_\eta`$. Applying $`T_{\mathrm{vertex}}^\dagger`$ to this known tuple and the record register uses (1) to give

$$
\operatorname{Alt}|1,\ldots,r\rangle\otimes|\mathcal F\rangle\otimes|0^C\rangle
$$

in the ideal resource limit. Apply $`H_s`$ to every particle, then the polar transport and canonical endpoint conversion from [the one-particle construction](polar_transport.md) to every particle. Every orbital begins in $`s^\perp`$, so polar transport is isometric on all occupied modes.

The result is a Slater state in the edge orbitals $`W_EQ`$. Apply $`T_{\mathrm{edge}}`$ to sort the particle edge labels. Its topology is identical to that of $`T_{\mathrm{vertex}}`$ and the key sort; different logical payload widths are embedded in the common padded word width specified above. Equation (1) returns the same record $`\mathcal R`$, so the full state factors as

$$
\sum_{S:\,|S|=r}\det((W_EQ)_S)|S\rangle
\otimes|\mathcal F\rangle|\mathcal R\rangle.
$$

Apply $`K_\eta^\dagger`$ to the key and record registers. In the ideal resource limit this returns all of them to zero. Only the graph-dependent determinant amplitudes remain in the sorted edge register. There is no measurement or discarded graph-dependent garbage at any stage.

## Why the nonzero amplitudes are exactly tree amplitudes

Let $`L=B^\dagger B`$, and put $`M_Q=Q^\dagger LQ`$. The folded polar map satisfies

$$
W_EQ=BQ M_Q^{-1/2}.
$$

The columns on the right are orthonormal. Expanding their Slater determinant and grouping the $`r!`$ permutations of each sorted subset gives the amplitude $`\det((W_EQ)_S)`$ shown above. There is no additional factorial in the sorted-subset amplitude: the normalized antisymmetric basis already contains $`1/\sqrt{r!}`$.

If $`S`$ is not a spanning tree, its $`n-1`$ incidence rows are rank deficient, so its minor vanishes. For a spanning tree $`T`$, let $`\overline B_T`$ be its square incidence matrix after deleting vertex column zero. Then $`\det\overline B_T\in\{+1,-1\}`$.

Set $`\Omega=[s\ Q]`$, a unitary $`n\times n`$ matrix. The matrix with first row $`s^\dagger`$ and remaining rows $`B_T`$ obeys

$$
\begin{bmatrix}s^\dagger\\ B_T\end{bmatrix}\Omega
=\begin{bmatrix}1&0\\0&B_TQ\end{bmatrix}.
$$

The signed maximal cofactors of $`B_T`$ form its right-kernel vector. Its kernel is the constant vector, hence all these signed cofactors equal $`\det\overline B_T`$. Expanding the first row of the matrix on the left therefore gives $`\sqrt n\det\overline B_T`$. Taking determinants yields

$$
\det(B_TQ)=\det(\Omega)\sqrt n\det\overline B_T.
$$

The matrix-tree theorem gives $`\det M_Q=n\tau(G)`$, equivalently the product of the nonzero Laplacian eigenvalues is $`n\tau(G)`$. Consequently

$$
\det((W_EQ)_T)
=\det(\Omega)\frac{\det\overline B_T}{\sqrt{\tau(G)}}. \tag{3}
$$

The phase $`\det(\Omega)`$ is independent of $`T`$ and of the graph. The only remaining relative sign is the rooted incidence determinant. The [sign circuit](sign_cleanup.md) computes that sign in soft-linear ordinary gates, applies its phase, and uncomputes its workspace. Equation (3) then gives the positive target state, up to the fixed global phase.

## Joint error, clean work and inversion

The resource circuit (2) is used once forward and once backward. For the ideal main circuit, its preparation error contributes at most $`\eta`$ by unitary invariance. Conversely,

$$
\|K_\eta^\dagger|\mathcal F,\mathcal R\rangle-|0\rangle\|
=\||\mathcal F,\mathcal R\rangle-K_\eta|0\rangle\|\le\eta.
$$

Thus the entire universal-resource contribution is at most $`2\eta`$. No assumption about the errors' record distribution is needed.

For the particle operations, compare the actual circuit with the ideal circuit one particle at a time. Each ideal input is in the occupied $`s^\perp`$ space with clean work, even though the particles are entangled by antisymmetry. The full isometry bound in [polar transport](polar_transport.md) holds with a reference, so a one-particle error at most $`\zeta`$ gives total error at most $`r\zeta`$. The same hybrid argument applies to the approximate $`H_s`$ reflections and compiled oracle-independent rotations. Choose the resource error and synthesis tolerances so that $`2\eta+r\zeta`$ and all remaining synthesis errors sum to at most $`\epsilon`$; one concrete allocation is given in [resources](resources.md).

Sorting and sign computation are total reversible circuits. Their arbitrary action on malformed labels does not enlarge the distance from the exact tree-supported state. All ideal work registers return to zero; the resulting joint-state norm bound proves the theorem's simultaneous output and workspace statement.

The physical preparation circuit is a fixed product of unitary gates. Reversing it gives $`\mathcal U_{G,\epsilon}^\dagger`$ with the same cost. In particular $`\mathcal U_{G,\epsilon}(I-2|0\rangle\langle0|)\mathcal U_{G,\epsilon}^\dagger`$ is an exact reflection about the state the compiled circuit actually prepares, and approximates the corresponding ideal setup reflection with operator error at most $`2\epsilon`$ up to the choice of projector convention. Subsequent algorithms must choose a tighter setup error when they call this reflection repeatedly.
