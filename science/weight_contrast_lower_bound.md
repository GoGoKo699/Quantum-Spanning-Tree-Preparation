# Weight contrast costs queries even at fixed gap

In a dense graph, a spanning tree uses only a small fraction of the available edges. A hidden increase in one edge weight can nevertheless give that edge a large chance of appearing in the tree. The family below makes this effect occur independently in many rows while keeping both normalized Laplacian gaps bounded below.

## Theorem

Fix integers $`8\le q\le N`$. There is a family with $`n=2N`$ vertices and $`\Theta(n^2)`$ edges, with public topology and edge weights in $`\{1,q\}`$. The supplied weight-contrast bound is $`\kappa=q`$. Both the weighted and unweighted normalized Laplacian gaps are at least $`1/14`$ throughout the family.

For $`0\lt\epsilon\le1/10`$, a quantum algorithm producing a tree register within trace distance $`\epsilon`$ of the positive endpoint-list q-sample needs $`\Omega(N\sqrt q)`$ weight queries in the worst case. A classical randomized algorithm drawing one endpoint-list sample within total variation distance $`\epsilon`$ of the target law needs $`\Omega(Nq)`$ expected weight queries, already on the all-unit instance. These claims use the sorted local interface of the [weighted construction](weighted_preparation.md). Giving the topology, edge locations and unweighted degrees for free leaves both conclusions valid.

At fixed gap, the quantum bound matches the weighted preparation theorem up to logarithms. Reading all $`Nq`$ unknown weights suffices for a classical sample in the query model. The two bounds give a quadratic query separation in weight contrast on this family, up to the logarithms in the quantum upper bound. Ordinary circuit costs and classical computation remain separate resources.

## A dense family with fixed gaps

Start with a unit-weight clique of $`N`$ core vertices. Designate a public set $`A`$ of $`q`$ core vertices as attachment sites. Add $`N`$ row vertices, each with an edge to every site in $`A`$ and no edges to the other rows. The input is $`x=(x_1,\ldots,x_N)\in\{0,1,\ldots,q\}^N`$. In row $`i`$, all edge weights are one if $`x_i=0`$. If $`x_i=a>0`$, give the edge to site $`a`$ weight $`q`$. Sorted adjacency locations and reverse-port indices are independent of $`x`$.

Write $`x_i'`$ for the value of a real test function on row $`i`$ and $`y_j`$ for its value at core vertex $`j`$. Let $`h`$ be the mean of $`y_j`$ over the core and $`a_0`$ its mean on $`A`$. Define the cross and core energies by

```math
E_{\mathrm{cross}}=\sum_{i=1}^N\sum_{j\in A}w_{ij}(x_i'-y_j)^2,
\qquad
E_{\mathrm{core}}=\sum_{1\le j\lt k\le N}(y_j-y_k)^2
=N\sum_{j=1}^N(y_j-h)^2.
```

Row $`i`$ has weighted degree $`d_i\le2q-1`$. Jensen's inequality gives

```math
q(x_i'-a_0)^2\le\sum_{j\in A}(x_i'-y_j)^2,
\qquad
q(a_0-h)^2\le\sum_{j=1}^N(y_j-h)^2.
```

Using both estimates and $`(r+s)^2\le2r^2+2s^2`$ bounds the whole row contribution by

```math
V_{\mathrm{row}}=\sum_{i=1}^N d_i(x_i'-h)^2
\le4E_{\mathrm{cross}}+4E_{\mathrm{core}}.
```

The contribution to the core's degree-weighted variance from cross edges is at most $`2E_{\mathrm{cross}}+2V_{\mathrm{row}}`$, by applying $`(y_j-h)^2\le2(y_j-x_i')^2+2(x_i'-h)^2`$ on each cross edge. The clique degrees contribute at most $`E_{\mathrm{core}}`$. For all vertices $`v`$, with weighted degrees $`d_v`$ and test function $`f_v`$, this yields

```math
\min_{c\in\mathbb{R}}\sum_v d_v(f_v-c)^2
\le \sum_v d_v(f_v-h)^2
\le 14E_{\mathrm{cross}}+13E_{\mathrm{core}}.
```

The numerator of the normalized Laplacian Rayleigh quotient is $`E_{\mathrm{cross}}+E_{\mathrm{core}}`$. The variational characterization of the first positive normalized eigenvalue gives a gap of at least $`1/14`$. Applying the same proof with all weights set to one gives the unweighted gap bound.

## One edge event distinguishes adjacent inputs

For an edge $`e=\{u,v\}`$, its inclusion probability under the weighted tree law is $`w_e R_{\mathrm{eff}}(u,v)`$. To see this, differentiate the logarithm of the weighted tree partition function with respect to $`w_e`$. The spanning-tree sum gives the inclusion probability divided by $`w_e`$. The matrix-tree determinant gives $`b_e^{\mathrm{T}}L_{\mathrm{red}}^{-1}b_e`$, where $`L_{\mathrm{red}}`$ is the Laplacian with one root removed and $`b_e`$ is the incidence vector with that coordinate dropped. The latter expression is the effective resistance from solving for the grounded voltage of a unit current from $`u`$ to $`v`$.

Compare two inputs that agree except that row $`i`$ is unmarked in one input and boosts the edge $`e`$ to site $`j`$ in the other. In the unmarked input, $`w_e=1`$. Dropping all clique edges and reducing all boosted edges to one can only increase resistance, by the minimum-energy characterization over unit flows. The resulting component is a unit $`K_{N,q}`$. Its resistance across the parts is $`(N+q-1)/(Nq)`$: the current vector splits into mean-zero vectors on the two parts with Laplacian eigenvalues $`q`$ and $`N`$, and a part-constant mean-zero vector with eigenvalue $`N+q`$. Their squared norms are $`1-1/N`$, $`1-1/q`$, and $`1/N+1/q`$, respectively. Thus the unmarked inclusion probability is at most $`2/q`$.

In the marked input, any unit flow between the two endpoints sends net current one across the cut of row $`i`$. The sum of squared edge currents divided by their conductances is at least $`1/(2q-1)`$ on that cut, by Cauchy–Schwarz. The effective resistance is at least that large, so the marked inclusion probability is at least $`q/(2q-1)`$.

The separation is greater than $`1/4`$ for $`q\ge8`$. Approximation shifts each probability by at most $`\epsilon`$, leaving a separation of at least $`1/20`$ at the stated error. The test reads only whether the public endpoint pair occurs in the output.

## Quantum queries

On one row, let $`S`$ be the adjacency matrix of the star on labels $`0,1,\ldots,q`$, with center $`0`$. On all input strings, use the real symmetric matrix

```math
\Gamma=\sum_{i=1}^N I^{\otimes(i-1)}\otimes S\otimes I^{\otimes(N-i)}.
```

Its nonzero entries compare exactly the adjacent pairs from the edge test. The star has operator norm $`\sqrt q`$ and a nonnegative unit eigenvector for eigenvalue $`\sqrt q`$. Tensoring that vector gives a nonnegative unit vector $`\delta`$ with eigenvalue $`N\sqrt q`$ for $`\Gamma`$. The triangle inequality shows this is the operator norm.

For each query address $`z`$, let $`\Delta_z(x,x')=1`$ when the two oracle replies differ and $`0`$ otherwise. A mutable address identifies one cross edge of row $`i`$ and site $`a`$. In $`\Gamma\circ\Delta_z`$, all summands except the one at $`i`$ vanish. In that summand only the star link $`0\leftrightarrow a`$ remains. Hence $`\Vert\Gamma\circ\Delta_z\Vert=1`$. Two port addresses for the same edge induce the same mask. Degree queries, invalid addresses and public clique edges have zero masks. This argument covers either weight-only XOR queries or combined sorted-neighbor and weight replies, since the extra reply bits are known and independent of $`x`$.

Defer measurements and purify the algorithm's randomness. At each step let $`|\psi_x\rangle`$ be the full state when the input is $`x`$, set $`|\Psi\rangle=\sum_x\delta_x|x\rangle|\psi_x\rangle`$, and use the progress quantity

```math
W=\langle\Psi|(\Gamma\otimes I)|\Psi\rangle.
```

The initial value is $`N\sqrt q`$. The final output event separates the reduced states of adjacent inputs by trace distance at least $`1/20`$. Trace distance cannot increase under discarding registers. Since the full states are pure, the magnitude of each adjacent-pair overlap is at most $`\sqrt{1-(1/20)^2}`$. Nonnegativity of the entries of $`\Gamma`$ and $`\delta`$ gives a final progress value at most $`\sqrt{1-(1/20)^2}\,N\sqrt q`$.

An input-independent unitary leaves $`W`$ fixed. For a query, pass to the binary Fourier basis for the XOR reply register. For each address and reply Fourier label, the query acts on the input index by a diagonal sign matrix $`F`$. On a given address the reply has at most two possible values, so $`\Gamma-F\Gamma F`$ is either zero or $`2(\Gamma\circ\Delta_z)`$. All address and reply-label blocks have operator norm at most two. The change in $`W`$ per query is therefore at most two. This holds also for controlled inactive query slots, which have zero change. The required progress decrease proves $`\Omega(N\sqrt q)`$ queries.

## Classical queries

Let $`x^{(0)}`$ be the all-unit input, and let $`x^{(e)}`$ boost just one cross edge $`e`$. Couple the executions of a classical randomized sampler by using the same random coins. Until the first query to $`e`$, the two transcripts coincide. An execution that never queries $`e`$ has identical output under the coupling, including when the sampler decides to stop based on its transcript. Accordingly, the total variation distance between the two output laws is at most the probability of querying $`e`$ on $`x^{(0)}`$.

The edge-event estimate gives total variation distance at least $`1/20`$ for every choice of $`e`$. Summing those first-hit probabilities over all $`Nq`$ cross edges shows that the expected number of distinct edges queried on $`x^{(0)}`$ is at least $`Nq/20`$. Counting repeated queries can only increase the cost. Conversely, one can read the $`Nq`$ cross weights and then sample using the explicit weighted graph. This last statement counts queries and leaves the classical sampling computation to a separate resource estimate.

## Scope and attribution

The family isolates the cost of bounded weight contrast at a fixed graph gap. The vanishing-gap dependence remains open. The separate [cubic lower bound](lower_bound.md) proves the linear vertex requirement for the unweighted regular endpoint-output problem. The [related-work comparison](../references/related_work.md#hamoudi-tanasa-sridhara-2026) credits the independent-row search from general weighted tree sampling. The construction here uses positive integer weights and a dense core to enforce constant gaps, and proves pairwise output separation from a single marginal. The progress argument uses the quantum adversary method. [Ambainis, 2000](https://arxiv.org/abs/quant-ph/0002066)
