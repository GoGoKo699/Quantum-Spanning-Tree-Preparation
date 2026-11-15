# Incidence polar transport

The one-particle circuit transports a known vertex subspace into the graph's cut space. Its normalization is important: the cost depends on the normalized-Laplacian gap, without a degree penalty hidden in the block encoding.

## An explicit projected-unitary encoding

Let $`\mathcal H_A`$ be the port space. Prepare the uniform coin state by a known range-preparation unitary $`U_d`$, and define the isometry

$$
V|v\rangle=\frac{1}{\sqrt d}\sum_{k=0}^{d-1}|v,k\rangle.
$$

The coin preparation contains no graph data. Let $`R`$ be the port involution from the [model](model.md), and set

$$
A=\frac{(I-R)V}{2}.
$$

This is a projected block of an actual unitary. With a control qubit $`c`$, put

$$
U=(H_c\otimes I)\bigl(|0\rangle\langle0|_c\otimes I
+|1\rangle\langle1|_c\otimes R\bigr)
(H_c\otimes I)(I_c\otimes I_v\otimes U_d).
$$

Project the input onto $`c=0`$ and coin zero, and the output onto $`c=1`$. Under the natural identifications of these input and output spaces, the projected map is $`A`$. Both projectors have explicit graph-independent reflections. The unitary uses a constant number of rotation calls; controlled classical-function queries can also be implemented by compute, controlled copy and uncompute with constant-factor overhead.

Because $`R=R^\dagger`$ and $`R^2=I`$,

$$
A^\dagger A
=\frac14 V^\dagger(I-R)^2V
=\frac12(I-V^\dagger RV)
=\frac{I-P}{2}.
$$

The last equality follows entrywise: $`V^\dagger RV`$ has entry $`1/d`$ precisely for adjacent vertices. In particular $`\Vert A\Vert \le1`$. Connectivity makes its kernel exactly the uniform vector

$$
|s\rangle=\frac1{\sqrt n}\sum_{v=0}^{n-1}|v\rangle.
$$

Every nonzero singular value of $`A`$ lies in $`[\sqrt{\gamma/2},1]`$. An eigenvalue $`-1`$ of $`P`$, possible for a bipartite graph, merely gives singular value one and causes no difficulty.

## The polar isometry and its full-state error

On $`s^\perp`$, define

$$
W=A(A^\dagger A)^{-1/2}.
$$

It is an isometry into the antisymmetric port subspace. Singular-vector transformation implements this polar factor; the underlying primitive is inherited from [Gilyén, Su, Low and Wiebe](https://arxiv.org/abs/1806.01838) and the polar-decomposition formulation of [Quek and Rebentrost](https://arxiv.org/abs/2106.07634).

For completeness, the error used here concerns the full unitary dilation, rather than only its projected block. Choose a real odd bounded polynomial $`p`$ such that

$$
1-\delta\le p(x)\le1
\quad\text{for}\quad x\in[\sqrt{\gamma/2},1].
$$

The standard sign approximation has degree

$$
D=O\!\left(\gamma^{-1/2}\log\frac1\delta\right).
$$

The real-polynomial QSVT construction produces a unitary $`U_p`$ whose relevant block is $`p^{\mathrm{SV}}(A)`$. We include its constant-size branch ancilla and designated input/output projection: averaging the two conjugate phase sequences implements the real polynomial without an extra normalization factor, as in Corollary 18 of [Gilyén, Su, Low and Wiebe](https://arxiv.org/abs/1806.01838). Write a unit input in $`s^\perp`$ as $`|\psi\rangle=\sum_j c_j|v_j\rangle`$, using right singular vectors, and $`W|v_j\rangle=|u_j\rangle`$. Embed the ideal output in the output projector with all designated ancillary values. Its overlap with the full actual output is

$$
\langle W\psi|U_p|\psi\rangle
=\sum_j |c_j|^2p(\sigma_j)\ge1-\delta.
$$

Both vectors have norm one, so

$$
\Vert U_p|\psi\rangle-|W\psi\rangle\Vert ^2\le2\delta.
$$

This proves a uniform isometry error of $`\sqrt{2\delta}`$, including every failure component outside the projected output. It also holds with an arbitrary reference system. The ideal output control $`c=1`$ and any real-polynomial branch state $`|+\rangle`$ are known fixed states; apply $`X`$ and $`H`$, respectively, to return them to zero. Other designated constant ancillary states are treated in the same way. These constant-cost operations preserve the error bound and permit serial reuse of the one-particle workspace. Setting $`\delta=\Theta((\epsilon/n)^2)`$ gives one-particle error $`O(\epsilon/n)`$ while retaining $`D=O(\gamma^{-1/2}\log(n/\epsilon))`$. Approximate gate synthesis is added by an operator-norm hybrid bound in [resources](resources.md).

## Folding ports into undirected edges

For an edge with ports $`h`$ and $`Rh`$, choose the canonical port $`e=\min(h,Rh)`$ in lexicographic order. Computing the partner port, comparing the two, and conditionally swapping gives the reversible map

$$
|h\rangle\longmapsto |e\rangle|b(h)\rangle,
\qquad b(h)=\mathbf1[h>Rh].
$$

To clean the temporary larger-port register, recompute $`R(e)`$ and XOR it away, then reverse the temporary computation. The map is a unitary extension of the displayed bijection on valid labels and costs a constant number of rotation calls. Consequently

$$
\frac{|e\rangle-|Re\rangle}{\sqrt2}
\longmapsto |e\rangle|{-}\rangle.
$$

The orientation qubit has the same state for every edge and is returned to zero by a known one-qubit circuit. No ranking of all graph edges is performed.

Orient each edge from its smaller endpoint to its larger endpoint, and let $`B`$ be the $`m\times n`$ incidence matrix with $`+1`$ at the tail and $`-1`$ at the head. Folding $`A`$ gives $`B/\sqrt{2d}`$: each port difference contributes a factor of $`\sqrt2`$, and canonical port order agrees with endpoint order on a simple graph. With $`L=B^\dagger B=d(I-P)`$, the folded polar isometry is therefore

$$
W_E=B(L|_{s^\perp})^{-1/2}.
$$

The factors $`\sqrt{2d}`$ cancel. This is the reason no extra $`\sqrt d`$ appears in the query count.

## Endpoint encoding without graph-dependent garbage

A canonical port is $`(u,k)`$ with neighbor $`v>u`$. Compute $`v`$, then recover $`k`$ by reversible binary search for $`v`$ in $`u`$'s sorted adjacency list. XOR that recovered index into the old index register and uncompute the search. The result is precisely the endpoint pair $`(u,v)`$, with every port-index temporary zero. This takes $`O(\log(d+1))`$ sorted-list queries, or a soft-logarithmic number of rotation calls by evaluating the neighbor through $`R`$.

For fixed $`u`$, sorted adjacency indices have the same order as neighbors, so this conversion preserves the lexicographic edge order. Conversion is performed coherently before the final sorting and sign circuit. On padded or malformed labels define fixed default values and retain/reverse all temporary arithmetic; the circuit remains a total unitary. Its action on such labels cannot amplify the norm of the existing approximation error.
