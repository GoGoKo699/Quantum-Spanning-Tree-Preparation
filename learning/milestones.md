# Thirty milestones from graph access to coherent trees

This is the project's common understanding map. Its targets depend on the science, not on a particular reader's experience or learning history. The single educational anchor is Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, **17 April 2025**; the [anchor bridge](anchor_bridge.md) records the relevant sections and translates their notation. The scientific files remain authoritative for the construction and its claims.

The map has **14 background milestones and 16 construction milestones**. The background connects graph objects, quantum registers, reversible access and determinant states. The construction builds the weighted circuit, proves its coherent output and cleanup, then accounts for its costs and query lower bounds.

| Phase | IDs | Scientific progression |
| --- | --- | --- |
| Background/preliminaries | M01–M14 | A concrete tree state, its graph and circuit language, then the complete problem specification |
| Narrative/innovation | M15–M30 | Weighted incidence, the degree-rooted occupied subspace, polar transport, positive tree amplitudes and sharp weight-query scaling |

Begin with the [four-cycle](anchor_bridge.md#a-four-cycle-from-input-to-clean-output) on vertices $`0,1,2,3`$. Every edge has weight one, every vertex has degree two and each of the four trees has the same weight. Then [add a diagonal of weight two](anchor_bridge.md#one-weighted-diagonal-changes-the-input-state). The same four vertices show how unequal degrees change the input and unequal edge weights change the output. The contrast lower bound uses a separate family of dense graphs.

An anchor pointer supplies foundations, not an assertion that the lecture notes prove the project's local construction. Polar singular-vector transformation, coherent sorting resources, matrix-tree amplitudes and the tree-sign circuit are explicitly supplied in the linked scientific chapters, with research attribution there.

<a id="m01"></a>

## M01 — The object the circuit must produce

Phase: background/preliminaries

Prerequisites: none

**Central question:** What is the output of coherent spanning-tree preparation?

**Understanding target:** Explain that a spanning tree joins every graph vertex without a cycle. Identify the output as one pure state with positive amplitudes whose squares are proportional to the products of their edge weights. Explain what measuring the state gives and what keeping it coherent enables.

**Story role:** Establish the operational destination before introducing its machinery.

**Conceptual connection:** A combinatorial collection becomes a quantum basis family; the preparation problem concerns relative amplitudes and work registers as well as measurement probabilities.

**Source pointers:** Childs §1.1 · [weighted model and output](../science/weighted_preparation.md) · [worked interpretation](anchor_bridge.md#one-weighted-diagonal-changes-the-input-state).

<a id="m02"></a>

## M02 — Four trees and one added edge

Phase: background/preliminaries

Prerequisites: M01

**Central question:** What changes in the target state when the four-cycle gets a weighted diagonal?

**Understanding target:** Count the four trees of the unweighted cycle and recover their amplitudes of one half. Add diagonal $`02`$ with weight two. Count four trees of weight one and four of weight two, then use their total weight to obtain each positive amplitude.

**Story role:** Supply a complete small example that will be revisited after transport, signs and cleanup.

**Conceptual connection:** The sum of tree weights fixes the normalization. A tree's probability uses its weight product and its amplitude uses the square root.

**Source pointers:** Childs §§1.1–1.2 · [four-cycle worked example](anchor_bridge.md#a-four-cycle-from-input-to-clean-output) · [weighted diagonal](anchor_bridge.md#one-weighted-diagonal-changes-the-input-state).

<a id="m03"></a>

## M03 — Registers, superpositions and unwanted records

Phase: background/preliminaries

Prerequisites: M01, M02

**Central question:** Why must a random-seed or sorting record be treated as part of the output state?

**Understanding target:** Explain how a tree register correlated with different work records can have the desired measurement distribution without being the desired pure tree state. Recognize a common fixed work state as a different case: it factors from the tree and may be unprepared independently.

**Story role:** Make the later cleanup obligation visible from the start.

**Conceptual connection:** Tensor-product factorization is the bridge between a successful classical sampler and a genuinely coherent setup circuit.

**Source pointers:** Childs §§1.1–1.2 and §1.4; [universal permutation resource](../science/coherent_preparation.md#a-universal-clean-permutation-resource); [joint output guarantee](../science/model.md#main-theorem).

<a id="m04"></a>

## M04 — Reversible access has a circuit cost

Phase: background/preliminaries

Prerequisites: M03

**Central question:** What information does one graph-oracle call supply, and what does it cost to supply it coherently?

**Understanding target:** Identify the ordinary-degree and sorted neighbor-and-weight queries, and follow how they act reversibly on a superposition of labels. Account for the circuit and work space needed to implement them when the input is supplied as a classical adjacency table.

**Story role:** Ground all later asymptotic statements in a paid input interface.

**Conceptual connection:** Query complexity counts calls to an operation; implementation complexity also counts the circuit that realizes each call.

**Source pointers:** Childs §1.4, §1.6 and §§21.1–21.2 · [weighted access and resources](../science/weighted_preparation.md) · [regular rotation interface](../science/model.md#graph-access-and-output).

<a id="m05"></a>

## M05 — Ports, their partners and endpoint labels

Phase: background/preliminaries

Prerequisites: M04

**Central question:** How can a local port identify an undirected edge without hiding a costly inverse lookup?

**Understanding target:** Explain the rotation involution $`R(v,k)=(w,\ell)`$ and why applying it twice returns the starting port. Distinguish a canonical port label from the endpoint pair $`(u,v)`$; identify sorted neighbor indices as the promise enabling clean binary-search conversion between them.

**Story role:** Fix the input and output labels before they enter the Hilbert spaces.

**Conceptual connection:** The coin/shift language of a quantum walk becomes an explicit reversible graph interface, while output conventions impose additional cleanup requirements.

**Source pointers:** Childs §18.1 and §1.4; [graph access](../science/model.md#graph-access-and-output); [endpoint encoding](../science/polar_transport.md#endpoint-encoding-without-graph-dependent-garbage).

<a id="m06"></a>

## M06 — Incidence turns a graph into a linear map

Phase: background/preliminaries

Prerequisites: M02, M05

**Central question:** What does an oriented incidence row record?

**Understanding target:** Build the four-cycle's edge-by-vertex incidence matrix with $`+1`$ at the smaller endpoint and $`-1`$ at the larger endpoint. Explain that applying a row to vertex values measures their difference, and that the arbitrary orientation convention changes signs without changing the underlying graph.

**Story role:** Introduce the linear object whose determinants will later select trees.

**Conceptual connection:** Local edge differences encode global connectivity once rows are combined; orientation is bookkeeping rather than an extra graph promise.

**Source pointers:** Childs §18.2 for the graph-to-operator entry point; local incidence derivation in [polar transport](../science/polar_transport.md#folding-ports-into-undirected-edges); [four-cycle matrix](../science/interpretation.md#four-cycle-worked-example).

<a id="m07"></a>

## M07 — The Laplacian and its missing constant mode

Phase: background/preliminaries

Prerequisites: M06

**Central question:** Why does the incidence map have one null direction on a connected graph?

**Understanding target:** Explain $`L=B^\dagger B`$ through its sum of squared edge differences. Connectivity makes constant vertex data the only null direction. See why ordinary-degree normalization turns that direction into amplitudes proportional to $`\sqrt{d_v}`$ and why positive edge weights preserve the incidence rank.

**Story role:** Identify the exact mode excluded by the preparation circuit.

**Conceptual connection:** A graph's connectivity statement becomes a rank statement, and the rank determines how many one-particle modes can be occupied isometrically.

**Source pointers:** Childs §§18.2–18.3 · [weighted identity and kernel](../science/weighted_preparation.md) · [regular normalization](../science/polar_transport.md#an-explicit-projected-unitary-encoding).

<a id="m08"></a>

## M08 — What the spectral gap promises

Phase: background/preliminaries

Prerequisites: M07

**Central question:** Which spectral gap controls this algorithm, and which gap is unnecessary?

**Understanding target:** Interpret the known bound on the second normalized-Laplacian eigenvalue as a separation between the null mode and the useful modes. Locate the four-cycle at degree two and normalized gap one. Explain why its random-walk eigenvalue minus one is compatible with this promise. Identify the supplied weight contrast $`\kappa=w_{\max}/w_{\min}`$ as the other parameter in the weighted singular bound.

**Story role:** Give the structural promise its exact meaning before using it in a cost bound.

**Conceptual connection:** Markov-chain spectra guide quantum constructions, but the relevant eigenvalue separation must be identified rather than replaced by a generic mixing-time slogan.

**Source pointers:** Childs §§18.2–18.3 · [weighted gap promise](../science/weighted_preparation.md) · [regular polar singular interval](../science/polar_transport.md#an-explicit-projected-unitary-encoding).

<a id="m09"></a>

## M09 — A projected block can represent a nonunitary map

Phase: background/preliminaries

Prerequisites: M04, M05

**Central question:** How can a quantum circuit contain an incidence-like map that is not itself unitary?

**Understanding target:** Distinguish a full unitary from the input-to-output block selected by known projectors. Trace how a control Hadamard, a controlled rotation and a second Hadamard create a sum or difference of two operations. Keep the block's normalization explicit.

**Story role:** Introduce the circuit representation used by the one-particle ingredient.

**Conceptual connection:** Linear combinations of unitaries and block encodings turn algebraic identities into implementable projected transformations.

**Source pointers:** Childs §28.3 and §29.1; [explicit projected-unitary encoding](../science/polar_transport.md#an-explicit-projected-unitary-encoding).

<a id="m10"></a>

## M10 — Singular vectors and polar transport

Phase: background/preliminaries

Prerequisites: M07, M09

**Central question:** What changes when a linear map's singular values are replaced by one?

**Understanding target:** Explain how a singular-value decomposition pairs input and output directions. The polar factor preserves those pairings and removes the stretching on the nonzero input subspace. Identify the uniform null mode of the cycle as a special case of the degree-rooted mode.

**Story role:** Identify the desired one-particle operation before studying its implementation.

**Conceptual connection:** Normalizing individual output vectors is not enough; an isometry preserves all superpositions and inner products on the occupied subspace.

**Source pointers:** Childs §29.1–§29.3 as the matrix-transformation foundation; the rectangular polar step is supplied locally in [polar isometry](../science/polar_transport.md#the-polar-isometry-and-its-full-state-error).

<a id="m11"></a>

## M11 — Polynomial accuracy and full-state leakage

Phase: background/preliminaries

Prerequisites: M08, M09, M10

**Central question:** Why is a good projected block not by itself a complete state-error guarantee?

**Understanding target:** Explain how a bounded polynomial approximates the polar transformation on a promised singular interval. Distinguish its block error $`\delta`$ from the full unitary-dilation state error of order $`\sqrt\delta`$. Identify the output flags and branch states that must return to fixed clean values.

**Story role:** Establish the accuracy convention that will control the complete preparation.

**Conceptual connection:** QSP supplies polynomial transformation, while unitarity converts successful-block overlap into a bound on all leakage components.

**Source pointers:** Childs §§29.1–29.3 and §2.1; local real-polynomial and leakage derivation in [full-state error](../science/polar_transport.md#the-polar-isometry-and-its-full-state-error).

<a id="m12"></a>

## M12 — Antisymmetry makes determinant amplitudes

Phase: background/preliminaries

Prerequisites: M03, M06, M10

**Central question:** Why does occupying orthonormal one-particle modes generate determinants on edge subsets?

**Understanding target:** Explain the signed sum over particle permutations and its cancellation when two edge labels coincide. After grouping permutations of a distinct sorted subset, identify its amplitude as a determinant of the corresponding orbital rows, with the normalization already included in the antisymmetric basis.

**Story role:** Introduce the many-particle ingredient that converts linear-algebraic rank into combinatorial support.

**Conceptual connection:** Quantum tensor registers carry a fermionic antisymmetry rule; determinant zeros, rather than a membership-search loop, remove forbidden subsets.

**Source pointers:** Childs §1.1 and §§32.2–32.3 for register and fermionic context; the first-quantized determinant construction is supplied in [tree amplitudes](../science/coherent_preparation.md#why-the-nonzero-amplitudes-are-exactly-tree-amplitudes).

<a id="m13"></a>

## M13 — Why maximal incidence minors select trees

Phase: background/preliminaries

Prerequisites: M06, M07, M12

**Central question:** What connects a maximal incidence determinant to a spanning tree?

**Understanding target:** Explain why a non-tree set of $`n-1`$ edges has deficient incidence rank and why a tree's reduced determinant has magnitude one. Scale each row by the square root of its edge weight and identify the effect on the signed tree determinant. Connect normalization to the sum of tree weights.

**Story role:** Establish the support and weight dependence of the determinant state.

**Conceptual connection:** Connectivity, rank and determinant normalization jointly select trees; the surviving relative signs still need a circuit remedy.

**Source pointers:** Childs §§18.2–18.3 for the spectral framework · [weighted tree amplitudes](../science/weighted_preparation.md) · [four-cycle sign table](../science/interpretation.md#four-cycle-worked-example).

<a id="m14"></a>

## M14 — The complete preparation problem

Phase: background/preliminaries

Prerequisites: M01, M03, M04, M05, M08, M09, M10, M11, M12, M13

**Central question:** What must an end-to-end solution accomplish beyond producing the right determinant probabilities?

**Understanding target:** Assemble the known gap and contrast, paid sorted access, positive weighted endpoint-list output and joint error and work-return requirements into one specification. Explain why the route prepares the graph-dependent occupied subspace as well as solving transport, signs and cleanup.

**Story role:** Close the background phase with a global framework rather than one more isolated prerequisite.

**Conceptual connection:** The familiar circuit, walk and matrix tools become a precisely scoped scientific task whose success includes resources and coherent reuse.

**Source pointers:** Childs §1.4, §§18.1–18.3 and §§29.1–29.3 · [weighted model and theorem](../science/weighted_preparation.md) · [science overview](../science/README.md).

<a id="m15"></a>

## M15 — Weighted incidence from local queries

Phase: narrative/innovation

Prerequisites: M05, M07, M09, M14

**Central question:** How do sorted ports and a weight flag produce the normalized incidence block?

**Understanding target:** Prepare a uniform port superposition conditional on the ordinary degree $`d_v`$ and form the antisymmetric port difference. Follow the success factor $`\sqrt{w_e/w_{\max}}`$ shared by the two orientations of edge $`e`$. Read the folded map as $`\Lambda^{1/2}B D^{-1/2}/\sqrt{2w_{\max}}`$ and check its unique null state.

**Story role:** Begin the construction with its load-bearing local identity.

**Conceptual connection:** The LCU difference from Childs becomes a graph incidence block whose exact normalization determines the entire algorithm's spectral cost.

**Source pointers:** Childs §28.3 and §29.1 · [weighted projected encoding](../science/weighted_preparation.md) · [regular block construction](../science/polar_transport.md#an-explicit-projected-unitary-encoding).

<a id="m16"></a>

## M16 — A paid polar isometry on the occupied modes

Phase: narrative/innovation

Prerequisites: M08, M10, M11, M15

**Central question:** How does the gap turn the normalized incidence block into a usable transport circuit?

**Understanding target:** Connect the singular threshold $`\sqrt{\gamma/(2\kappa)}`$ to a polar sign transformation of degree $`O(\sqrt{\kappa/\gamma}\log(n/\epsilon))`$. Explain why the polynomial tolerance is chosen at order $`(\epsilon/n)^2`$ so the full one-particle state error stays of order $`\epsilon/n`$.

**Story role:** Convert the algebraic ingredient into a finite-accuracy coherent operation.

**Conceptual connection:** Polynomial transformation and leakage accounting jointly determine a charged isometry, rather than an uncosted inverse square root.

**Source pointers:** Childs §§29.1–29.3 and §2.1 · [weighted gap and transform](../science/weighted_preparation.md) · [polar circuit and error](../science/polar_transport.md#the-polar-isometry-and-its-full-state-error).

<a id="m17"></a>

## M17 — Fold orientations and erase port indices

Phase: narrative/innovation

Prerequisites: M05, M15, M16

**Central question:** How does an antisymmetric pair of ports become one clean endpoint-encoded edge?

**Understanding target:** Trace the reversible folding of the two ports of each edge into its canonical label and a fixed orientation state. Explain why the symmetric weight factor leaves that orientation state fixed. Follow the paid binary search that erases the old port index when the edge is written as an endpoint pair.

**Story role:** Complete the one-particle route in the same output labels used by the theorem and lower bound.

**Conceptual connection:** An algebraic orientation cancellation and a computational inverse-index lookup are separate obligations, both necessary for the endpoint guarantee.

**Source pointers:** Childs §18.1 and §1.4 · [port folding](../science/polar_transport.md#folding-ports-into-undirected-edges) · [endpoint cleanup](../science/polar_transport.md#endpoint-encoding-without-graph-dependent-garbage) · [weighted extension](../science/weighted_preparation.md).

<a id="m18"></a>

## M18 — Fill the complement by preparing one missing vertex

Phase: narrative/innovation

Prerequisites: M07, M10, M12, M14, M15

**Central question:** How can one degree-rooted state specify all occupied input directions?

**Understanding target:** Prepare amplitudes proportional to $`\sqrt{d_v}`$ from uniform labels, a degree-controlled flag and fixed-point amplification. Map each successful label $`v`$ to the signed list omitting $`v`$ and erase the old label by XOR. Explain why antisymmetrizing this superposition fills the orthogonal complement of the null state.

**Story role:** Supply the many-particle input by specifying its single excluded direction.

**Conceptual connection:** The Hodge dual converts a one-particle null state into the alternating product of all complementary directions.

**Source pointers:** Childs §§1.1–1.2, §1.4 and §19.3 · [degree-rooted input](../science/weighted_preparation.md#prepare-the-missing-vertex-once) · [weighted diagonal example](anchor_bridge.md#one-weighted-diagonal-changes-the-input-state).

<a id="m19"></a>

## M19 — Transport all occupied modes coherently

Phase: narrative/innovation

Prerequisites: M12, M16, M17, M18

**Central question:** What is produced by applying the same one-particle transport to an antisymmetric input?

**Understanding target:** Follow the occupied modes from the complement of the degree-rooted null state into orthonormal edge orbitals. Explain why applying the same polar map to each register preserves antisymmetry and gives determinants on sorted edge subsets.

**Story role:** Join the local transport to the global combinatorial state.

**Conceptual connection:** The exterior-power action of an isometry translates one-particle orthogonality into a normalized many-particle state with meaningful determinant amplitudes.

**Source pointers:** Childs §1.1 and §§32.2–32.3 for context; [preparation circuit](../science/coherent_preparation.md#preparation-and-cleanup-circuit); [orbital-minor identity](../science/coherent_preparation.md#why-the-nonzero-amplitudes-are-exactly-tree-amplitudes).

<a id="m20"></a>

## M20 — A sorting record independent of the subset

Phase: narrative/innovation

Prerequisites: M03, M12, M19

**Central question:** Why can sorting an antisymmetric state return a universal record instead of leaking its edge subset?

**Understanding target:** Explain that a fixed comparator network responds only to the relative ranks of distinct inputs. Its swap record identifies the permutation, and the recorded swap parity cancels the antisymmetric sign. The resulting sorted subset factors from one universal permutation-record state, even across a superposition of different subsets.

**Story role:** Resolve the first possible source of graph-dependent garbage.

**Conceptual connection:** Reversible classical sorting and quantum exchange signs cooperate to compress particle labels coherently; simply discarding a comparison history would not do so.

**Source pointers:** Childs §1.4; [universal resource identity](../science/coherent_preparation.md#a-universal-clean-permutation-resource); [finite state checks and limits](../verification/README.md#what-the-checks-establish-on-the-tested-instances).

<a id="m21"></a>

## M21 — Prepare, reuse and unprepare the universal resource

Phase: narrative/innovation

Prerequisites: M04, M11, M20

**Central question:** How is the permutation resource supplied without an irreversible success-conditioned sampler?

**Understanding target:** Follow uniform random keys, coherent distinctness filtering, and the factorization of sorted keys from the universal record. Explain the role of fixed-point amplification and why the same $`K`$ and $`K^\dagger`$ surround the before-and-after sorting operations. Identify the resulting $`2\eta`$ contribution to joint error.

**Story role:** Complete a reversible preparation route for the many-particle state.

**Conceptual connection:** Childs' amplification and uncomputation foundations support a local resource construction whose seed is retained and cleaned, rather than silently erased.

**Source pointers:** Childs §19.3 and §1.4; the fixed-point specialization and complete factorization are supplied in [universal resource](../science/coherent_preparation.md#a-universal-clean-permutation-resource) and [joint error](../science/coherent_preparation.md#joint-error-clean-work-and-inversion).

<a id="m22"></a>

## M22 — Weighted tree magnitudes from normalized minors

Phase: narrative/innovation

Prerequisites: M13, M17, M18, M19, M21

**Central question:** Why is the amplitude of each tree proportional to the square root of its edge-weight product?

**Understanding target:** Relate the polar orbitals to the root-deleted weighted incidence matrix by a common invertible basis change. Its determinant is shared by all edge subsets. Read the tree-dependent magnitude from the row weights, recognize the rooted sign, and normalize by the sum of the tree products.

**Story role:** Establish the full combinatorial content of the circuit before correcting its phases.

**Conceptual connection:** The common change of basis leaves the relative amplitudes controlled by the weighted incidence minors.

**Source pointers:** Childs §§18.2–18.3 and §29.1 as foundations · [weighted minor proof](../science/weighted_preparation.md) · [unweighted cofactor proof](../science/coherent_preparation.md#why-the-nonzero-amplitudes-are-exactly-tree-amplitudes).

<a id="m23"></a>

## M23 — The determinant sign has a tree description

Phase: narrative/innovation

Prerequisites: M06, M13, M22

**Central question:** How can a tree's determinant sign be computed without evaluating a dense determinant?

**Understanding target:** Root the tree at zero and assign each edge its child endpoint. Explain why these children permute the nonroot vertex labels, and why the reduced determinant equals that permutation's parity times the product of the child incidence signs. Recognize the nilpotent parent matrix behind the proof.

**Story role:** Replace a potentially expensive algebraic phase evaluation by a graph computation.

**Conceptual connection:** A determinant's orientation information becomes rooted-tree structure, making a positive-amplitude q-sample computationally accessible.

**Source pointers:** Childs §1.4 for reversible computation; [exact sign identity](../science/sign_cleanup.md#input-orientation-and-the-exact-phase); [four-cycle determinant convention](../science/interpretation.md#four-cycle-worked-example).

<a id="m24"></a>

## M24 — Rooting through fixed-network joins

Phase: narrative/innovation

Prerequisites: M04, M20, M23

**Central question:** How is the sign computed coherently without assuming a free data-dependent memory lookup?

**Understanding target:** Follow the two directed arcs per tree edge, their Euler-tour successor cycle, and pointer doubling after breaking the cycle at the root. Explain how fixed sorting-network joins implement the needed successor lookups, including repeated keys at the terminal. Trace compute–phase–uncompute through the final sign bit.

**Story role:** Establish the gate and workspace legitimacy of sign removal.

**Conceptual connection:** A classical nearlinear graph procedure becomes a fixed reversible circuit once its variable-address lookups are replaced by batched sorting operations.

**Source pointers:** Childs §1.4; [lookup primitive](../science/sign_cleanup.md#a-fixed-network-lookup-primitive), [Euler rooting](../science/sign_cleanup.md#rooting-a-tree-by-an-euler-tour), and [complete phase circuit](../science/sign_cleanup.md#complete-reversible-phase-circuit).

<a id="m25"></a>

## M25 — Finish the weighted four-vertex state

Phase: narrative/innovation

Prerequisites: M02, M17, M19, M21, M22, M23, M24

**Central question:** Where does each amplitude, sign and work register end up after the weighted diagonal is added?

**Understanding target:** Trace the ordinary degrees $`(3,2,3,2)`$, signed missing-vertex list and three polar transports. Explain why sorting and sign correction return clean work and give amplitudes $`1/\sqrt{12}`$ on each tree omitting the diagonal and $`\sqrt2/\sqrt{12}`$ on each tree using it.

**Story role:** Integrate the construction on one complete irregular instance before bounding the general circuit.

**Conceptual connection:** Positive amplitudes combine the tree-weight rule with coherent sign correction and workspace cleanup.

**Source pointers:** Childs §§1.1–1.4 for the circuit reading · [weighted example](anchor_bridge.md#one-weighted-diagonal-changes-the-input-state) · [four-cycle baseline](../science/interpretation.md#four-cycle-worked-example).

<a id="m26"></a>

## M26 — Joint accuracy and reusable inverses

Phase: narrative/innovation

Prerequisites: M11, M16, M21, M24, M25

**Central question:** Why does the complete circuit satisfy one joint output-and-work error guarantee?

**Understanding target:** Apply a hybrid argument to the degree-rooted state, the $`n-1`$ entangled particle operations, numerical synthesis and the forward/backward universal permutation resource. Explain why total reversible sign processing preserves the accumulated error even on malformed branches. Relate clean preparation and its inverse to an approximate reflection and charge repeated-use error.

**Story role:** Turn exact identities into the finite-accuracy theorem actually claimed.

**Conceptual connection:** Childs' subadditivity principle links local implementation tolerances to a global coherent interface, rather than to independent successful-block tests.

**Source pointers:** Childs §2.1 and §19.3 · [weighted precision and work return](../science/weighted_preparation.md) · [reflections](../science/interpretation.md#reflections-and-tree-dependent-operations).

<a id="m27"></a>

## M27 — Charge the complete preparation

Phase: narrative/innovation

Prerequisites: M04, M05, M16, M17, M18, M21, M24, M26

**Central question:** Which resources remain after all local ingredients are assembled?

**Understanding target:** Assemble $`\widetilde O(n\sqrt{\kappa/\gamma})`$ queries from the one-time $`\widetilde O(\sqrt n)`$ degree-state preparation, transport on each occupied slot and endpoint conversion. Charge the supplied oracle gates and workspace, finite-bit weight arithmetic, sorting, sign gates and separate classical phase compilation.

**Story role:** State the capability in the same cost model as its construction.

**Conceptual connection:** Fast polynomial transformation is one component of the algorithm; its physical interface, work-return obligations and classical circuit preparation determine the complete comparison.

**Source pointers:** Childs §§1.5–1.6 and §2.1 · [weighted resources](../science/weighted_preparation.md) · [regular baseline resources](../science/resources.md).

<a id="m28"></a>

## M28 — A dense fixed-gap family with hidden weight boosts

Phase: narrative/innovation

Prerequisites: M05, M08, M14, M27

**Central question:** How can changing one weight make a visible difference to the tree law while both normalized gaps stay fixed?

**Understanding target:** Start with $`N`$ rows attached to the same $`q`$ core vertices in a clique. Give each row at most one boost from weight one to $`q`$. Use the row and clique energy comparison to justify a constant gap. Use effective resistance and the row cut to bound a candidate edge's inclusion probability with and without its boost.

**Story role:** Build the same physical graph-access promise for the two contrast lower bounds.

**Conceptual connection:** A tree edge's inclusion probability carries a constant signal about a hidden weight even though the topology is fixed.

**Source pointers:** Childs §§21.1–21.2 for the query framework · [dense family and gap](../science/weight_contrast_lower_bound.md#a-dense-family-with-fixed-gaps) · [edge inclusion comparison](../science/weight_contrast_lower_bound.md#one-edge-event-distinguishes-adjacent-inputs).

<a id="m29"></a>

## M29 — Turn a visible boost into quantum and classical query bounds

Phase: narrative/innovation

Prerequisites: M04, M26, M28

**Central question:** Why do the same possible boosts impose different costs on quantum and classical samplers?

**Understanding target:** For the quantum bound, form the Kronecker sum of row stars and see why its norm is $`N\sqrt q`$ while the norm filtered by a particular query is one. Use the edge event to bound the final overlap for an adjacent input pair even at constant output error. For the classical bound, compare each single boost with the all-unit-weight input under shared randomness and sum the probabilities of touching the changed edges.

**Story role:** Match the quantum square-root contrast cost and compare it with the classical cost on the same dense family.

**Conceptual connection:** A common sampling distinction supplies two kinds of progress bound, one through quantum state overlap and the other through identical classical transcripts.

**Source pointers:** Childs §§21.1–21.2 and Chapter 23 · [quantum lower bound](../science/weight_contrast_lower_bound.md#quantum-queries) · [classical lower bound](../science/weight_contrast_lower_bound.md#classical-queries).

<a id="m30"></a>

## M30 — The established capability and its boundary

Phase: narrative/innovation

Prerequisites: M14, M22, M24, M25, M26, M27, M28, M29

**Central question:** Which graph promises, outputs and costs go together in the weighted theorem?

**Understanding target:** Explain the route from sorted local degree and weight queries to clean positive weighted tree amplitudes and a reversible preparation. State the supplied gap and contrast, and the circuit and compilation costs alongside the query count. Read the quantum and classical contrast separation on the dense hard family alongside the older linear bound for regular unweighted graphs. Identify optimal dependence on a shrinking gap and a hardware crossover as separate questions.

**Story role:** Close the map by integrating mechanism, evidence, attribution, cost and scope into one scientific proposition.

**Conceptual connection:** Degree normalization and antisymmetry determine which trees appear, while the local weight filter determines their amplitudes and the cost of learning the weighted interface.

**Source pointers:** Childs §1.6, §§18.1–18.3, §§21.1–21.2 and §§29.1–29.3 · [weighted theorem](../science/weighted_preparation.md) · [contrast lower bounds](../science/weight_contrast_lower_bound.md) · [related work](../references/related_work.md).
