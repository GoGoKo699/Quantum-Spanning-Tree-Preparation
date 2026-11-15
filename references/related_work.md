# Related work and attribution

The result concerns **clean coherent preparation** of a positive uniform spanning-tree state for a connected, unweighted, regular graph with a supplied normalized-Laplacian gap lower bound. Its endpoint-output theorem assumes a coherent rotation map whose ports are indexed in increasing neighbor order, or coherent sorted adjacency-list access. The circuit implementing that access is charged. The determinant description of spanning trees, fermionic antisymmetry, quantum polar decomposition and QSVT are established ingredients.

The contribution is an end-to-end compiler joining those ingredients: it constructs the normalized incidence polar map from the graph oracle, transports a known antisymmetric state, removes the rooted-incidence determinant signs, and cleans its workspace. Its stated cost is $`\widetilde O(n/\sqrt{\gamma})`$ graph-rotation calls and $`\widetilde O((C_R+1)n/\sqrt{\gamma})`$ gates when one implemented rotation costs $`C_R`$ gates. It introduces no graph table or QRAM preprocessing. Classical phase-compilation cost is retained separately in the [resource account](../science/resources.md); at fixed positive gap it is polylogarithmic. This is a promised-graph algorithm, not a general weighted-graph improvement.

## Direct comparisons

Here $`n`$ is the number of vertices, $`m`$ the number of edges, $`r`$ a matrix rank, and $`\gamma`$ the normalized-Laplacian gap. Tildes hide logarithmic factors; approximation and failure parameters must be restored when using a bound.

| Source and task | Access and established resource | Relationship to this result |
| --- | --- | --- |
| [Hamoudi–Tanasa–Sridhara, 2026](#hamoudi-tanasa-sridhara-2026): positive spanning-tree q-samples | Connected weighted graphs with $`m\ge100n`$ and sorted adjacency-list access. Their current Theorem 3.1 gives preprocessing $`\widetilde O(\sqrt{mn/\rho})`$, subsequent q-sampling $`\widetilde O(\sqrt{mn\rho})`$, and reflection $`\widetilde O(\sqrt{m\rho})`$, for $`\rho\in[n/m,1]`$. Their implementation discussion uses QRAM and gives a loose quadratic time bound. | Positive tree q-sampling is already known. Here regularity and a gap promise permit a different, direct polar compiler with no preprocessing. For one sample, the cited general bound is $`\widetilde O(\sqrt{mn})`$; this result gives $`\widetilde O(n/\sqrt{\gamma})`$. Their amortized reflection advantage is not claimed here. |
| [Kerenidis–Prakash, 2022](#kerenidis-prakash-2022): determinant/subspace states | For an explicit $`M\times r`$ matrix, Theorem 5.5 uses $`O(Mr^2)`$ classical orthogonalization and $`O(Mr\log M)`$ gates per sample. A supplied embedding with a short Givens decomposition is a favorable special case. | The exterior-power state and determinant amplitudes are inherited. Here the orthonormal image is produced implicitly from local graph access; its dense matrix and Givens decomposition are not computed. |
| [Fanuel–Bardenet, 2025](#fanuel-bardenet-2025): bypassing orthogonalization in a projection-DPP sampler | Column normalization costs $`O(Mr)`$. The resulting circuit is combined with rejection or amplitude amplification governed by the column-normalized Gram determinant $`a`$. Its graph example includes uniform spanning trees. | Orthogonalization-free DPP sampling is already known. Here the polar transform pays an inverse singular-gap factor instead of a potentially very small determinant acceptance. |
| [Quek–Rebentrost, 2022](#quek-rebentrost-2022), building on [Gilyén–Su–Low–Wiebe, 2019](#gilyen-su-low-wiebe-2019): polar isometry | Projected-unitary/block-encoding access and a nonzero singular-value lower bound $`\delta`$ give a polar transform with $`O(\delta^{-1}\log(1/\varepsilon))`$ queries. The full output isometry error must include signal-block leakage. | This supplies the one-particle transform. The graph construction identifies $`\delta\ge\sqrt{\gamma/2}`$ and places every occupied input mode in its supported row space. No new polar-decomposition primitive is claimed. |
| [Berry et al., 2018](#berry-et-al-2018): first-quantized antisymmetrization | Section II antisymmetrizes sorted, distinct tuples coherently using sorting networks, with nearlinear size up to logarithms in particle count and label range. | This supplies the permutation machinery. The present account must additionally retain a fixed universal resource and implement its inverse so that graph-dependent records are cleaned. |
| [Apers–Gao–Ji–Liu, 2025](#apers-gao-ji-liu-2025): random spanning-tree samples | General weighted graphs; $`\widetilde O(\sqrt{mn})`$ quantum queries and time, producing a classical tree. | This is a different output contract. Measuring our state yields a classical sample, but the claimed capability is the clean coherent state before measurement. |

## What the gap promise changes

For a $`d`$-regular graph, $`m=nd/2`$. At a constant normalized gap, the direct preparation cost is nearlinear in the size of the tree output. In the dense regime covered by the cited theorem, relative to its general one-sample q-sampling bound, the available upper bounds differ by a factor of order $`\sqrt d`$, up to logarithms. This comparison includes the earlier algorithm's preprocessing; it is not a lower bound against every algorithm specialized to expanders.

The mechanism is a singular-gap statement. With explicit uniform-port loading $`V`$ and the involutive port reversal $`R`$ from the stated interface, the projected map

```math
A=\frac{I-R}{2}V
```

obeys

```math
A^\dagger A=\frac{I-P}{2}.
```

Its known kernel is the uniform vertex vector. Polar transport on the orthogonal complement therefore avoids both a dense classical orthogonalization and multiplication of unorthogonalized columns with determinant-dependent postselection. Exterior powers and the matrix-tree identity turn its minors into equal-magnitude tree amplitudes. The rooted-tree sign computation is needed to obtain positive amplitudes rather than merely the correct measurement distribution.

## Classical samples and coherent samples

Classical spanning-tree sampling is a mature subject; [Wilson's loop-erased-walk algorithm](#wilson-1996) is a standard example. On regular constant-gap graphs, cover-time methods already give nearlinear expected costs up to logarithms. The result establishes no asymptotic advantage for producing a classical sample in that regime.

A reversible classical sampler generally retains its random seed. Erasing that seed is an additional requirement for a pure positive q-sample. This distinction is explicit in Hamoudi–Tanasa–Sridhara's introduction and motivates their coherent output contract. Here the compiler cleans its permutation resources, orientation information and sign-computation workspace.

The earlier general weighted q-sampling lower bound uses hidden edge weights and a weighted hub construction. It does not establish a lower bound for the unweighted regular constant-gap class. Conversely, this algorithm does not contradict that weighted worst-case bound.

The [endpoint-output lower bound](../science/lower_bound.md) supplies a separate $`\Omega(n)`$ query bound on a cubic, constant-gap family. It encodes independent bits in mandatory bridge endpoints and reduces any valid endpoint-tree output to oracle interrogation. The query method is inherited from Beals et al. and van Dam; constant-gap base expanders are supplied by Bordenave's formulation of Friedman's theorem. This matches the upper bound's vertex dependence up to logarithms at fixed gap, without establishing the optimal gap dependence.

## Scope of the comparison

The graph-to-polar identity, determinant normalization and sign compiler form the specific algorithmic account developed here. The comparisons above do not establish exhaustive priority or optimal dependence on $`\gamma`$. They also do not extend the theorem to arbitrary weighted, irregular, directed or disconnected graphs. Any such extension requires its own access construction, null-space preparation, amplitude/sign proof and complete resource accounting.

The port-order assumption also matters. The polar construction can retain canonical port labels under an arbitrarily ordered rotation map. Converting them cleanly to conventional endpoint pairs requires an inverse index locator. Sorted neighbor order supplies that locator by reversible binary search; an arbitrary-port interface must supply and charge it separately. The endpoint theorem does not give this inverse lookup for free.

The primary-source check covered the direct tree qsampler, explicit-matrix DPP/subspace samplers, polar-QSVT algorithms and first-quantized antisymmetrization. No earlier end-to-end theorem with the same sorted-access, regular-gap promise and clean positive endpoint-tree output was identified in that check.

## Sources

### Hamoudi-Tanasa-Sridhara 2026

Yassine Hamoudi, Adrian Tanasa and Shrinidhi Teganahally Sridhara, *Quantum Sampling of Random Spanning Trees via Amortized Data Structures*, [arXiv:2609.40314](https://arxiv.org/abs/2609.40314). The comparison uses the [author-hosted revision dated 6 November 2026](https://shrinidhits.bitbucket.io/files/publications/spanning-trees.pdf), especially Section 2.1, Theorem 3.1, Section 3.5 and the weighted lower-bound construction. Its formal theorem is used rather than reconstructing a tradeoff from the abstract. BibTeX key: `HamoudiTanasaSridhara2026`.

### Kerenidis-Prakash 2022

Iordanis Kerenidis and Anupam Prakash, *Quantum machine learning with subspace states*, [arXiv:2202.00054v2](https://arxiv.org/abs/2202.00054v2), especially Definition 1.1, the Givens-circuit preparation discussion, Lemma 5.4 and Theorem 5.5. BibTeX key: `KerenidisPrakash2022`.

### Fanuel-Bardenet 2025

Michaël Fanuel and Rémi Bardenet, *Bypassing orthogonalization in the quantum DPP sampler*, [arXiv:2503.05906v2](https://arxiv.org/abs/2503.05906v2), especially Sections 1.1, 2–3 and 4.2. BibTeX key: `FanuelBardenet2025`.

### Quek-Rebentrost 2022

Yihui Quek and Patrick Rebentrost, *Fast algorithm for quantum polar decomposition and applications*, [Physical Review Research **4**, 013144 (2022)](https://doi.org/10.1103/PhysRevResearch.4.013144); [preprint arXiv:2106.07634](https://arxiv.org/abs/2106.07634). The preprint's Theorem 1 and Corollary 1 explicitly separate the projected singular-vector approximation from the full isometry error. BibTeX key: `QuekRebentrost2022`.

### Gilyen-Su-Low-Wiebe 2019

András Gilyén, Yuan Su, Guang Hao Low and Nathan Wiebe, *Quantum singular value transformation and beyond: exponential improvements for quantum matrix arithmetics*, [STOC 2019, pp. 193–204](https://doi.org/10.1145/3313276.3316366); [full version arXiv:1806.01838](https://arxiv.org/abs/1806.01838). Singular-vector transformation and the bounded polynomial/sign approximation are inherited from this framework. BibTeX key: `GilyenEtAl2019`.

### Berry et al 2018

Dominic W. Berry, Mária Kieferová, Artur Scherer, Yuval R. Sanders, Guang Hao Low, Nathan Wiebe, Craig Gidney and Ryan Babbush, *Improved techniques for preparing eigenstates of fermionic Hamiltonians*, [npj Quantum Information **4**, 22 (2018)](https://doi.org/10.1038/s41534-018-0071-5); [arXiv:1711.10460v3](https://arxiv.org/abs/1711.10460v3), Section II and its sorting-network appendices. BibTeX key: `BerryEtAl2018`.

### Apers-Gao-Ji-Liu 2025

Simon Apers, Minbo Gao, Zhengfeng Ji and Chenghua Liu, *Quantum Speedup for Sampling Random Spanning Trees*, [ICALP 2025, article 13](https://doi.org/10.4230/LIPIcs.ICALP.2025.13). BibTeX key: `ApersEtAl2025`.

### Yoder-Low-Chuang 2014

Theodore J. Yoder, Guang Hao Low and Isaac L. Chuang, *Fixed-point quantum search with an optimal number of queries*, [Physical Review Letters **113**, 210501 (2014)](https://doi.org/10.1103/PhysRevLett.113.210501); [arXiv:1409.3305v2](https://arxiv.org/abs/1409.3305v2). This supplies the coherent fixed-point amplification primitive used to prepare the graph-independent universal key resource. BibTeX key: `YoderLowChuang2014`.

### Wilson 1996

David Bruce Wilson, *Generating random spanning trees more quickly than the cover time*, [STOC 1996, pp. 296–303](https://doi.org/10.1145/237814.237880). BibTeX key: `Wilson1996`.

### Lyons-Peres 2016

Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Cambridge University Press (2016), [author-hosted book and bibliography](https://rdlyons.pages.iu.edu/prbtree/), Chapter 4 for uniform spanning trees and their determinant/electrical-network structure. BibTeX key: `LyonsPeres2016`.

### Lower-bound foundations

Charles Bordenave, *A new proof of Friedman's second eigenvalue theorem and its extension to random lifts*, [Annales scientifiques de l'École Normale Supérieure **53**, 1393–1439 (2020)](https://doi.org/10.24033/asens.2450), Theorem 1; [arXiv:1502.04482](https://arxiv.org/abs/1502.04482). BibTeX key: `Bordenave2020`.

Robert Beals, Harry Buhrman, Richard Cleve, Michele Mosca and Ronald de Wolf, *Quantum lower bounds by polynomials*, [Journal of the ACM **48**, 778–797 (2001)](https://doi.org/10.1145/502090.502097); [arXiv:quant-ph/9802049](https://arxiv.org/abs/quant-ph/9802049). BibTeX key: `BealsEtAl2001`.

Wim van Dam, *Quantum Oracle Interrogation: Getting All Information for Almost Half the Price*, [FOCS 1998, pp. 362–367](https://doi.org/10.1109/SFCS.1998.743486); [arXiv:quant-ph/9805006](https://arxiv.org/abs/quant-ph/9805006). The endpoint argument needs only a linear bound, not its sharp interrogation constant. BibTeX key: `VanDam1998`.

[Machine-readable bibliography](references.bib)

