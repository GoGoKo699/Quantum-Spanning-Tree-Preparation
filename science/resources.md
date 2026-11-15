# Complete resource accounting

The cost is measured from the supplied coherent graph interface to the positive, sorted endpoint-list q-sample. State preparation, permutation records, signs, endpoint conversion, inverses and precision are all included. This page does not charge an input oracle as a unit-cost physical device when its circuit is expensive.

## Parameters and precision

Use the parameters of the [model](model.md), and set $`r=n-1`$. Let

$$
D=O\!\left(\gamma^{-1/2}\log\frac{n}{\epsilon}\right)
$$

be the degree of the sign transformation used for each polar map. For example, allocate at most $`\epsilon/8`$ to each use of the universal key-resource state, at most $`\epsilon/(8r)`$ to each ideal polar isometry's full-state error, and at most $`\epsilon/4`$ in total to all compiled rotations. The first two allocations cost at most $`\epsilon/4+\epsilon/8`$; the remaining allowance covers the $`r`$ approximate uniform-subspace reflections and harmless rounding of these constants.

For a polar full-state error at most $`\epsilon/(8r)`$, choose its sign-polynomial error

$$
\delta\le\frac{\epsilon^2}{128r^2}.
$$

Indeed $`\sqrt{2\delta}\le\epsilon/(8r)`$. To prevent block-encoding error from accumulating across $`rD`$ uses, synthesize each constituent unitary to operator error $`O(\epsilon/(rD))`$, divided further by its number of elementary rotations. The resulting bit precision is

$$
p=O\!\left(\log\frac{n(D+1)}{\epsilon}\right)
$$

up to logarithms of the explicit local arithmetic circuit size. Exact reversible integer comparisons and additions introduce no numerical approximation. All-angle circuit bounds may alternatively be read in the arbitrary-rotation model; a fixed universal fault-tolerant gate set introduces these same logarithmic synthesis factors.

## Quantum operations

| Operation | Coherent graph calls | Ordinary gates and work |
|---|---:|---|
| Uniform vertex-subspace Householder | 0 | $`r\,\operatorname{poly}(\log(n/\epsilon))`$ gates; no graph table |
| Universal key resource, forward and backward | 0 | $`O(r\log^3(r+1)\log(1/\epsilon))`$ gates with bitonic networks, up to gate-synthesis factors |
| Initial and final particle sorting | 0 | $`O(r\log^3(n+1))`$ gates; $`O(r\log^2(r+1))`$ record bits |
| $`r`$ polar maps | $`O(rD)`$ rotation calls | $`O(rD(C_R+\operatorname{polylog}(n(D+1)/\epsilon)))`$ gates |
| Port folding | $`O(r)`$ rotation calls | $`O(r\operatorname{polylog}n)`$ gates |
| Clean endpoint conversion | $`O(r\log(d+1))`$ rotation calls, or sorted-list queries | $`O(r\operatorname{polylog}n)`$ gates |
| Rooted incidence sign | No graph calls once endpoints are present | $`O(n\log^4(n+1))`$ gates and $`O(n\log^3(n+1))`$ scratch, then uncomputed |

The endpoint conversion row is absorbed by the soft notation and does not introduce any degree power. If one prefers to retain canonical port labels as the output, it can be omitted; the theorem includes it to provide the conventional endpoint-list encoding.

The explicit query total, retaining the conversion logarithm, is

$$
O\!\left(n\gamma^{-1/2}\log\frac{n}{\epsilon}
+n\log(d+1)\right)
=O\!\left(n\gamma^{-1/2}\log\frac{n}{\epsilon}\right),
$$

because $`d<n`$, $`\gamma\le2`$, and $`\epsilon<1/10`$. Under sorted-list access, constructing every rotation call adds an $`O(\log(d+1))`$ factor. With an explicitly compiled rotation circuit, its entire cost $`C_R`$ is multiplied by the number of calls. The resulting quantum gate count is

$$
\widetilde O\!\left(n\gamma^{-1/2}(C_R+1)\right).
$$

The circuit uses $`O(n\log n)`$ payload qubits, universal key and sorting registers of soft-linear size, logarithmic-size one-particle work, and the $`O(n\log^3 n)`$ sign workspace. Retaining reversible sign intermediates therefore gives $`\widetilde O(n)`$ non-oracle qubits. If the supplied clean rotation circuit needs $`S_R`$ workspace qubits, peak total space is $`\widetilde O(n)+O(S_R)`$. Its workspace is reused serially across every oracle call and particle; it is not multiplied by the query count. Reversing the preparation has the same counts. A reflection implemented through preparation and inverse doubles the preparation cost and adds a multi-controlled phase on the all-zero state.

## Classical circuit compilation

The sorting networks, endpoint arithmetic, tree-sign circuit and universal key circuit have uniform descriptions generated from $`n,d`$ and precision; no graph-dependent preprocessing is used. Known prefix counts determine the uniform and Householder state-preparation rotations without a table of $`n`$ amplitudes.

The singular-value sign transformation requires a classical polynomial/phase compiler. Let $`C_{\mathrm{phase}}(D,p)`$ denote its actual cost, including its requested output accuracy. A standard polynomial-time QSVT phase compiler suffices for the quantum circuit theorem; the complete implementation cost includes this term rather than assuming it vanishes. The same compiled phase list is reused on all $`r`$ particles. Storing that classical list costs $`O(Dp)`$ classical bits and loading a prescribed sequential phase is ordinary circuit control, not a quantum-addressed lookup.

For a fixed positive $`\gamma`$, $`D`$ and $`p`$ are polynomial in $`\log(n/\epsilon)`$. Polynomial-time phase compilation is then a polylogarithmic contribution. Including it, circuit-description generation, and the explicitly charged graph-circuit gates preserves the nearlinear bound in $`n`$ for this central expander regime. For a shrinking gap, a claim about total classical-plus-quantum wall-clock complexity must retain $`C_{\mathrm{phase}}(D,p)`$ or specify a verified faster compiler. The quantum gate and oracle-query bounds above do not require a nearlinear-time phase compiler.

## Scope of the improvement

At constant gap and with a rotation circuit of polylogarithmic gate and workspace cost, the complete preparation has soft-linear gate count and soft-linear space, including clean positive sign removal. For a dense graph this cost is sublinear in the number of edges. With a larger oracle, its explicit gate and workspace terms remain. The interface must make each graph query at its charged cost; a succinct circuit can do so, whereas scanning a classical edge table cannot be silently replaced by a free oracle.

Classical algorithms can already produce an ordinary random tree in nearlinear time on regular expanders. The preparation result supplies a pure positive q-sample and its inverse. It does not establish practical quantum advantage, a hardware crossover, a faster classical-output expander sampler, or optimal dependence on $`\gamma`$. Those distinctions are part of the theorem's resource interpretation, not postponed costs.
