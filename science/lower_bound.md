# A linear lower bound for endpoint output

The near-linear dependence on the number of vertices is unavoidable, even for unweighted cubic graphs with a fixed positive spectral gap. The lower bound below concerns trees encoded by their **vertex endpoint pairs**, as in the preparation theorem. It does not assert optimal dependence on a vanishing gap.

## Theorem

There are absolute constants $\gamma_*>0$ and $c>0$, and an infinite family of even graph sizes $n$, with the following property. Suppose a quantum algorithm receives coherent rotation-map access to an unknown connected, simple, unweighted, cubic graph $G$ on $n$ publicly labelled vertices, promised to have normalized-Laplacian gap at least $\gamma_*$. The algorithm must prepare an output state whose tree register is within trace distance $\epsilon\leq 1/3$ of

$$
|\mathrm{UST}(G)\rangle
=\frac{1}{\sqrt{\tau(G)}}\sum_{T\text{ spanning tree of }G}|T\rangle,
$$

where $|T\rangle$ contains the lexicographically sorted list of the $n-1$ unordered endpoint pairs of $T$. Then its worst-case number of graph queries is at least $cn$ for all sufficiently large sizes in that family. The statement permits arbitrary known computation, ancillary registers, intermediate measurements, and adaptive control. It also holds for coherent sorted adjacency-list access at degree three.

The same conclusion applies when the preparation guarantee is a Euclidean error bound on the complete pure state: trace distance of the reduced tree register is at most that Euclidean error. The proof only uses the probability of obtaining a valid tree, so it applies more broadly to any output procedure whose measured endpoint list is a spanning tree with probability at least $2/3$ on every graph in the constructed family.

## 1. A constant-gap graph carrying linearly many hidden bits

Fix a publicly known simple cubic expander $X=(V_X,E_X)$ with $n_0$ vertices and $m_0=3n_0/2$ edges. Write its normalized-Laplacian gap as $\gamma_X\geq\gamma_0$, where $0<\gamma_0\leq1$ is an absolute constant independent of $n_0$.

Such graphs exist for arbitrarily large even $n_0$. For example, Friedman's theorem, in the uniform simple-graph formulation of Bordenave [1, Theorem 1], gives cubic graphs with adjacency eigenvalue

$$
\lambda_2(A_X)\leq 2\sqrt{2}+\eta
$$

for any fixed $\eta>0$ and all sufficiently large admissible sizes. Choosing $\eta=(3-2\sqrt2)/2$ permits $\gamma_0=(3-2\sqrt2)/6>0$. We only use existence: the chosen base graph and all its port tables are public, input-independent data in this query lower bound. No cost of constructing or reading an unknown expander is hidden in the reduction.

For every base edge $e=\{u,v\}$, make the following replacement.

1. Subdivide $e$ by a new midpoint $z_e$, giving $u-z_e-v$.
2. Take a disjoint copy of $K_4$ with vertices $a_e,b_e,c_e,d_e$ and subdivide its edge $\{a_e,b_e\}$ by a new vertex $p_e$.
3. Add the edge $\{z_e,p_e\}$.

Call the resulting graph $G_0$. The four original $K_4$ vertices retain degree three. The new midpoint $z_e$ and gadget port $p_e$ each have degree three after the attachment. Original base vertices also retain degree three. Thus $G_0$ is simple, connected, unweighted and cubic. Its size is

$$
n=n_0+6m_0=10n_0.
$$

Each attachment edge $\{z_e,p_e\}$ is a bridge: removing it disconnects exactly that five-vertex gadget from the rest of the graph. Consequently every spanning tree contains every attachment bridge.

There is one hidden bit $x_e$ for each base edge. For $x=(x_e)_{e\in E_X}\in\{0,1\}^{m_0}$, define $G_x$ by independently exchanging the public labels of $p_e$ and $a_e$ when $x_e=1$, and leaving them unchanged when $x_e=0$. The label sets of different gadgets are disjoint. This is a relabelling of one fixed abstract graph, so every $G_x$ has exactly the same spectrum. Its attachment bridge has labelled endpoint

$$
\{z_e,p_e\}\quad\text{if }x_e=0,
\qquad
\{z_e,a_e\}\quad\text{if }x_e=1.
$$

The number of hidden bits is

$$
N=m_0=\frac{3n}{20}.
$$

## 2. An explicit constant-gap bound

Here is a Poincare comparison that verifies the promised gap without appealing to a graph-replacement slogan.

Orient every base edge by a fixed public rule. Assign $z_e$ and its entire five-vertex gadget to the tail of $e$. For each base vertex $u$, let $F_u$ be $u$ together with all assigned new vertices. These sets partition $V(G_0)$; each is connected and has at most $19$ vertices. Every vertex of $F_u$ has a path to $u$ lying inside $F_u$ of length at most four.

For a real function $f$ on $V(G_0)$, put

$$
\mathcal E_G(f)=\sum_{\{v,w\}\in E(G_0)}(f(v)-f(w))^2,
\qquad
a=\frac1{n_0}\sum_{u\in V_X}f(u).
$$

Using $(r+s)^2\leq2r^2+2s^2$ gives

$$
\sum_{w\in V(G_0)}(f(w)-a)^2
\leq
2\sum_u\sum_{w\in F_u}(f(w)-f(u))^2
+2\sum_u|F_u|(f(u)-a)^2.
$$

Choose one of the length-at-most-four paths for each non-root vertex of each fiber. Cauchy--Schwarz bounds its squared endpoint difference by four times the energy along that path. At most eighteen such paths occur in a fiber, and different fibers have disjoint internal edges. Therefore

$$
2\sum_u\sum_{w\in F_u}(f(w)-f(u))^2
\leq144\mathcal E_G(f).
$$

The base graph's gap gives

$$
\sum_{u\in V_X}(f(u)-a)^2
\leq\frac1{3\gamma_0}
\sum_{\{u,v\}\in E_X}(f(u)-f(v))^2.
$$

Each base edge is represented by its own edge-disjoint path $u-z_e-v$ in $G_0$. A further Cauchy--Schwarz inequality bounds the sum on the right by $2\mathcal E_G(f)$. Since $|F_u|\leq19$,

$$
2\sum_u|F_u|(f(u)-a)^2
\leq\frac{76}{3\gamma_0}\mathcal E_G(f).
$$

If $\bar f$ denotes the mean on all vertices of $G_0$, minimizing over the centering constant yields

$$
\sum_w(f(w)-\bar f)^2
\leq
\left(144+\frac{76}{3\gamma_0}\right)\mathcal E_G(f).
$$

For a cubic graph, the normalized-Laplacian Rayleigh quotient is $\mathcal E_G(f)/(3\sum_w(f(w)-\bar f)^2)$. Hence

$$
\gamma(G_x)=\gamma(G_0)
\geq\frac1{432+76/\gamma_0}
\geq\frac{\gamma_0}{508}
=:\gamma_*>0.
$$

The constants are deliberately loose. Only their independence of $n$ and the hidden string matters.

## 3. Constant-query simulation of the graph oracles

Let the hidden bits be supplied by the usual coherent XOR oracle

$$
O_x|e,b\rangle=|e,b\mathbin\oplus x_e\rangle.
$$

Initially give every abstract vertex of $G_0$ a known three-entry port table. Let $R_0$ be its known rotation involution. Define $\sigma_x$ on vertices to exchange $p_e,a_e$ exactly when $x_e=1$, and let it preserve the port number. With these abstract port conventions, the unknown rotation is

$$
R_x=\sigma_x\circ R_0\circ\sigma_x^{-1}.
$$

One application of $\sigma_x$ uses a constant number of bit queries: compute the gadget index from the public label, load its bit, exchange the two labels conditionally, and uncompute that bit. The index is unchanged by the exchange. Non-gadget and other gadget labels are fixed; a known dummy-zero bit handles their coherent inactive branches. Because $R_0$ is public, this implements an in-place $R_x$ query using $O(1)$ calls to $O_x$, with clean work registers. The construction acts coherently on superpositions of ports and permits the same constant-factor simulation of controlled queries.

The in-place convention and the XOR-value convention for a rotation map are equivalent up to a factor of two. Given a value oracle, compute $R_x(h)$ into a blank register, swap the registers, and query again to erase the old $h$, using $R_x^2=I$. Given the in-place permutation, copy the basis label $h$ coherently into scratch, apply $R_x$ there, XOR its value into the target, and apply $R_x$ again to clean scratch. Invalid padded port labels can be assigned a known fixed action. Thus the lower bound does not depend on choosing one of these standard rotation-oracle conventions.

For **sorted adjacency-list access**, recompute the three neighbour labels and sort this constant-size list. An original base vertex's neighbour list is independent of $x$. The complete list at $z_e$ or within its gadget depends only on $x_e$. It therefore takes $O(1)$ bit queries to compute the requested sorted neighbour cleanly. A sorted-port rotation also determines the reverse port by inspecting the neighbour's three-entry list; at most a constant number of cell bits is involved. Conversely, at degree three one can obtain a reverse port from a neighbour oracle with only three neighbour queries. The bit-query simulation remains constant under either input convention. This argument uses no data-dependent memory table or QRAM.

## 4. A measured endpoint list reveals the whole hidden string

Every valid spanning tree of $G_x$ contains all its attachment bridges. For each public midpoint $z_e$, find the tree edge joining it to the public label set $\{a_e,b_e,c_e,d_e,p_e\}$. There is exactly one such graph edge, and it is necessarily present. Its gadget endpoint is $p_e$ if $x_e=0$ and $a_e$ if $x_e=1$. This recovers $x_e$ without querying $G_x$.

Thus a single valid tree determines **all** $N$ bits. The decoder is public computation. It may scan and sort the endpoint list by the structured public vertex labels; a near-linear classical implementation is available, although the query lower bound permits arbitrary decoder computation and does not rely on its running time.

If the algorithm's reduced tree state is within trace distance $\epsilon$ of the ideal q-sample, any measurement-event probability changes by at most $\epsilon$. The ideal state produces a valid spanning tree with probability one. Measuring the approximate output and applying this decoder consequently recovers the complete string with probability at least $1-\epsilon\geq2/3$ for every $x$.

Endpoint output is essential here. A bare abstract port identifier can conceal whether the bridge endpoint is labelled $p_e$ or $a_e$. The preparation theorem outputs endpoint pairs and charges their coherent conversion; this lower bound must not be transferred silently to a weaker port-only output task.

## 5. A self-contained oracle-interrogation bound

For completeness, the required linear lower bound for recovering all bits follows directly from the quantum-query polynomial method [2]. The sharper interrogation constants studied by van Dam [3] are unnecessary.

Consider a $T$-query algorithm for $O_x$, including arbitrary known computation and ancillary registers. Defer and purify all measurements. In the $\{+,-\}$ basis of the XOR target qubit, a bit query either leaves an amplitude unchanged or multiplies it by $(-1)^{x_e}$. Inducting over queries shows that its final pure state has the Fourier expansion

$$
|\psi_x\rangle=
\sum_{\substack{S\subseteq[N]\\|S|\leq T}}
\chi_S(x)|v_S\rangle,
\qquad
\chi_S(x)=(-1)^{\sum_{e\in S}x_e},
$$

where the coefficient vectors $|v_S\rangle$ are independent of $x$. Repeated indices cancel because $(-1)^{2x_e}=1$. Thus all $2^N$ final states lie in a common subspace $V$ of dimension at most

$$
D_T=\sum_{k=0}^{\min(T,N)}\binom Nk.
$$

Let $\{M_x:x\in\{0,1\}^N\}$ be the final POVM for guessing the entire string; a failure outcome may be added. For every $x$, $|\psi_x\rangle\langle\psi_x|\leq\Pi_V$. Under a uniform input string, the success probability is therefore at most

$$
2^{-N}\sum_x\operatorname{tr}
\bigl(M_x|\psi_x\rangle\langle\psi_x|\bigr)
\leq2^{-N}\operatorname{tr}\left(\Pi_V\sum_xM_x\right)
\leq\frac{D_T}{2^N}.
$$

For $T\leq N/3$, the binomial entropy bound gives

$$
D_T\leq2^{N H_2(1/3)},
\qquad H_2(1/3)<1,
$$

so the success probability tends to zero exponentially. An algorithm succeeding with probability at least $2/3$ on every string must consequently use $T=\Omega(N)$ bit queries. Classical randomness is covered by the purification, and a deterministic worst-case query budget permits inactive controlled-query slots after an early stopping branch.

If the spanning-tree algorithm used $q$ graph queries, the constant-query oracle simulation followed by the endpoint decoder would recover $x$ with $O(q)$ bit queries. Hence

$$
q=\Omega(N)=\Omega(n).
$$

This proves the theorem.

## Scope and attribution

The graph gadget and its Poincare comparison establish the lower bound for the endpoint-output task used here. The underlying expander existence theorem and oracle-interrogation method are inherited. The result matches the upper algorithm's $n$ dependence up to polylogarithms at fixed positive gap. It does not give a matching lower bound in $\gamma$, prove an improvement over classical sampling on expanders, or make a claim about weak encodings that omit endpoint labels.

1. Charles Bordenave, *A new proof of Friedman's second eigenvalue theorem and its extension to random lifts*, Annales scientifiques de l'Ecole Normale Superieure **53**, 1393--1439 (2020); [arXiv:1502.04482v4](https://arxiv.org/abs/1502.04482v4), Theorem 1. This proves the uniform simple-graph formulation of Joel Friedman's second-eigenvalue theorem; see also Friedman, *A Proof of Alon's Second Eigenvalue Conjecture and Related Problems*, Memoirs of the AMS **195**, no. 910 (2008), [arXiv:cs/0405020](https://arxiv.org/abs/cs/0405020).
2. Robert Beals, Harry Buhrman, Richard Cleve, Michele Mosca and Ronald de Wolf, *Quantum lower bounds by polynomials*, Journal of the ACM **48**, 778--797 (2001); [arXiv:quant-ph/9802049](https://arxiv.org/abs/quant-ph/9802049). The state-space Fourier argument is supplied above rather than relying on an unstated sharp constant.
3. Wim van Dam, *Quantum Oracle Interrogation: Getting All Information for Almost Half the Price*, FOCS 1998, pp. 362--367; [arXiv:quant-ph/9805006](https://arxiv.org/abs/quant-ph/9805006), [DOI:10.1109/SFCS.1998.743486](https://doi.org/10.1109/SFCS.1998.743486).
