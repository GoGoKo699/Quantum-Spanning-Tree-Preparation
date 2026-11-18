# From weighted incidence to coherent trees

A spanning tree is a connected, cycle-free set of $`n-1`$ edges. Weight each tree by the product of its edge weights. The output state assigns the square root of the normalized weight as a positive amplitude to the tree's sorted endpoint list. The preparation returns its work registers to zero within the joint-state error guarantee and gives an inverse for coherent use. The [weighted theorem](weighted_preparation.md) states the exact interface, output and resources.

## Prepare the occupied vertex space

The graph enters through a coherent sorted weighted neighbor oracle and its unweighted degree oracle. First load a uniform port state at each vertex using its degree, then flag that port with amplitude proportional to the square root of its edge weight. Project onto the antisymmetric sector of port reversal and fold the two ports for each edge. With $`B`$ the oriented incidence matrix, $`D`$ the unweighted degree diagonal and $`W`$ the edge-weight diagonal, the folded block is

```math
A=\frac{W^{1/2}B D^{-1/2}}{\sqrt{2w_{\max}}}.
```

Connectivity makes $`D^{1/2}\mathbf 1`$, after normalization, the sole missing vertex direction. A single degree-rooted state specifies it. Mapping that state to the signed list of all vertices except the selected one gives the antisymmetric state of the occupied complement. The supplied lower bound $`\gamma`$ on either normalized-Laplacian gap yields a nonzero singular-value bound of $`\sqrt{\gamma/(2\kappa)}`$. Polar singular-value transformation then transports the occupied modes isometrically to the weighted incidence image. [Block construction and occupied state](weighted_preparation.md).

In the [regular unweighted specialization](model.md), the vertex state is uniform and the coin has the same size at every vertex. The projected-unitary identity reduces to $`A^\dagger A=(I-P)/2`$ for simple random walk $`P`$. [Regular polar transport](polar_transport.md).

## Convert determinants to positive tree amplitudes

Transport the antisymmetric input and sort its edge registers coherently. The amplitude of each ordered edge subset is a minor of an orthonormal basis for the incidence image. Removing a fixed root column from the incidence matrix yields another basis for the same image after edge weighting. The determinant of that basis change is common to all subsets.

Non-trees have zero incidence determinant. Every spanning tree has a reduced unweighted incidence determinant of magnitude one. The weight factors from its selected rows therefore give the square root of the product of its edge weights. The matrix-tree identity gives the common normalization. The graph-independent permutation resource from the [clean coherent preparation](coherent_preparation.md) works on the weighted state by linearity.

Root the tree at the fixed vertex. Each edge has one child endpoint. The incidence sign is the parity of the permutation that orders edges by their child labels, multiplied by the signs of their child incidence entries. Euler-tour list ranking finds those children through sorting-network joins. Compute the sign, apply its phase and reverse the computation. [Reversible sign cleanup](sign_cleanup.md) and [four-cycle example](interpretation.md#four-cycle-worked-example).

## Account for accuracy and query cost

The polar approximation controls the full unitary output, including leakage outside the desired signal registers. The error of transporting the occupied modes adds to the errors in input preparation, fixed-angle synthesis and the other reversible steps. The [weighted resource account](weighted_preparation.md) charges sorted weighted oracle calls, full-state precision and compilation. The [regular resource account](resources.md) records the costs with a supplied rotation circuit and its conversion from sorted lists.

The [dense weighted lower bound](weight_contrast_lower_bound.md) varies optional row-edge boosts inside a fixed topology while keeping both normalized gaps bounded below. A single boosted edge changes its inclusion probability by a constant. Independent rows give a quantum adversary bound of $`\Omega(n\sqrt{\kappa})`$. Coupling classical runs on inputs differing in one queried weight gives an expected $`\Omega(n\kappa)`$ lower bound. The quantum construction matches the first bound up to logarithms at fixed gap. The [unweighted cubic lower bound](lower_bound.md) separately forces a linear vertex term via hidden bridge labels.

The [related-work account](../references/related_work.md) compares one-sample and amortized query costs, classical tree sampling and explicit-matrix determinant preparation.
