# Related work and attribution

The [preparation theorem](../science/weighted_preparation.md) constructs a clean, positive spanning-tree q-sample from sorted weighted adjacency and degree queries. The graph can be irregular, its edge weights lie in a supplied positive range of contrast $`\kappa`$, and a lower bound $`\gamma`$ on either normalized-Laplacian gap is supplied. The query bound is $`\widetilde O(n\sqrt{\kappa/\gamma})`$ without graph-dependent preprocessing. The oracle implementation, bit precision, and graph-independent phase compilation are accounted for separately.

The determinant description of weighted spanning trees, fermionic antisymmetry, quantum polar decomposition, and QSVT are established ingredients. The graph access construction normalizes its coins by unweighted degrees, flags edge weights locally, and fills the complement of a single degree-rooted vertex state. It then uses the incidence polar isometry, the sorting resource, and the rooted-incidence sign compiler to obtain the positive endpoint state and erase the work. The accompanying [lower bounds](../science/weight_contrast_lower_bound.md) determine the cost of contrast on a dense family whose weighted and unweighted gaps are both constant.

## Direct comparisons

Here $`n`$ is the number of vertices, $`m`$ the number of edges, $`M`$ an explicit matrix's row count, and $`r`$ its rank. Tildes hide logarithmic factors. The original theorems give their own accuracy and failure parameters.

| Source and task | Access and established resource | Relationship to this result |
| --- | --- | --- |
| [Hamoudi–Tanasa–Sridhara, 2026](#hamoudi-tanasa-sridhara-2026): positive weighted spanning-tree q-samples | For connected weighted graphs with $`m\ge 100n`$, Theorem 3.1 uses sorted adjacency lists and preprocesses with $`\widetilde O(\sqrt{mn/\rho})`$ queries. Subsequent preparation uses $`\widetilde O(\sqrt{mn\rho})`$ queries and reflection uses $`\widetilde O(\sqrt{m\rho})`$ for $`\rho\in[n/m,1]`$. Its implementation discussion uses QRAM and gives a loose quadratic time bound. | At fixed accuracy and failure probability, set $`\rho=1`$ to compare a first sample including preprocessing. This gives $`\widetilde O(\sqrt{mn})`$ for the general method and $`\widetilde O(n\sqrt{\kappa/\gamma})`$ for the gap-and-contrast promise here. The prior tradeoff also addresses many samples and cheaper amortized reflections. |
| [Kerenidis–Prakash, 2022](#kerenidis-prakash-2022): determinant and subspace states | For an explicit $`M\times r`$ matrix, Theorem 5.5 uses $`O(Mr^2)`$ classical orthogonalization and $`O(Mr\log M)`$ gates per sample. A supplied embedding with a short Givens decomposition is a favorable special case. | The exterior-power construction and determinant amplitudes are inherited. The local graph compiler produces the orthonormal image implicitly, without constructing its dense matrix or Givens decomposition. |
| [Fanuel–Bardenet, 2025](#fanuel-bardenet-2025): bypassing orthogonalization in a projection-DPP sampler | Column normalization costs $`O(Mr)`$. The resulting circuit uses rejection or amplification governed by the column-normalized Gram determinant. The examples include uniform spanning trees. | Both methods bypass orthogonalization. The local-oracle compiler pays for the inverse singular gap to implement a polar isometry, then transports the full occupied exterior state. |
| [Quek–Rebentrost, 2022](#quek-rebentrost-2022), building on [Gilyén–Su–Low–Wiebe, 2019](#gilyen-su-low-wiebe-2019): polar isometry | Projected-unitary access and a nonzero singular-value lower bound $`\delta`$ give a polar transform with $`O(\delta^{-1}\log(1/\varepsilon))`$ queries, with full-output error accounted for separately from the projected block. | The weighted graph construction guarantees $`\delta\ge\sqrt{\gamma/(2\kappa)}`$ and prepares all occupied input modes in the supported subspace. |
| [Berry et al., 2018](#berry-et-al-2018): first-quantized antisymmetrization | Section II antisymmetrizes sorted, distinct tuples coherently using sorting networks, with nearlinear size up to logarithms in particle count and label range. | The same permutation machinery serves the graph-independent resource in the tree compiler. Returning the output in sorted order allows that resource to be separated and unprepared. |
| [Apers–Gao–Ji–Liu, 2025](#apers-gao-ji-liu-2025): random spanning-tree samples | For general weighted graphs, $`\widetilde O(\sqrt{mn})`$ quantum queries and time for a classical tree sample at fixed accuracy. | Measuring the state here also produces a classical tree sample. The clean coherent circuit gives an inverse as an additional capability. |

## Compare the same first-sample output

Hamoudi–Tanasa–Sridhara's q-sample stores a weight with each sorted endpoint pair. The endpoint state here can coherently append the weight of every output edge by reversible binary search in the sorted lists, using $`O(n\log n)`$ more local calls. This fits the stated soft query bound. The endpoint-only output can also be recovered by running the same weight lookup in reverse. This lets the one-sample comparison use the same encoding and include preprocessing on both sides. [Weighted output and resources](../science/weighted_preparation.md).

For dense graphs at fixed gap and fixed contrast, the direct compiler uses nearlinear queries in $`n`$, while the general first-sample guarantee is $`\widetilde O(n^{3/2})`$. More generally, the two upper bounds differ by a polynomial factor when $`m/n`$ exceeds $`\kappa/\gamma`$ by a polynomial factor. The direct construction obtains a reflection by applying the preparation circuit and its inverse around a fixed zero-state phase. The amortized reflection bound of Hamoudi–Tanasa–Sridhara uses their preprocessed data structures. The [regular unweighted construction](../science/model.md) is also available directly in the rotation interface, with the familiar $`\widetilde O(n/\sqrt{\gamma})`$ rotation cost.

## Compare the lower-bound promises

Theorem 4.2 of Hamoudi–Tanasa–Sridhara gives a general $`\widetilde\Omega(\sqrt{kmn})`$ quantum-query lower bound for $`k`$ copies in its stated range. Its construction uses independent rows of hidden edge weights, zero-weight candidates and a very heavy hub. The dense family here also gives each row an independent unknown choice. It uses a fixed clique core and only positive weights, in $`\{1,\kappa\}`$, and both of its normalized gaps are bounded below by a constant. The tree marginal of the changed edge separates neighboring oracle inputs, which suffices for an adversary progress bound for one coherent output. This gives $`\Omega(n\sqrt{\kappa})`$ queries with constant error, even if the topology is given. [Dense weighted lower bound](../science/weight_contrast_lower_bound.md).

On the same family, one classical tree sample requires an expected $`\Omega(n\kappa)`$ weight queries. Querying all mutable weights gives a matching classical cost in the query model, with computation after queries charged separately when discussing a real implementation. This classical separation applies to the weighted promise family above. For regular unweighted graphs, Wilson's loop-erased-walk method and cover-time bounds provide the separate classical benchmark. A reversible classical sampler ordinarily retains its random seed, while a q-sampler must dispose of its working records coherently. [Wilson, 1996](#wilson-1996).

The [cubic-graph lower bound](../science/lower_bound.md) separately encodes hidden bits in forced bridge endpoints and gives $`\Omega(n)`$ calls for endpoint output at constant gap. It uses polynomial-method and oracle-interrogation ideas, with base expanders supplied by Bordenave's formulation of Friedman's theorem. The two lower bounds resolve vertex and contrast costs for the respective fixed-gap families. Sharp dependence on a shrinking gap remains open in this account.

## Interface boundaries

The sorted neighbor promise supplies reversible inverse-index lookup for canonical endpoint output. With an arbitrary port order, the polar construction can retain canonical port labels. Conventional endpoints then require a separately supplied and charged inverse-index locator. The weighted theorem uses a gap lower bound and an explicit implementation of coherent access. Physical runtime depends on that implementation, arithmetic precision, phase compilation and gate costs. The cited general-purpose tradeoffs, determinant samplers and classical algorithms establish their respective guarantees under the assumptions listed above.

## Sources

### Hamoudi-Tanasa-Sridhara 2026

Yassine Hamoudi, Adrian Tanasa and Shrinidhi Teganahally Sridhara, *Quantum Sampling of Random Spanning Trees via Amortized Data Structures*. The comparison uses the oracle model in Section 2, the guarantees in Theorem 3.1, the implementation discussion in Section 3.5 and the lower-bound construction in Section 4 leading to Theorem 4.2. BibTeX key `HamoudiTanasaSridhara2026`. [arXiv:2609.40314v1](https://arxiv.org/html/2609.40314v1). [Author-hosted revision dated 6 November 2026](https://shrinidhits.bitbucket.io/files/publications/spanning-trees.pdf).

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

Theodore J. Yoder, Guang Hao Low and Isaac L. Chuang, *Fixed-point quantum search with an optimal number of queries*. The fixed-point amplification primitive prepares both the graph-independent permutation resource and the degree-rooted vertex state. BibTeX key `YoderLowChuang2014`. [Physical Review Letters **113**, 210501 (2014)](https://doi.org/10.1103/PhysRevLett.113.210501). [arXiv:1409.3305v2](https://arxiv.org/abs/1409.3305v2).

### Wilson 1996

David Bruce Wilson, *Generating random spanning trees more quickly than the cover time*, [STOC 1996, pp. 296–303](https://doi.org/10.1145/237814.237880). BibTeX key: `Wilson1996`.

### Lyons-Peres 2016

Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Cambridge University Press (2016). Chapter 4 gives the spanning-tree determinant and the transfer-current identity that expresses an edge marginal through its conductance and effective resistance. BibTeX key `LyonsPeres2016`. [Author-hosted book and bibliography](https://rdlyons.pages.iu.edu/prbtree/).

### Lower-bound foundations

Howard Barnum, Michael E. Saks and Mario Szegedy, *Quantum query complexity and semi-definite programming*, CCC 2003, pp. 179–193. This is a source for the spectral adversary method. BibTeX key `BarnumSaksSzegedy2003`. [Conference paper](https://doi.org/10.1109/CCC.2003.1214419).

Troy Lee, Rajat Mittal, Ben W. Reichardt, Robert Špalek and Mario Szegedy, *Quantum query complexity of state conversion*, FOCS 2011, pp. 344–353. It formulates query lower bounds for input-dependent states through their Gram matrices. The dense weight-query proof uses an explicit positive adversary progress calculation. BibTeX key `LeeEtAl2011`. [Conference paper](https://doi.org/10.1109/FOCS.2011.75). [arXiv:1011.3020v2](https://arxiv.org/abs/1011.3020v2).

Charles Bordenave, *A new proof of Friedman's second eigenvalue theorem and its extension to random lifts*, [Annales scientifiques de l'École Normale Supérieure **53**, 1393–1439 (2020)](https://doi.org/10.24033/asens.2450), Theorem 1; [arXiv:1502.04482](https://arxiv.org/abs/1502.04482). BibTeX key: `Bordenave2020`.

Robert Beals, Harry Buhrman, Richard Cleve, Michele Mosca and Ronald de Wolf, *Quantum lower bounds by polynomials*, [Journal of the ACM **48**, 778–797 (2001)](https://doi.org/10.1145/502090.502097); [arXiv:quant-ph/9802049](https://arxiv.org/abs/quant-ph/9802049). BibTeX key: `BealsEtAl2001`.

Wim van Dam, *Quantum Oracle Interrogation: Getting All Information for Almost Half the Price*, [FOCS 1998, pp. 362–367](https://doi.org/10.1109/SFCS.1998.743486); [arXiv:quant-ph/9805006](https://arxiv.org/abs/quant-ph/9805006). The endpoint argument needs only a linear bound, not its sharp interrogation constant. BibTeX key: `VanDam1998`.

[Machine-readable bibliography](references.bib)

