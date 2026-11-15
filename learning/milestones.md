# Thirty milestones from graph access to coherent trees

This is the project's common understanding map. Its targets depend on the science, not on a particular reader's experience or learning history. The single educational anchor is Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, **17 April 2025**; the [anchor bridge](anchor_bridge.md) records the relevant sections and translates their notation. The scientific files remain authoritative for the construction and its claims.

The allocation is **14 background/preliminary milestones and 16 narrative/innovation milestones**. The background connects graph objects, quantum registers, reversible access and determinant states before assembling a precise preparation problem. The narrative then builds the circuit from its one-particle ingredient, proves its output and cleanup, and integrates its complete costs and lower bound. Both phases move from local ingredients toward a global account. This map covers the load-bearing ideas and boundaries; it does not enumerate every technical lemma.

| Phase | IDs | Scientific progression |
| --- | --- | --- |
| Background/preliminaries | M01–M14 | A concrete tree state, its graph and circuit language, then the complete problem specification |
| Narrative/innovation | M15–M30 | Normalized incidence, polar transport, coherent determinant assembly, positive signs, complete cost and lower-bound synthesis |

The running example is always the same four-cycle $`C_4`$: vertices $`0,1,2,3`$, sorted edges $`(01),(03),(12),(23)`$, degree two, normalized-Laplacian gap one, and root zero. It has four spanning trees, each obtained by deleting one edge. Its [worked account](../science/interpretation.md#four-cycle-worked-example) connects the abstract circuit to a complete output state. The later lower bound uses a separate graph family because a four-vertex example cannot establish asymptotic necessity.

An anchor pointer supplies foundations, not an assertion that the lecture notes prove the project's local construction. Polar singular-vector transformation, coherent sorting resources, matrix-tree amplitudes and the tree-sign circuit are explicitly supplied in the linked scientific chapters, with research attribution there.

<a id="m01"></a>

## M01 — The object the circuit must produce

Phase: background/preliminaries

Prerequisites: none

**Central question:** What is the output of coherent spanning-tree preparation?

**Understanding target:** Explain that a spanning tree joins every graph vertex without a cycle, and identify the output as one pure state with equal positive amplitude on every sorted tree edge list. Distinguish this state from a classical record naming one randomly selected tree.

**Story role:** Establish the operational destination before introducing its machinery.

**Conceptual connection:** A combinatorial collection becomes a quantum basis family; the preparation problem concerns relative amplitudes and work registers as well as measurement probabilities.

**Source pointers:** Childs §1.1; [model: graph, access and output](../science/model.md#graph-access-and-output); [worked interpretation](../science/interpretation.md#four-cycle-worked-example).

<a id="m02"></a>

## M02 — Four trees in one fixed example

Phase: background/preliminaries

Prerequisites: M01

**Central question:** What does the target look like on the four-cycle?

**Understanding target:** Follow why deleting any one of the four cycle edges leaves a tree, why there are exactly four outputs, and why the target amplitudes have magnitude one half. Interpret a measurement as choosing a deleted edge uniformly, while the unmeasured state retains its phase relations.

**Story role:** Supply a complete small example that will be revisited after transport, signs and cleanup.

**Conceptual connection:** Normalization ties the size of a combinatorial family to its state amplitudes; it does not determine their signs.

**Source pointers:** Childs §§1.1–1.2; [four-cycle worked example](../science/interpretation.md#four-cycle-worked-example); [main theorem](../science/model.md#main-theorem).

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

**Understanding target:** Read a controlled reversible oracle as a transformation on superpositions of labels, with its own gate cost $`C_R`$ and clean workspace $`S_R`$. Explain why a classical adjacency table does not automatically provide that operation at polylogarithmic physical cost.

**Story role:** Ground all later asymptotic statements in a paid input interface.

**Conceptual connection:** Query complexity counts calls to an operation; implementation complexity also counts the circuit that realizes each call.

**Source pointers:** Childs §1.4, §1.6 and §§21.1–21.2; [model interface](../science/model.md#graph-access-and-output); [complete resources](../science/resources.md).

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

**Understanding target:** Explain $`L=B^\dagger B`$ through its sum of squared edge differences. A constant vertex vector has zero difference on every edge; connectivity makes it the only such direction. Recognize that disconnected graphs have additional null directions and therefore require a different occupied subspace.

**Story role:** Identify the exact mode excluded by the preparation circuit.

**Conceptual connection:** A graph's connectivity statement becomes a rank statement, and the rank determines how many one-particle modes can be occupied isometrically.

**Source pointers:** Childs §§18.2–18.3; [normalized identity and kernel](../science/polar_transport.md#an-explicit-projected-unitary-encoding); [verification promise boundaries](../verification/README.md#what-the-checks-establish-on-the-tested-instances).

<a id="m08"></a>

## M08 — What the spectral gap promises

Phase: background/preliminaries

Prerequisites: M07

**Central question:** Which spectral gap controls this algorithm, and which gap is unnecessary?

**Understanding target:** Interpret the known bound on the second normalized-Laplacian eigenvalue as a separation between the constant null mode and the useful modes. Explain why a bipartite graph is permitted even though its random walk can have eigenvalue minus one. Locate the four-cycle at degree two and normalized gap one.

**Story role:** Give the structural promise its exact meaning before using it in a cost bound.

**Conceptual connection:** Markov-chain spectra guide quantum constructions, but the relevant eigenvalue separation must be identified rather than replaced by a generic mixing-time slogan.

**Source pointers:** Childs §§18.2–18.3; [gap promise](../science/model.md#graph-access-and-output); [polar singular interval](../science/polar_transport.md#an-explicit-projected-unitary-encoding).

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

**Understanding target:** Explain that a singular-value decomposition pairs input and output directions, while singular values describe their stretching. The polar factor preserves those pairings and removes the stretching on the nonzero input subspace. It cannot be an isometry on a null direction, which is why the uniform mode is excluded.

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

**Understanding target:** Explain why a non-tree set of $`n-1`$ edges has deficient incidence rank, while a tree's reduced determinant has magnitude one. Connect the matrix-tree normalization to the number of trees. On the four-cycle, recognize the reduced signs $`+,-,-,-`$ under the fixed root and edge convention.

**Story role:** Establish the combinatorial theorem that gives the determinant state its intended support and equal magnitudes.

**Conceptual connection:** Connectivity, rank and determinant normalization jointly select trees; the surviving relative signs still need a circuit remedy.

**Source pointers:** Childs §§18.2–18.3 for the spectral framework; local cofactor and matrix-tree derivation in [tree amplitudes](../science/coherent_preparation.md#why-the-nonzero-amplitudes-are-exactly-tree-amplitudes); [four-cycle sign table](../science/interpretation.md#four-cycle-worked-example).

<a id="m14"></a>

## M14 — The complete preparation problem

Phase: background/preliminaries

Prerequisites: M01, M03, M04, M05, M08, M09, M10, M11, M12, M13

**Central question:** What must an end-to-end solution accomplish beyond producing the right determinant probabilities?

**Understanding target:** Assemble the graph promises, paid controlled access, known uniform complement, positive endpoint-list output, joint error and work-return requirements into one specification. Explain why the candidate route must solve transport, antisymmetrization, sign removal and cleanup together.

**Story role:** Close the background phase with a global framework rather than one more isolated prerequisite.

**Conceptual connection:** The familiar circuit, walk and matrix tools become a precisely scoped scientific task whose success includes resources and coherent reuse.

**Source pointers:** Childs §1.4, §§18.1–18.3 and §§29.1–29.3; [model and theorem](../science/model.md); [science overview](../science/README.md).

<a id="m15"></a>

## M15 — Normalized incidence from one controlled rotation

Phase: narrative/innovation

Prerequisites: M05, M07, M09, M14

**Central question:** Why does the actual projected circuit give $`A^\dagger A=(I-P)/2`$?

**Understanding target:** Follow the uniform port isometry $`V`$, the difference map $`A=(I-R)V/2`$, and the involution identity $`(I-R)^2=2(I-R)`$. Explain the resulting normalization and why its useful singular values depend on the normalized gap without an extra degree factor.

**Story role:** Begin the construction with its load-bearing local identity.

**Conceptual connection:** The LCU difference from Childs becomes a graph incidence block whose exact normalization determines the entire algorithm's spectral cost.

**Source pointers:** Childs §28.3 and §29.1; [projected encoding proof](../science/polar_transport.md#an-explicit-projected-unitary-encoding); [finite encoding checks](../verification/README.md#what-the-checks-establish-on-the-tested-instances).

<a id="m16"></a>

## M16 — A paid polar isometry on the occupied modes

Phase: narrative/innovation

Prerequisites: M08, M10, M11, M15

**Central question:** How does the gap turn the normalized incidence block into a usable transport circuit?

**Understanding target:** Connect the singular threshold $`\sqrt{\gamma/2}`$ to a polar sign transformation of degree $`O(\gamma^{-1/2}\log(n/\epsilon))`$. Explain why the polynomial tolerance is chosen at order $`(\epsilon/n)^2`$, so the full one-particle state error can be made order $`\epsilon/n`$.

**Story role:** Convert the algebraic ingredient into a finite-accuracy coherent operation.

**Conceptual connection:** Polynomial transformation and leakage accounting jointly determine a charged isometry, rather than an uncosted inverse square root.

**Source pointers:** Childs §§29.1–29.3 and §2.1; [polar circuit and error](../science/polar_transport.md#the-polar-isometry-and-its-full-state-error); [precision choices](../science/resources.md#parameters-and-precision).

<a id="m17"></a>

## M17 — Fold orientations and erase port indices

Phase: narrative/innovation

Prerequisites: M05, M15, M16

**Central question:** How does an antisymmetric pair of ports become one clean endpoint-encoded edge?

**Understanding target:** Trace the reversible folding of the two ports of an edge into a canonical label and one fixed orientation state. Explain why the orientation qubit can be cleaned, why the resulting map is $`B(L|_{s^\perp})^{-1/2}`$, and where sorted neighbor access pays for erasing the old port index.

**Story role:** Complete the one-particle route in the same output labels used by the theorem and lower bound.

**Conceptual connection:** An algebraic orientation cancellation and a computational inverse-index lookup are separate obligations, both necessary for the endpoint guarantee.

**Source pointers:** Childs §18.1 and §1.4; [port folding](../science/polar_transport.md#folding-ports-into-undirected-edges); [endpoint cleanup](../science/polar_transport.md#endpoint-encoding-without-graph-dependent-garbage).

<a id="m18"></a>

## M18 — An explicit complement for arbitrary vertex count

Phase: narrative/innovation

Prerequisites: M07, M10, M14

**Central question:** How is the uniform null mode excluded without preparing a table of graph eigenvectors?

**Understanding target:** Explain the known Householder reflection that sends basis label zero to the uniform valid vertex state. Its remaining $`n-1`$ columns form the required complement. Identify why preserving the valid subspace matters when $`n`$ is not a power of two, and why a generic first-column state preparation alone would not establish that property.

**Story role:** Supply the actual input orbitals for the many-particle circuit.

**Conceptual connection:** Simple known-state preparation replaces graph-dependent eigensystem preparation while respecting padded register labels.

**Source pointers:** Childs §§1.1–1.2 and §1.4; [Householder construction and prefix rotations](../science/coherent_preparation.md#a-known-basis-of-the-correct-vertex-subspace).

<a id="m19"></a>

## M19 — Transport all occupied modes coherently

Phase: narrative/innovation

Prerequisites: M12, M16, M17, M18

**Central question:** What is produced by applying the same one-particle transport to an antisymmetric input?

**Understanding target:** Follow the occupied modes from the known complement into orthonormal edge orbitals. Explain why linearity preserves the antisymmetric superposition and why the final sorted-subset coefficients depend on orbital determinants rather than separately sampled particles.

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

## M22 — Uniform tree magnitudes from normalized minors

Phase: narrative/innovation

Prerequisites: M13, M17, M18, M19, M21

**Central question:** Why does the assembled state have equal magnitude on every tree, with no non-tree support in the ideal limit?

**Understanding target:** Connect rank-deficient non-tree minors to zero amplitude, the reduced incidence cofactors to signs of unit magnitude, and the product of nonzero Laplacian eigenvalues to the common normalization. Explain that the basis-completion determinant contributes one global phase, while the reduced tree determinant supplies the remaining relative sign.

**Story role:** Establish the full combinatorial content of the circuit before correcting its phases.

**Conceptual connection:** Polar normalization, orthogonal-complement preparation and the matrix-tree theorem make a determinant state into a uniform signed tree state.

**Source pointers:** Childs §§18.2–18.3 and §29.1 as foundations; [complete minor and cofactor proof](../science/coherent_preparation.md#why-the-nonzero-amplitudes-are-exactly-tree-amplitudes); [four-cycle signs](../science/interpretation.md#four-cycle-worked-example).

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

## M25 — Finish the four-cycle state

Phase: narrative/innovation

Prerequisites: M02, M17, M19, M21, M22, M23, M24

**Central question:** Where does each amplitude, sign and clean work register end up in the complete small example?

**Understanding target:** Trace the same four-cycle from normalized incidence through polar transport, its three occupied modes, sorted signed tree amplitudes and final sign correction. Explain how the $`+,-,-,-`$ table becomes four positive amplitudes of one half, with both permutation-resource and sign workspace cleaned.

**Story role:** Integrate the mechanism on one complete instance before returning to all-size error and cost.

**Conceptual connection:** Equal measured probabilities were already present before sign correction; the correction and cleanup establish the stronger pure-state result that M01 specified.

**Source pointers:** Childs §§1.1–1.4 for the circuit reading; [complete four-cycle example](../science/interpretation.md#four-cycle-worked-example); [preparation and cleanup](../science/coherent_preparation.md#preparation-and-cleanup-circuit).

<a id="m26"></a>

## M26 — Joint accuracy and reusable inverses

Phase: narrative/innovation

Prerequisites: M11, M16, M21, M24, M25

**Central question:** Why does the complete circuit satisfy one joint output-and-work error guarantee?

**Understanding target:** Apply a hybrid argument to the $`n-1`$ entangled particle operations and the forward/backward universal resource. Explain why total reversible sign processing preserves existing error even on malformed branches, and why approximation does not permit treating leakage as corrected. Relate a clean preparation and its inverse to an approximate reflection, with repeated-use error charged.

**Story role:** Turn exact identities into the finite-accuracy theorem actually claimed.

**Conceptual connection:** Childs' subadditivity principle links local implementation tolerances to a global coherent interface, rather than to independent successful-block tests.

**Source pointers:** Childs §2.1 and §19.3; [joint error proof](../science/coherent_preparation.md#joint-error-clean-work-and-inversion); [reflections and tree-dependent operations](../science/interpretation.md#reflections-and-tree-dependent-operations).

<a id="m27"></a>

## M27 — Charge the complete preparation

Phase: narrative/innovation

Prerequisites: M04, M05, M16, M17, M18, M21, M24, M26

**Central question:** Which resources remain after all local ingredients are assembled?

**Understanding target:** Reconstruct the soft $`O(n/\sqrt\gamma)`$ quantum call scaling, its multiplication by the oracle gate cost, and the separate oracle-workspace term. Include endpoint conversion, sorting, sign gates, precision and classical phase compilation. Explain why the fixed-positive-gap regime has a nearlinear complete bound when the supplied access circuit is efficient.

**Story role:** State the capability in the same cost model as its construction.

**Conceptual connection:** Fast polynomial transformation is one component of the algorithm; its physical interface, work-return obligations and classical circuit preparation determine the complete comparison.

**Source pointers:** Childs §1.5–§1.6 and §2.1; [quantum operations](../science/resources.md#quantum-operations); [classical compilation](../science/resources.md#classical-circuit-compilation); [scope](../science/resources.md#scope-of-the-improvement).

<a id="m28"></a>

## M28 — Hard endpoint output at constant gap

Phase: narrative/innovation

Prerequisites: M05, M08, M14, M27

**Central question:** How can every valid output tree reveal many hidden bits while the graph remains a regular expander?

**Understanding target:** Follow the cubic base graph, bounded-size attached gadgets, forced bridges and hidden label swaps. Explain why every tree exposes each swapped bridge endpoint, why relabeling preserves the spectrum, and how the written Poincare comparison supplies a constant gap for the enlarged family.

**Story role:** Introduce the specific family used to test whether the upper bound's vertex dependence is avoidable.

**Conceptual connection:** The output encoding matters as much in a lower bound as in a preparation theorem: actual endpoint labels reveal information that an abstract port identifier could hide.

**Source pointers:** Childs §§21.1–21.2; local [graph family](../science/lower_bound.md#1-a-constant-gap-graph-carrying-linearly-many-hidden-bits), [gap comparison](../science/lower_bound.md#2-an-explicit-constant-gap-bound), and [endpoint decoder](../science/lower_bound.md#4-a-measured-endpoint-list-reveals-the-whole-hidden-string).

<a id="m29"></a>

## M29 — From tree preparation to oracle interrogation

Phase: narrative/innovation

Prerequisites: M04, M26, M28

**Central question:** Why does recovering the gadget labels force linearly many quantum queries?

**Understanding target:** Explain the constant-query simulation of graph access by a hidden-bit oracle and the reduction from a valid tree to the entire hidden string. Follow why a $`T`$-query state contains only Fourier characters of degree at most $`T`$, limiting the dimension available for distinguishing all strings. Preserve the finite-error success guarantee through measurement and decoding.

**Story role:** Complete the lower bound and match the upper bound's vertex scaling at fixed gap.

**Conceptual connection:** Childs' query-polynomial framework becomes a self-contained information-recovery argument for this exact endpoint-output task; it does not establish optimal shrinking-gap dependence.

**Source pointers:** Childs §§21.1–21.3; [oracle simulation](../science/lower_bound.md#3-constant-query-simulation-of-the-graph-oracles); [interrogation proof](../science/lower_bound.md#5-a-self-contained-oracle-interrogation-bound); [lower-bound scope](../science/lower_bound.md#scope-and-attribution).

<a id="m30"></a>

## M30 — The established capability and its boundary

Phase: narrative/innovation

Prerequisites: M14, M22, M24, M25, M26, M27, M28, M29

**Central question:** What can the field now do under the stated promises, and which stronger conclusions do not follow?

**Understanding target:** Explain the complete route from sorted paid graph access to a clean positive endpoint-encoded spanning-tree q-sample, its reusable inverse, and the nearlinear fixed-gap vertex scaling with a matching linear query lower bound up to logarithms. State the restrictions: unweighted regular connected graphs, a known normalized-gap bound, charged oracle gates and workspace, and explicit general-gap phase compilation. Distinguish this capability from a classical-output expander speedup, universal weighted qsampling, practical crossover, or a matching gap lower bound.

**Story role:** Close the map by integrating mechanism, evidence, attribution, cost and scope into one scientific proposition.

**Conceptual connection:** Quantum walk access, polynomial transport and determinant structure produce a coherent combinatorial interface only because normalization, relative signs and every relevant record are handled together.

**Source pointers:** Childs §1.6, §§18.1–18.3, §§21.1–21.3 and §§29.1–29.3; [main theorem](../science/model.md#main-theorem), [operational interpretation](../science/interpretation.md), [related-work comparison](../references/related_work.md), and [finite verification boundaries](../verification/README.md).
