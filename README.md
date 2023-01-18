# Interesting OEIS programs invented automatically

We follow the approach used in https://arxiv.org/abs/2202.11908 , using neural machine translation (NMT) for program generation.

## Table of Contents

- [Number of Hamiltonian paths in the n-Bruhat graph.](#number-of-hamiltonian-paths-in-the-n-bruhat-graph)
- [a(n) = U(2*n, n), where U(n, x) is the Chebyshev polynomial of the second kind.](#an--u2n-n-where-un-x-is-the-chebyshev-polynomial-of-the-second-kind)
- [Greatest integer k such that k/2^n &lt; 1/e.](#greatest-integer-k-such-that-k2n--1e)
- [Crystal ball sequence for 6-dimensional cubic lattice.](#crystal-ball-sequence-for-6-dimensional-cubic-lattice)
- [Molien series for A_5.](#molien-series-for-a_5)
- [Multiplicative with a(n) = n if n is odd and a(2^s)=2.](#multiplicative-with-an--n-if-n-is-odd-and-a2s2)
- [Coordination sequence Gal.6.199.4 where G.u.t.v denotes the coordination sequence for a vertex of type v in tiling number t in the Galebach list of u-uniform tilings](#coordination-sequence-gal61994-where-gutv-denotes-the-coordination-sequence-for-a-vertex-of-type-v-in-tiling-number-t-in-the-galebach-list-of-u-uniform-tilings)
- [Coordination sequence Gal.6.129.2 where G.u.t.v denotes the coordination sequence for a vertex of type v in tiling number t in the Galebach list of u-uniform tilings.](#coordination-sequence-gal61292-where-gutv-denotes-the-coordination-sequence-for-a-vertex-of-type-v-in-tiling-number-t-in-the-galebach-list-of-u-uniform-tilings)
- [Coordination sequence Gal.6.623.2 where G.u.t.v denotes the coordination sequence for a vertex of type v in tiling number t in the Galebach list of u-uniform tilings.](#coordination-sequence-gal66232-where-gutv-denotes-the-coordination-sequence-for-a-vertex-of-type-v-in-tiling-number-t-in-the-galebach-list-of-u-uniform-tilings)
- [Coordination sequence Gal.5.302.5 where G.u.t.v denotes the coordination sequence for a vertex of type v in tiling number t in the Galebach list of u-uniform tilings.](#coordination-sequence-gal53025-where-gutv-denotes-the-coordination-sequence-for-a-vertex-of-type-v-in-tiling-number-t-in-the-galebach-list-of-u-uniform-tilings)
- [OEIS writing backwards](#oeis-writing-backwards)
- [Sum of first n primes whose indices are primes.](#sum-of-first-n-primes-whose-indices-are-primes)
- [Primes such that the previous two primes are a twin prime pair.](#primes-such-that-the-previous-two-primes-are-a-twin-prime-pair)
- [Sums of successive twin primes of order 2.](#sums-of-successive-twin-primes-of-order-2)
- [Primes p such that 2p+1 is composite.](#primes-p-such-that-2p1-is-composite)
- [Total number of OFF (white) cells after n iterations of the "Rule 111" elementary cellular automaton starting with a single ON (black) cell.](#total-number-of-off-white-cells-after-n-iterations-of-the-rule-111-elementary-cellular-automaton-starting-with-a-single-on-black-cell)
- [Number of active (ON,black) cells at stage 2^n-1 of the two-dimensional cellular automaton defined by "Rule 659", based on the 5-celled von Neumann neighborhood.](#number-of-active-onblack-cells-at-stage-2n-1-of-the-two-dimensional-cellular-automaton-defined-by-rule-659-based-on-the-5-celled-von-neumann-neighborhood)
- [Number of cubefree numbers &lt;= n.](#number-of-cubefree-numbers--n)
- [Denominators of continued fraction convergents to sqrt(895).](#denominators-of-continued-fraction-convergents-to-sqrt895)
- [Start with Pascal's triangle; form a rhombus by sliding down n steps from top on both sides then sliding down inwards to complete the rhombus and then deleting the inner numbers; a(n) = sum of entries on perimeter of rhombus.](#start-with-pascals-triangle-form-a-rhombus-by-sliding-down-n-steps-from-top-on-both-sides-then-sliding-down-inwards-to-complete-the-rhombus-and-then-deleting-the-inner-numbers-an--sum-of-entries-on-perimeter-of-rhombus)
- [Nearest integer to Gamma(n + 3/8)/Gamma(3/8).](#nearest-integer-to-gamman--38gamma38)
- [Figurate numbers based on the 10-dimensional regular convex polytope called the 10-dimensional cross-polytope, or 10-dimensional hyperoctahedron, which is represented by the Schlaefli symbol {3, 3, 3, 3, 3, 3, 3, 3, 4}. It is the dual of the 10-dimensional hypercube.](#figurate-numbers-based-on-the-10-dimensional-regular-convex-polytope-called-the-10-dimensional-cross-polytope-or-10-dimensional-hyperoctahedron-which-is-represented-by-the-schlaefli-symbol-3-3-3-3-3-3-3-3-4-it-is-the-dual-of-the-10-dimensional-hypercube)
- [Fibonacci 14-step numbers, a(n) = a(n-1) + a(n-2) + ... + a(n-14).](#fibonacci-14-step-numbers-an--an-1--an-2----an-14)
- [Molien series for Weyl group E_7.](#molien-series-for-weyl-group-e_7)
- [8-step Fibonacci sequence starting with 0,0,0,0,0,0,1,0.](#8-step-fibonacci-sequence-starting-with-00000010)
- [Poincaré series [or Poincare series] P(T_{3,2}; x).](#poincaré-series-or-poincare-series-pt_32-x)
- [Octanacci numbers: a(0)=a(1)=...=a(6)=0, a(7)=1; for n &gt;= 8, a(n) = Sum_{i=1..8} a(n-i).](#octanacci-numbers-a0a1a60-a71-for-n--8-an--sum_i18-an-i)
- [Product of prime(n) primes starting from prime(n).](#product-of-primen-primes-starting-from-primen)
- [Next larger integer with same binary weight (number of 1 bits) as n.](#next-larger-integer-with-same-binary-weight-number-of-1-bits-as-n)
- [a(n) = 1^n + 2^n + ... + 6^n.](#an--1n--2n----6n)
- [Coordination sequence for C_4 lattice.](#coordination-sequence-for-c_4-lattice)
- [Number of perfect matchings on n edges which represent RNA secondary folding structures characterized by the Lyngso and Pedersen (L&amp;P) family and the Cao and Chen (C&amp;C) family.](#number-of-perfect-matchings-on-n-edges-which-represent-rna-secondary-folding-structures-characterized-by-the-lyngso-and-pedersen-lp-family-and-the-cao-and-chen-cc-family)
- [Determinant of inverse Hilbert matrix.](#determinant-of-inverse-hilbert-matrix)
- [Fibbinary numbers: if n = F(i1) + F(i2) + ... + F(ik) is the Zeckendorf representation of n (i.e., write n in Fibonacci number system) then a(n) = 2^(i1 - 2) + 2^(i2 - 2) + ... + 2^(ik - 2). Also numbers whose binary representation contains no two adjacent 1's.](#fibbinary-numbers-if-n--fi1--fi2----fik-is-the-zeckendorf-representation-of-n-ie-write-n-in-fibonacci-number-system-then-an--2i1---2--2i2---2----2ik---2-also-numbers-whose-binary-representation-contains-no-two-adjacent-1s)
- [Nimsum n + 16.](#nimsum-n--16)
- [Cumulative product of all divisors of 1..n.](#cumulative-product-of-all-divisors-of-1n)
- [Bessel polynomial y_n(-2).](#bessel-polynomial-y_n-2)
- [a(n) = [ tau * a(n-1) ] + [ tau * a(n-2) ].](#an---tau--an-1----tau--an-2-)
- [Divide odd numbers into groups with prime(n) elements and add together.](#divide-odd-numbers-into-groups-with-primen-elements-and-add-together)
- [The smallest numbers of every class in a classification of positive numbers (see comment).](#the-smallest-numbers-of-every-class-in-a-classification-of-positive-numbers-see-comment)
- [Number of odd unitary divisors of n. d is a unitary divisor of n if d divides n and gcd(d,n/d)=1.](#number-of-odd-unitary-divisors-of-n-d-is-a-unitary-divisor-of-n-if-d-divides-n-and-gcddnd1)
- [[ exp(1/5) * n! ].](#-exp15--n-)
- [A second-order recursive sequence.](#a-second-order-recursive-sequence)
- [Smallest digit of n.](#smallest-digit-of-n)
- [Nicomachus triangle read by rows, T(n, k) = 2^(n - k) * 3^k, for 0 &lt;= k &lt;= n.](#nicomachus-triangle-read-by-rows-tn-k--2n---k--3k-for-0--k--n)
- [Number of even semiprimes strictly between prime(n) and 2 * prime(n).](#number-of-even-semiprimes-strictly-between-primen-and-2--primen)
- [Values x of the solutions (x,y) of the Diophantine equation 5*(X-Y)^4 - 4*X*Y = 0 with X &gt;= Y.](#values-x-of-the-solutions-xy-of-the-diophantine-equation-5x-y4---4xy--0-with-x--y)
- [Half-convolution of Catalan sequence A000108 with itself.](#half-convolution-of-catalan-sequence-a000108-with-itself)
- [Composite evil numbers.](#composite-evil-numbers)
- [Numbers k such that sin(k) &gt; 0 and sin(k+2) &lt; 0.](#numbers-k-such-that-sink--0-and-sink2--0)
- [a(n) is the number of edges (one-dimensional faces) in the convex polytope of real n X n doubly stochastic matrices.](#an-is-the-number-of-edges-one-dimensional-faces-in-the-convex-polytope-of-real-n-x-n-doubly-stochastic-matrices)
- [Numbers k such that cos(k) &lt; cos(k+1).](#numbers-k-such-that-cosk--cosk1)
- [Numbers that contain an odd digit.](#numbers-that-contain-an-odd-digit)
- [Expand cos x / exp x and invert nonzero coefficients.](#expand-cos-x--exp-x-and-invert-nonzero-coefficients)
- [Length of longest integral ladder that can be moved horizontally around the right angled corner where two hallway corridors of integral widths meet.](#length-of-longest-integral-ladder-that-can-be-moved-horizontally-around-the-right-angled-corner-where-two-hallway-corridors-of-integral-widths-meet)
- [Start with the symbol **|* and for each iteration replace * with **|* . This sequence is the number of *'s between each dash.](#start-with-the-symbol--and-for-each-iteration-replace--with---this-sequence-is-the-number-of-s-between-each-dash)
- [Number of triangles with perimeter n whose side lengths are even.](#number-of-triangles-with-perimeter-n-whose-side-lengths-are-even)
- [Numbers that contain a digit 0.](#numbers-that-contain-a-digit-0)
- [Characteristic function of Sophie Germain primes.](#characteristic-function-of-sophie-germain-primes)
- [Gaps between twin prime pairs.](#gaps-between-twin-prime-pairs)
- [Hypotenuses of primitive Pythagorean triangles.](#hypotenuses-of-primitive-pythagorean-triangles)
- [a(n) is the Y-coordinate of the n-th point of the Peano curve. Sequence A332380 gives X-coordinates.](#an-is-the-y-coordinate-of-the-n-th-point-of-the-peano-curve-sequence-a332380-gives-x-coordinates)
- [Fixed point reached by iterating the Kempner function A002034 starting at n.](#fixed-point-reached-by-iterating-the-kempner-function-a002034-starting-at-n)
- [Numbers k such that k^2 - k - 1 and k^2 - k + 1 are twin primes.](#numbers-k-such-that-k2---k---1-and-k2---k--1-are-twin-primes)
- [Expansion of the exponential generating function arcsin(2*x)/(2*(1-2*x)^(3/2)).](#expansion-of-the-exponential-generating-function-arcsin2x21-2x32)
- [[ exp(1/9)*n! ].](#-exp19n-)
- [Sum of the products of the smaller and larger parts of the partitions of n into two parts with the smaller part odd.](#sum-of-the-products-of-the-smaller-and-larger-parts-of-the-partitions-of-n-into-two-parts-with-the-smaller-part-odd)
- [Number of n X n matrices over GF(2) with rank n-1.](#number-of-n-x-n-matrices-over-gf2-with-rank-n-1)
- [Liouville's function L(n) = partial sums of A008836.](#liouvilles-function-ln--partial-sums-of-a008836)
- [Pascal's triangle read by rows: C(n,k) = binomial(n,k) = n!/(k!*(n-k)!), 0 &lt;= k &lt;= n.](#pascals-triangle-read-by-rows-cnk--binomialnk--nkn-k-0--k--n)
- [Liouville's function lambda(n) = (-1)^k, where k is number of primes dividing n (counted with multiplicity).](#liouvilles-function-lambdan---1k-where-k-is-number-of-primes-dividing-n-counted-with-multiplicity)
- [Molien series for invariants of finite Coxeter group A_7.](#molien-series-for-invariants-of-finite-coxeter-group-a_7)
- [Hosoya triangle of Lucas type.](#hosoya-triangle-of-lucas-type)
- [For each prime p take the sum of nonprimes &lt; p.](#for-each-prime-p-take-the-sum-of-nonprimes--p)
- [Primes p for which the continued fraction expansion of sqrt(p) does not have a 1 in the second position.](#primes-p-for-which-the-continued-fraction-expansion-of-sqrtp-does-not-have-a-1-in-the-second-position)
- [Triangle of denominators in Leibniz's Harmonic Triangle a(n,k), n &gt;= 1, 1 &lt;= k &lt;= n.](#triangle-of-denominators-in-leibnizs-harmonic-triangle-ank-n--1-1--k--n)
- [Luhn algorithm double-and-add sum of digits of n.](#luhn-algorithm-double-and-add-sum-of-digits-of-n)
- [Expansion of f(x) = f(x, -x^2) in powers of x where f(, ) is Ramanujan's general theta function.](#expansion-of-fx--fx--x2-in-powers-of-x-where-f--is-ramanujans-general-theta-function)
- [The Akiyama-Tanigawa algorithm applied to 1/(1,2,3,5,... old prime numbers). Reduced numerators of the second row.](#the-akiyama-tanigawa-algorithm-applied-to-11235-old-prime-numbers-reduced-numerators-of-the-second-row)
- [Number of steps to fixed point of "n -&gt; n/2 or (n+1)/2 until result is prime".](#number-of-steps-to-fixed-point-of-n---n2-or-n12-until-result-is-prime)
- [Squares that are not the sum of 2 nonzero squares.](#squares-that-are-not-the-sum-of-2-nonzero-squares)
- [Number of symbols in Babylonian numeral representation of n.](#number-of-symbols-in-babylonian-numeral-representation-of-n)
- [Divisors of 2^30 - 1.](#divisors-of-230---1)
- [Maximal length of rook tour on an n X n+4 board.](#maximal-length-of-rook-tour-on-an-n-x-n4-board)
- [Number of partitions of n into at most 8 parts.](#number-of-partitions-of-n-into-at-most-8-parts)
- [A Jacobsthal triangle.](#a-jacobsthal-triangle)
- [Unique monotonic sequence of nonnegative integers satisfying a(a(n)) = 3n.](#unique-monotonic-sequence-of-nonnegative-integers-satisfying-aan--3n)
- [Numbers n that are not coprime to the numerator of zeta(2*n)/(Pi^(2*n)).](#numbers-n-that-are-not-coprime-to-the-numerator-of-zeta2npi2n)
- [Molien series for invariants of finite Coxeter group A_9.](#molien-series-for-invariants-of-finite-coxeter-group-a_9)
- [Solution to Tower of Hanoi puzzle encoded in pairs with the moves (1,2),(2,3),(3,1),(2,1),(3,2),(1,3). The disks are moved from peg 1 to 2. For a tower of k disks use the first 2^k-1 number pairs.](#solution-to-tower-of-hanoi-puzzle-encoded-in-pairs-with-the-moves-122331213213-the-disks-are-moved-from-peg-1-to-2-for-a-tower-of-k-disks-use-the-first-2k-1-number-pairs)
- [Sierpiński's triangle, read by rows, starting from 1: T(n,k) = (T(n-1,k) + T(n-1,k-1)) mod 2.](#sierpińskis-triangle-read-by-rows-starting-from-1-tnk--tn-1k--tn-1k-1-mod-2)
- [a(1) = 1; if a(n-1) + n is prime then a(n) = a(n-1) + n, else a(n) = a(n-1).](#a1--1-if-an-1--n-is-prime-then-an--an-1--n-else-an--an-1)
- [Order of Burnside group B(6,n) of exponent 6 and rank n.](#order-of-burnside-group-b6n-of-exponent-6-and-rank-n)
- [a(n) is the number of unitary divisors of n (d such that d divides n, gcd(d, n/d) = 1).](#an-is-the-number-of-unitary-divisors-of-n-d-such-that-d-divides-n-gcdd-nd--1)
- [Number of partitions of n in which any two parts differ by at most 7.](#number-of-partitions-of-n-in-which-any-two-parts-differ-by-at-most-7)
- [Triangle T(n,k) of coefficients relating to Bezier curve continuity.](#triangle-tnk-of-coefficients-relating-to-bezier-curve-continuity)
- [Triangle read by rows, Sierpinski's gasket, A047999 * (1,2,4,8,...) diagonalized.](#triangle-read-by-rows-sierpinskis-gasket-a047999--1248-diagonalized)
- [A masked Pascal triangle.](#a-masked-pascal-triangle)
- [Numbers that are the sum of two powers of 12.](#numbers-that-are-the-sum-of-two-powers-of-12)
- [Central factorial numbers.](#central-factorial-numbers)
- [Number of inequivalent ways to color faces of a cube using at most n colors.](#number-of-inequivalent-ways-to-color-faces-of-a-cube-using-at-most-n-colors)
- [Number of partitions of n into at most 11 parts.](#number-of-partitions-of-n-into-at-most-11-parts)
- [The (1,2)-Pascal triangle (or Lucas triangle) read by rows.](#the-12-pascal-triangle-or-lucas-triangle-read-by-rows)
- [Rows of Fibonacci-Pascal triangle.](#rows-of-fibonacci-pascal-triangle)
- [Number of restricted 3 X 3 matrices with row and column sums n.](#number-of-restricted-3-x-3-matrices-with-row-and-column-sums-n)
- [Fermat coefficients.](#fermat-coefficients)
- [Pseudoperfect (or semiperfect) numbers n: some subset of the proper divisors of n sums to n.](#pseudoperfect-or-semiperfect-numbers-n-some-subset-of-the-proper-divisors-of-n-sums-to-n)
- [Molien series for invariants of finite Coxeter group D_10 (bisected).](#molien-series-for-invariants-of-finite-coxeter-group-d_10-bisected)
- [Orders of non-Abelian Z-groups.](#orders-of-non-abelian-z-groups)
- [Coordination sequence for A_4 lattice.](#coordination-sequence-for-a_4-lattice)
- [Determinant of the Cayley addition table of Z_{n}.](#determinant-of-the-cayley-addition-table-of-z_n)
- [Number of "sets of lists": number of partitions of {1,...,n} into any number of lists, where a list means an ordered subset.](#number-of-sets-of-lists-number-of-partitions-of-1n-into-any-number-of-lists-where-a-list-means-an-ordered-subset)
- [Dying rabbits: a(n) = a(n-1) + a(n-2) - a(n-6).](#dying-rabbits-an--an-1--an-2---an-6)
- [Number of partitions of n into at most 12 parts.](#number-of-partitions-of-n-into-at-most-12-parts)
- [Generalized Catalan numbers.](#generalized-catalan-numbers)
- [Subtrees in rooted plane trees on n nodes.](#subtrees-in-rooted-plane-trees-on-n-nodes)
- [Sums of ménage numbers.](#sums-of-ménage-numbers)
- [Number of ways to place n non-attacking bishops on a 2 X 2n board.](#number-of-ways-to-place-n-non-attacking-bishops-on-a-2-x-2n-board)
- [Motzkin numbers: number of ways of drawing any number of nonintersecting chords joining n (labeled) points on a circle.](#motzkin-numbers-number-of-ways-of-drawing-any-number-of-nonintersecting-chords-joining-n-labeled-points-on-a-circle)
- [Number of pairs of functions (f,g) from a set of n elements into itself satisfying f(x) = f(g(f(x))).](#number-of-pairs-of-functions-fg-from-a-set-of-n-elements-into-itself-satisfying-fx--fgfx)
- [Domb numbers: number of 2n-step polygons on diamond lattice.](#domb-numbers-number-of-2n-step-polygons-on-diamond-lattice)
- [Convolution of primes with themselves.](#convolution-of-primes-with-themselves)

### Number of Hamiltonian paths in the n-Bruhat graph.
https://oeis.org/A317485 : 0 1 6 4128

size 73, time 497: loop2 (x + (loop2 ((loop2 ((loop ((loop ((loop (x + x) (x div 2) 1) + x) (1 + (y div 2)) x) + x) (y - 1) y) + x) ((y - 1) - 2) (1 + (y div (1 + 2))) 0 y) + x) ((y - 2) - 2) (1 + (y div (2 + 2))) 0 y)) ((y - (2 * (2 + 2))) - 1) 2 0 x

K K K D K C G B J K D B L C G D K J K D L B E L J K D L B E C E B L B C D G D A L N K D L C E C E B L C C D G D A L N D L C C C D F E B E C A K N

```
def f5(X):
  x = 1
  for y in range (1,(X // 2) + 1):
    x = x + x
  return x

def f4(X,Y):
  x = X
  for y in range (1,(1 + (Y // 2)) + 1):
    x = f5(x) + x
  return x

def f3(X,Y):
  x = Y
  for y in range (1,(Y - 1) + 1):
    x = f4(x,y) + x
  return x

def f2(X,Y):
  x,y = 0, Y
  for z in range (1,(1 + (Y // (1 + 2))) + 1):
    x,y = (f3(x,y) + x), ((y - 1) - 2)
  return x

def f1(X,Y):
  x,y = 0, Y
  for z in range (1,(1 + (Y // (2 + 2))) + 1):
    x,y = (f2(x,y) + x), ((y - 2) - 2)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,2 + 1):
    x,y = (x + f1(x,y)), ((y - (2 * (2 + 2))) - 1)
  return x

for x in range(32):
  print (f0(x))
```

### a(n) = U(2\*n, n), where U(n, x) is the Chebyshev polynomial of the second kind.

https://oeis.org/A349073  

1 3 209 40391 15003009 9127651499 8254109243953 10393834843080975 17391182043967249409 37326390852372133364819 99976027392046047055178001 326887883645157139828711692503 1281398359905415379814555044995201 5932135472283024519893762690145006075

size 16, time 24577: loop2 (((x div y) * x) - y) x (x + x) 1 (x + x)

K L G K F L E K K K D B K K D N

### Greatest integer k such that k/2^n < 1/e.

https://oeis.org/A293339 

0 0 1 2 5 11 23 47 94 188 376 753 1506 3013 6027 12054 24109 48218 96437 192874 385749 771499 1542998 3085996 6171992 1
2343985 24687971 49375942 98751885 197503771 395007542 790015084 1580030168 3160060337 6320120674

size 19, time 86473: ((loop (2 * (x * y)) x 1) - 1) div (loop (1 + (x * y)) x 1)

C K L F F K B J B E B K L F D K B J G

Perhaps  a division of some variants of factorial:

```
def f1(X):
  x = 1
  for y in range (1,X + 1):
    x = 2 * (x * y)
  return x

def f2(X):
  x = 1
  for y in range (1,X + 1):
    x = 1 + (x * y)
  return x

def f0(X):
  return (f1(X) - 1) // f2(X)

for x in range(32):
  print (f0(x))
```  

### Crystal ball sequence for 6-dimensional cubic lattice.

https://oeis.org/A1848 

It invented a long program that repeats the same construction 5 times. Not sure what it is doing.

1 13 85 377 1289 3653 8989 19825 40081 75517 134245 227305 369305 579125 880685 1303777 1884961 2668525 3707509 5064793 6814249 9041957 11847485 15345233 19665841 24957661 31388293 39146185 48442297 59511829 72616013 88043969

size 86, time 427812: loop2 ((loop2 ((loop2 ((loop2 ((loop2 ((loop2 ((loop (((2 * ((x + x) + x)) div y) + x) y 1) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y) + x) (y - 1) (if x <= 0 then 1 else 2) 0 x

C K K D K D F L G K D L B J K D L B E L B C I A L N K D L B E L B C I A L N K D L B E L B C I A L N K D L B E L B C I A L N K D L B E L B C I A L N K D L B E K B C I A K N

```
def f6(X,Y):
  x = 1
  for y in range (1,Y + 1):
    x = ((2 * ((x + x) + x)) // y) + x
  return x

def f5(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f6(x,y) + x), (y - 1)
  return x

def f4(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f5(x,y) + x), (y - 1)
  return x

def f3(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f4(x,y) + x), (y - 1)
  return x

def f2(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f3(x,y) + x), (y - 1)
  return x

def f1(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f2(x,y) + x), (y - 1)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,(1 if X <= 0 else 2) + 1):
    x,y = (f1(x,y) + x), (y - 1)
  return x

for x in range(32):
  print (f0(x))
```  

### Molien series for A_5.

https://oeis.org/A008628

Not sure how hard or easy is to get the explicit formula here. We did:

https://oeis.org/A8628 : 1 1 2 3 5 7 10 13 18 23 31 38 49 60 75 91 111 132 159 187 222 258 302 348 403 461 528 599 681 767 866 969 1086 1209 1347
1492 1653 1822 2009 2205 2421 2646 2893 3151 3432 3726 4044 4376 4735 5109 5512 5931

size 57, time 212654: loop2 ((loop2 ((loop (1 + (loop (((y * y) div (2 + y)) + x) x x)) 1 (y div 2)) + x) ((y - 1) - 2) (1 + (y div (1 + 2))) 0 y)
 + x) (((y - 1) - 2) - 2) (1 + (x div (1 + (2 + 2)))) 0 x

B L L F C L D G K D K K J D B L C G J K D L B E C E B L B C D G D A L N K D L B E C E C E B K B C C D D G D A K N

```
def f3(X):
  x = X
  for y in range (1,X + 1):
    x = ((y * y) // (2 + y)) + x
  return x

def f2(X,Y):
  x = Y // 2
  for y in range (1,1 + 1):
    x = 1 + f3(x)
  return x

def f1(X,Y):
  x,y = 0, Y
  for z in range (1,(1 + (Y // (1 + 2))) + 1):
    x,y = (f2(x,y) + x), ((y - 1) - 2)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,(1 + (X // (1 + (2 + 2)))) + 1):
    x,y = (f1(x,y) + x), (((y - 1) - 2) - 2)
  return x

for x in range(32):
  print (f0(x))
```  

### Multiplicative with a(n) = n if n is odd and a(2^s)=2.

https://oeis.org/A259445 

1 2 3 2 5 6 7 2 9 10 11 6 13 14 15 2 17 18 19 10 21 22 23 6 25 26 27 14 29 30 31 2 33 34 35 18 37 38 39 10 41 42 43 22 45 46 47 6 49 50 51 26 53 54 55 14 57 58 59 30 61 62 63 2 65 66 67 34

size 77, time 2612: loop (x + x) (x mod 2) (1 + (loop (loop (loop (loop (loop (loop (loop (loop (loop (loop (loop (loop (loop (x div 2) (x mod 2) x) (2 + 2) x) (x mod 2) x) 1 (x div 2)) (x mod 2) x) 1 (x div 2)) (x mod 2) x) 1 (x div 2)) (x mod 2) x) 1 (x div 2)) (x mod 2) x) 1 (x div 2)) (x mod 2) x))

K K D K C H B K C G K C H K J C C D K J K C H K J B K C G J K C H K J B K C G J K C H K J B K C G J K C H K J B K C G J K C H K J B K C G J K C H K J D J

size 15, time 41344: loop (x div (if (x mod (2 + 2)) <= 0 then 2 else 1)) x (1 + x)
K K C C D H C B I G K B K D J

### Coordination sequence Gal.6.199.4 where G.u.t.v denotes the coordination sequence for a vertex of type v in tiling number t in the Galebach list of u-uniform tilings

https://oeis.org/A314106 .

From the description it's not clear if OEIS knows the program. (They do have the explicit formula e.g. for this similar sequence: https://oeis.org/A301298 ). 

Here is the program:

https://oeis.org/A314106 : 1 5 11 16 21 25 31 35 40 45 51 56 61 67 72 77 81 87 91 96 101 107 112 117 123 128 133 137 143 147 152 157 163 168 173 179 184 189 193 199 203 208 213 219 224 229 235 240 245 249

size 58, time 4100: (if x <= 0 then 1 else (loop ((loop ((((((x div 2) div 2) mod 2) + x) div 2) + x) 1 ((1 - x) div (1 + 2))) + x) 1 ((((1 + (2 + (2 + (x + x)))) div (1 + (2 + (2 * (2 + 2))))) + x) + x))) + (2 * (x + x))

K B K C G C G C H K D C G K D B B K E B C D G J K D B B C C K K D D D D B C C C C D F D D G K D K D J I C K K D F D

```
def f2(X):
  x = (1 - X) // (1 + 2)
  for y in range (1,1 + 1):
    x = (((((x // 2) // 2) % 2) + x) // 2) + x
  return x

def f1(X):
  x = (((1 + (2 + (2 + (X + X)))) // (1 + (2 + (2 * (2 + 2))))) + X) + X
  for y in range (1,1 + 1):
    x = f2(x) + x
  return x

def f0(X):
  return (1 if X <= 0 else f1(X)) + (2 * (X + X))

for x in range(32):
  print (f0(x))
```  


### Coordination sequence Gal.6.129.2 where G.u.t.v denotes the coordination sequence for a vertex of type v in tiling number t in the Galebach list of u-uniform tilings.

https://oeis.org/A311889 : 1 4 8 13 17 21 27 31 35 40 44 48 52 56 61 65 69 75 79 83 88 92 96 100 104 109 113 117 123 127 131 136 140 144 148 152 1 57 161 165 171 175 179 184 188 192 196 200 205 209 213

size 56, time 4200: (if x <= 0 then 1 else (loop (loop (((((x div 2) mod (1 + 2)) - x) div (1 + 2)) + x) 1 ((((x div 2) mod 2) + x) div 2)) 1 (((1 + (2 + (2 + x))) div (1 + (2 + (2 * (2 + 2))))) + x))) + (2 * (x + x))

K B K C G B C D H K E B C D G K D B K C G C H K D C G J B B C C K D D D B C C C C D F D D G K D J I C K K D F D

### Coordination sequence Gal.6.623.2 where G.u.t.v denotes the coordination sequence for a vertex of type v in tiling number t in the Galebach list of u-uniform tilings.

https://oeis.org/A315334 : 1 6 10 16 22 27 33 38 44 50 54 60 66 70 76 82 87 93 98 104 110 114 120 126 130 136 142 147 153 158 164 170 174 180 186 190 196 202 207 213 218 224 230 234 240 246 250 256 262 267

size 55, time 10265: (((2 * (x + x)) - (loop (loop (loop (((1 + (y div 2)) mod 2) + x) x x) 1 ((1 + x) div (1 + 2))) 1 (((1 + (2 + (2 + x))) div (1 + (2 + (2 * (2 + 2))))) + x))) + (if x <= 0 then 1 else x)) + x

C K K D F B L C G D C H K D K K J B B K D B C D G J B B C C K D D D B C C C C D F D D G K D J E K B K I D K D

### Coordination sequence Gal.5.302.5 where G.u.t.v denotes the coordination sequence for a vertex of type v in tiling number t in the Galebach list of u-uniform tilings.

https://oeis.org/A315742 

1 6 12 18 23 28 33 38 44 50 56 62 68 74 79 84 89 94 100 106 112 118 124 130 135 140 145 150 156 162 168 174 180 186 191 196 201 206 212 218 224 230 236 242 247 252 257 262 268 274

size 52, time 3800: ((((((((x div 2) + x) mod (1 + (2 + 2))) - x) div (1 + (2 + 2))) + (2 * (x + x))) - ((((2 - (x div 2)) mod (1 + (2 + 2))) + x) div (1 + (2 + 2)))) + (if x <= 0 then 1 else x)) + x

K C G K D B C C D D H K E B C C D D G C K K D F D C K C G E B C C D D H K D B C C D D G E K B K I D K D

### OEIS writing backwards 
In the iteration done on <2022-10-19> this was exploited in several newly invented programs:

https://oeis.org/A71587
https://oeis.org/A071586
https://oeis.org/A004165

Code for the last one: L B C C C C D F D I K F L C C C C D F D H D L C G B C C D D G B K D A K K F K F B B K D J N

The python code for the last one:
```
def f1(X):
  x = 1 + X
  for y in range (1,1 + 1):
    x = (x * x) * x
  return x

def f0(X):
  x,y = 0, f1(X)
  for z in range (1,(1 + X) + 1):
    x,y = (((1 if y <= 0 else (2 + (2 * (2 + 2)))) * x) + (y % (2 + (2 * (2 + 2))))), ((y // 2) // (1 + (2 + 2)))
  return x

for x in range(32):
  print (f0(x))
```

### Sum of first n primes whose indices are primes.

https://oeis.org/A83186 : 3 8 19 36 67 108 167 234 317 426 553 710 889 1080 1291 1532 1809 2092 2423 2776 3143 3544 3975 4436 4945 5492 6055 6642 
7241 7858 8567 9306 10079 10876 11735 12612 13531 14498 15489 16520 17583 18670 19823

size 69, time 2302265: loop ((loop (1 + (compr (x - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) (1 +
 x))) 1 (compr (x - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) (1 + y))) + x) x (1 + 2)
 
B K K B L D H C K I C K C C C C D D F G D B K D J E B K D M D B K K B L D H C K I C K C C C C D D F G D B K D J E B L D M J K D K B C D J

size 67, time 2304759: loop ((loop (1 + (compr (x - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) (1 +
 x))) 1 (compr (x - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) y)) + x) (1 + x) 0
 
B K K B L D H C K I C K C C C C D D F G D B K D J E B K D M D B K K B L D H C K I C K C C C C D D F G D B K D J E L M J K D B K D A J

```
def f3(X):
  x = 1 + X
  for y in range (1,(2 + (X // (2 * (2 + (2 + 2))))) + 1):
    x = 2 if (x % (1 + y)) <= 0 else x
  return x

def f2(X):
  x,i = 0,0
  while i <= 1 + X:
    if (x - f3(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f5(X):
  x = 1 + X
  for y in range (1,(2 + (X // (2 * (2 + (2 + 2))))) + 1):
    x = 2 if (x % (1 + y)) <= 0 else x
  return x

def f4(X,Y):
  x,i = 0,0
  while i <= 1 + Y:
    if (x - f5(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f1(X,Y):
  x = f4(X,Y)
  for y in range (1,1 + 1):
    x = 1 + f2(x)
  return x

def f0(X):
  x = 1 + 2
  for y in range (1,X + 1):
    x = f1(x,y) + x
  return x

for x in range(32):
  print (f0(x))
```

### Primes such that the previous two primes are a twin prime pair.

https://oeis.org/A88176 : 7 11 17 23 37 47 67 79 107 113 149 157 191 197 211 233 251 277 293 317 353 431 439 467 541 577 607 631 647 673 821 827 8
39 863 887 1031 1039 1061 1069 1097 1163 1237 1283 1297 1307 1327 1433 1459 1487 1493 1613

size 63, time 3431714: loop (loop2 (loop ((if (x mod (1 + y)) <= 0 then 1 else 0) + x) y x) (y div 2) x 2 x) 1 (2 + (compr ((loop (if (((2 + x) * 
x) mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (1 + (2 + (2 * (2 + 2)))))) (1 + x)) mod (1 + x)) (2 + x)))

K B L D H B A I K D L K J L C G K C K N B C C K D K F B L D H B L D K I C K B C C C C D F D D G D B K D J B K D H C K D M D J

```
def f2(X,Y):
  x = X
  for y in range (1,Y + 1):
    x = (1 if (x % (1 + y)) <= 0 else 0) + x
  return x

def f1(X):
  x,y = 2, X
  for z in range (1,X + 1):
    x,y = f2(x,y), (y // 2)
  return x

def f4(X):
  x = 1 + X
  for y in range (1,(2 + (X // (1 + (2 + (2 * (2 + 2)))))) + 1):
    x = (1 + y) if (((2 + x) * x) % (1 + y)) <= 0 else x
  return x

def f3(X):
  x,i = 0,0
  while i <= 2 + X:
    if (f4(x) % (1 + x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  x = 2 + f3(X)
  for y in range (1,1 + 1):
    x = f1(x)
  return x

for x in range(32):
  print (f0(x))
```

### Sums of successive twin primes of order 2.

https://oeis.org/A96282 : 18 22 30 42 54 66 84 108 132 156 186 222 252 276 318 378 414 426 462 522 564 588 630 690 732 756 774 786 822 882 924 948
 990 1050 1092 1116 1158 1218 1284 1356 1464 1608 1692 1716 1758 1818 1908 2028 2136 2232
 
size 54, time 3958844: loop2 (x + (loop2 ((loop (compr (1 - (loop (if (((2 - x) * x) mod (1 + y)) <= 0 then 0 else x) (1 + (x div (1 + (2 + 2)))) 
(1 + x))) (2 + x)) 1 (y div 2)) + x) (1 + y) 2 0 y)) (1 + y) 2 0 x

K B C K E K F B L D H A K I B K B C C D D G D B K D J E C K D M B L C G J K D B L D C A L N D B L D C A K N

```
def f4(X):
  x = 1 + X
  for y in range (1,(1 + (X // (1 + (2 + 2)))) + 1):
    x = 0 if (((2 - x) * x) % (1 + y)) <= 0 else x
  return x

def f3(X):
  x,i = 0,0
  while i <= 2 + X:
    if (1 - f4(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f2(X,Y):
  x = Y // 2
  for y in range (1,1 + 1):
    x = f3(x)
  return x

def f1(X,Y):
  x,y = 0, Y
  for z in range (1,2 + 1):
    x,y = (f2(x,y) + x), (1 + y)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,2 + 1):
    x,y = (x + f1(x,y)), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```

### Primes p such that 2p+1 is composite.

https://oeis.org/A53176 : 7 13 17 19 31 37 43 47 59 61 67 71 73 79 97 101 103 107 109 127 137 139 149 151 157 163 167 181 193 197 199 211 223 227 
229 241 257 263 269 271 277 283 307 311 313 317 331 337 347 349 353 367 373 379 383

size 54, time 702799: compr (((if ((loop (if (((x - 1) + x) mod (1 + y)) <= 0 then 2 else x) (2 + (x div (1 + (2 + 2)))) (1 + x)) mod (1 + x)) <= 
0 then 2 else 1) + (loop (if (x mod (1 + y)) <= 0 then 1 else x) (x div 2) x)) mod (1 + x)) (2 + x)

K B E K D B L D H C K I C K B C C D D G D B K D J B K D H C B I K B L D H B K I K C G K J D B K D H C K D M

size 59, time 292162: compr ((loop ((if ((loop (if (((x - 1) + x) mod (1 + y)) <= 0 then 2 else x) (2 + (x div (1 + (2 + 2)))) (1 + x)) mod (1 + x
)) <= 0 then 0 else 1) + x) 1 (loop (if (x mod (1 + y)) <= 0 then 2 else x) (x div (2 + 2)) x)) mod (1 + x)) (1 + x)

K B E K D B L D H C K I C K B C C D D G D B K D J B K D H A B I K D B K B L D H C K I K C C D G K J J B K D H B K D M

```
def f2(X):
  x = 1 + X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = 2 if (((x - 1) + x) % (1 + y)) <= 0 else x
  return x

def f3(X):
  x = X
  for y in range (1,(X // (2 + 2)) + 1):
    x = 2 if (x % (1 + y)) <= 0 else x
  return x

def f1(X):
  x = f3(X)
  for y in range (1,1 + 1):
    x = (0 if (f2(x) % (1 + x)) <= 0 else 1) + x
  return x

def f0(X):
  x,i = 0,0
  while i <= 1 + X:
    if (f1(x) % (1 + x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

for x in range(32):
  print (f0(x))
```

### Total number of OFF (white) cells after n iterations of the "Rule 111" elementary cellular automaton starting with a single ON (black) cell.

https://oeis.org/A267262 : 0 1 3 5 9 13 20 24 35 39 54 58 77 81 104 108 135 139 170 174 209 213 252 256 299 303 350 354 405 409 464 468 527 531 59
4 598 665 669 740 744 819 823 902 906 989 993 1080 1084 1175 1179 1274 1278 1377 1381

size 18, time 27351: loop (((y * y) - x) - ((x * y) div (1 + (x + y)))) x 0

L L F K E K L F B K L D D G E K A J

```
def f0(X):
  x = 0
  for y in range (1,X + 1):
    x = ((y * y) - x) - ((x * y) // (1 + (x + y)))
  return x

for x in range(32):
  print (f0(x))
```

### Number of active (ON,black) cells at stage 2^n-1 of the two-dimensional cellular automaton defined by "Rule 659", based on the 5-celled von Neumann neighborhood.

https://oeis.org/A273385 : 1 5 49 225 961 3969 16129 65025 261121 1046529 4190209 16769025 67092481 268402689 1073676289 4294836225

size 22, time 611: loop (x - (x div 2)) (2 - x) (loop (x * x) 1 ((loop (x + x) x 2) - 1))

K K C G E C K E K K F B K K D K C J B E J J

```
def f2(X):
  x = 2
  for y in range (1,X + 1):
    x = x + x
  return x

def f1(X):
  x = f2(X) - 1
  for y in range (1,1 + 1):
    x = x * x
  return x

def f0(X):
  x = f1(X)
  for y in range (1,(2 - X) + 1):
    x = x - (x // 2)
  return x

for x in range(32):
  print (f0(x))
```

### Number of cubefree numbers <= n.

https://oeis.org/A60431 : 1 2 3 4 5 6 7 7 8 9 10 11 12 13 14 14 15 16 17 18 19 20 21 21 22 23 23 24 25 26 27 27 28 29 30 31 32 33 34 34 35 36 37 3
8 39 40 41 41 42 43 44 45 46 46 47 47 48 49 50 51 52 53 54 54 55 56 57 58 59 60 61 61

size 19, time 285749: loop (x - ((x div (loop (x + x) y 2)) div (1 + y))) x (1 + x)

K K K K D L C J G B L D G E K B K D J

```
def f1(X,Y):
  x = 2
  for y in range (1,Y + 1):
    x = x + x
  return x

def f0(X):
  x = 1 + X
  for y in range (1,X + 1):
    x = x - ((x // f1(x,y)) // (1 + y))
  return x

for x in range(32):
  print (f0(x))
```

### Denominators of continued fraction convergents to sqrt(895).

https://oeis.org/A42731 : 1 1 11 12 707 719 7897 8616 507625 516241 5670035 6186276 364474043 370660319 4071077233 4441737552 261691855249 2661335
92801 2923027783259 3189161376060 187894387594739 191083548970799 2098729877302729 2289813426273528

size 45, time 10166: (if x <= 0 then 1 else (loop2 ((((if (x mod 2) <= 0 then (2 + 2) else 1) * ((if (x mod (2 + 2)) <= 0 then (1 + (2 + (2 + 2))) else 1) * x)) + x) + y) x (x - 1) 2 1)) div (1 + (x mod 2))
 
K B K C H C C D B I K C C D H B C C C D D D B I K F F K D L D K K B E C B N I B K C H D G

size 40, time 11076: (loop2 (((if (x mod 2) <= 0 then ((2 * ((1 + 2) * (loop 1 (x mod (2 + 2)) (1 + (2 + 2))))) - 1) else 2) * x) + y) x x 1 0) div (1 + (x mod 2))

K C H C B C D B K C C D H B C C D D J F F B E C I K F L D K K B A N B K C H D G

```
def f1(X):
  x,y = 2, 1
  for z in range (1,(X - 1) + 1):
    x,y = (((((2 + 2) if (x % 2) <= 0 else 1) * (((1 + (2 + (2 + 2))) if (x % (2 + 2)) <= 0 else 1) * x)) + x) + y), x
  return x

def f0(X):
  return (1 if X <= 0 else f1(X)) // (1 + (X % 2))

for x in range(32):
  print (f0(x))

```

### Start with Pascal's triangle; form a rhombus by sliding down n steps from top on both sides then sliding down inwards to complete the rhombus and then deleting the inner numbers; a(n) = sum of entries on perimeter of rhombus.

https://oeis.org/A81495 : 1 5 17 55 189 681 2519 9451 35765 136153 520695 1998745 7696467 29716025 115000947 445962899 1732525861 6741529113 26270
128535 102501265057 400411345659 1565841089321 6129331763923 24014172955545 94163002754699 369507926510401

size 43, time 9412: ((loop (2 * (((x div y) + x) + x)) x 1) div (1 + x)) + ((((loop (2 * ((x - (x div y)) + x)) x x) div (1 + x)) + ((x * x) div (1 + x))) + x)

C K L G K D K D F K B J B K D G C K K L G E K D F K K J B K D G K K F B K D G D K D D

```
def f1(X):
  x = 1
  for y in range (1,X + 1):
    x = 2 * (((x // y) + x) + x)
  return x

def f2(X):
  x = X
  for y in range (1,X + 1):
    x = 2 * ((x - (x // y)) + x)
  return x

def f0(X):
  return (f1(X) // (1 + X)) + (((f2(X) // (1 + X)) + ((X * X) // (1 + X))) + X)

for x in range(32):
  print (f0(x))
```

### Nearest integer to Gamma(n + 3/8)/Gamma(3/8).

https://oeis.org/A20027 : 1 0 1 1 4 18 97 620 4570 38270 358778 3722325 42341447 523975411 7008171125 100742459918 1548915321246 25363488385399 44
0690610696307 8097689971544645 156892743198677493 3196689642673053919

size 35, time 40812: loop ((((0 - 1) mod (1 + (2 + 2))) + x) div (2 * (2 + 2))) x (loop2 (x * y) ((2 * (2 + 2)) + y) x 1 (1 + 2))

A B E B C C D D H K D C C C D F G K K L F C C C D F L D K B B C D N J

```
def f1(X):
  x,y = 1, 1 + 2
  for z in range (1,X + 1):
    x,y = (x * y), ((2 * (2 + 2)) + y)
  return x

def f0(X):
  x = f1(X)
  for y in range (1,X + 1):
    x = (((0 - 1) % (1 + (2 + 2))) + x) // (2 * (2 + 2))
  return x

for x in range(32):
  print (f0(x))
```

### Figurate numbers based on the 10-dimensional regular convex polytope called the 10-dimensional cross-polytope, or 10-dimensional hyperoctahedron, which is represented by the Schlaefli symbol {3, 3, 3, 3, 3, 3, 3, 3, 4}. It is the dual of the 10-dimensional hypercube.	

https://oeis.org/A99197 : 0 1 20 201 1360 7001 29364 104881 329024 927441 2390004 5707449 12767184 26986089 54284244 104535009 193664256 346615329 601446996 1014889769 1669752016 2684641785 4226553716 6526963345 9902174016 14778775025 21725194036 31490462745

size 128, time 2351264: loop2 (x + (loop2 (x + (loop2 ((loop2 ((loop2 ((loop2 ((loop2 ((loop2 ((loop2 ((loop (((2 * ((2 * (x + x)) + x)) div y) + x) y 1) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y)) (y - 1) (if y <= 0 then 1 else 2) 0 y)) (y - 1) (if (x - 1) <= 0 then x else 2) 0 (x - 1)

K K C C K K D F K D F L G K D L B J K D L B E L B C I A L N K D L B E L B C I A L N K D L B E L B C I A L N K D L B E L B C I A L N K D L B E L B C I A L N K D L B E L B C I A L N K D L B E L B C I A L N D L B E L B C I A L N D L B E K B E K C I A K B E N

```
def f9(X,Y):
  x = 1
  for y in range (1,Y + 1):
    x = ((2 * ((2 * (x + x)) + x)) // y) + x
  return x

def f8(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f9(x,y) + x), (y - 1)
  return x

def f7(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f8(x,y) + x), (y - 1)
  return x

def f6(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f7(x,y) + x), (y - 1)
  return x

def f5(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f6(x,y) + x), (y - 1)
  return x

def f4(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f5(x,y) + x), (y - 1)
  return x

def f3(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f4(x,y) + x), (y - 1)
  return x

def f2(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f3(x,y) + x), (y - 1)
  return x

def f1(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (x + f2(x,y)), (y - 1)
  return x

def f0(X):
  x,y = 0, X - 1
  for z in range (1,(X if (X - 1) <= 0 else 2) + 1):
    x,y = (x + f1(x,y)), (y - 1)
  return x

for x in range(32):
  print (f0(x))
```

### Fibonacci 14-step numbers, a(n) = a(n-1) + a(n-2) + ... + a(n-14).

https://oeis.org/A220469 : 1 1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16383 32765 65528 131052 262096 524176 1048320 2096576 4193024 8385792 16771072 33541120 67080192 134156288 268304384 536592385 1073152005 2146238482 4292345912 8584429728

size 108, time 86457: loop2 (1 + ((((((((((((((((((((((((((((((((((((y * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y)) (x + y) (x - 1) 1 1

B L L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D D K L D K B E B B N

size 106, time 91487: loop2 (1 + ((((((((((((((((((((((((((((((((((((y * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y)) (x + y) x 1 0

B L L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D D K L D K B A N

```
def f0(X):
  x,y = 1, 1
  for z in range (1,(X - 1) + 1):
    x,y = (1 + ((((((((((((((((((((((((((((((((((((y * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y)), (x + y)
  return x

for x in range(32):
  print (f0(x))
```

### Molien series for Weyl group E_7.

https://oeis.org/A8583 : 1 1 1 2 3 4 6 8 10 14 18 22 29 36 44 55 67 80 98 117 138 165 194 226 266 309 356 413 475 542 622 708 802 911 1029 1157 1304 1462 1633 1827 2036 2261 2514 2785

size 106, time 232932: loop2 (x + (loop2 (x + (loop2 ((loop2 ((loop (((1 + x) * (2 + x)) div (2 + (2 + 2))) 1 (1 + (y div (1 + 2)))) + x) ((y - 2) - 2) (1 + (y div (2 + 2))) 0 y) + x) (((y - 1) - 2) - 2) (1 + (y div (1 + (2 + 2)))) 0 y)) ((((y - 1) - 2) - 2) - 2) (1 + (y div (1 + (2 + (2 + 2))))) 0 y)) (((y - 2) - 2) - 2) (1 + (x div (2 + (2 + 2)))) 0 x

K K B K D C K D F C C C D D G B B L B C D G D J K D L C E C E B L C C D G D A L N K D L B E C E C E B L B C C D D G D A L N D L B E C E C E C E B L B C C C D D D G D A L N D L C E C E C E B K C C C D D G D A K N

```
def f4(X,Y):
  x = 1 + (Y // (1 + 2))
  for y in range (1,1 + 1):
    x = ((1 + x) * (2 + x)) // (2 + (2 + 2))
  return x

def f3(X,Y):
  x,y = 0, Y
  for z in range (1,(1 + (Y // (2 + 2))) + 1):
    x,y = (f4(x,y) + x), ((y - 2) - 2)
  return x

def f2(X,Y):
  x,y = 0, Y
  for z in range (1,(1 + (Y // (1 + (2 + 2)))) + 1):
    x,y = (f3(x,y) + x), (((y - 1) - 2) - 2)
  return x

def f1(X,Y):
  x,y = 0, Y
  for z in range (1,(1 + (Y // (1 + (2 + (2 + 2))))) + 1):
    x,y = (x + f2(x,y)), ((((y - 1) - 2) - 2) - 2)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,(1 + (X // (2 + (2 + 2)))) + 1):
    x,y = (x + f1(x,y)), (((y - 2) - 2) - 2)
  return x

for x in range(32):
  print (f0(x))
```

### 8-step Fibonacci sequence starting with 0,0,0,0,0,0,1,0.	

https://oeis.org/A251672 : 0 0 0 0 0 0 1 0 1 2 4 8 16 32 64 127 254 507 1012 2020 4032 8048 16064 32064 64001 127748 254989 508966 1015912 2027792
 4047536 8079008 16125952 32187903 64248058 128241127 255973288 510930664 1019833536 2035619536
 
size 81, time 81817: loop (loop2 ((loop2 (1 + ((((((((((((((((((y * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y)) (x + y) (y - 2) (if y <= 0 then 0 else 1) 1) - x) (1 + y) 2 0 x) 1 (((x - 2) - 2) - 2)

B L L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D D K L D L C E L A B I B N K E B L D C A K N B 
K C E C E C E J

```
def f2(X,Y):
  x,y = 0 if Y <= 0 else 1, 1
  for z in range (1,(Y - 2) + 1):
    x,y = (1 + ((((((((((((((((((y * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y)), (x + y)
  return x

def f1(X):
  x,y = 0, X
  for z in range (1,2 + 1):
    x,y = (f2(x,y) - x), (1 + y)
  return x

def f0(X):
  x = ((X - 2) - 2) - 2
  for y in range (1,1 + 1):
    x = f1(x)
  return x

for x in range(32):
  print (f0(x))
```

### Poincaré series [or Poincare series] P(T_{3,2}; x).	

https://oeis.org/A124615 : 1 4 14 38 93 204 419 806 1480 2600 4411 7244 11579 18048 27528 41150 60428 87280 124203 174308 241555 330808 448140 600
918 798193 1050820 1371953 1777210 2285288 2918188 3701971 4667052 5849124 7289536 9036406 11145104

size 79, time 2500433: loop2 (x + (loop2 (x + (loop2 ((loop2 ((loop ((loop (((2 * ((x + x) + x)) div y) + x) (y div 2) 1) + x) y 1) + x) ((y - 1) - 2) (1 + (y div (1 + 2))) 0 y) + x) ((y - 1) - 2) (1 + (y div (1 + 2))) 0 y)) (y - 1) (if y <= 0 then 1 else 2) 0 y)) (y - 1) (if x <= 0 then 1 else 2) 0 x

K K C K K D K D F L G K D L C G B J K D L B J K D L B E C E B L B C D G D A L N K D L B E C E B L B C D G D A L N D L B E L B C I A L N D L B E K 
B C I A K N

```
def f5(X,Y):
  x = 1
  for y in range (1,(Y // 2) + 1):
    x = ((2 * ((x + x) + x)) // y) + x
  return x

def f4(X,Y):
  x = 1
  for y in range (1,Y + 1):
    x = f5(x,y) + x
  return x

def f3(X,Y):
  x,y = 0, Y
  for z in range (1,(1 + (Y // (1 + 2))) + 1):
    x,y = (f4(x,y) + x), ((y - 1) - 2)
  return x

def f2(X,Y):
  x,y = 0, Y
  for z in range (1,(1 + (Y // (1 + 2))) + 1):
    x,y = (f3(x,y) + x), ((y - 1) - 2)
  return x

def f1(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (x + f2(x,y)), (y - 1)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,(1 if X <= 0 else 2) + 1):
    x,y = (x + f1(x,y)), (y - 1)
  return x

for x in range(32):
  print (f0(x))
```


### Octanacci numbers: a(0)=a(1)=...=a(6)=0, a(7)=1; for n >= 8, a(n) = Sum_{i=1..8} a(n-i).	

https://oeis.org/A79262 : 0 0 0 0 0 0 0 1 1 2 4 8 16 32 64 128 255 509 1016 2028 4048 8080 16128 32192 64256 128257 256005 510994 1019960 2035872 
4063664 8111200 16190208 32316160 64504063 128752121 256993248 512966536 1023897200 2043730736

size 71, time 156913: 0 - (loop2 (((loop2 (1 + ((((((((((((((((((y * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y) * y) div (x + y)) + y)) (x + y) y 1 1) - x) - x) (1 + y) 2 0 x)

A B L L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D L F K L D G L D D K L D L B B N K E K E B L D C A K N E

```
def f2(X,Y):
  x,y = 1, 1
  for z in range (1,Y + 1):
    x,y = (1 + ((((((((((((((((((y * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y) * y) // (x + y)) + y)), (x + y)
  return x

def f1(X):
  x,y = 0, X
  for z in range (1,2 + 1):
    x,y = ((f2(x,y) - x) - x), (1 + y)
  return x

def f0(X):
  return 0 - f1(X)

for x in range(32):
  print (f0(x))
```

### Product of prime(n) primes starting from prime(n).	

https://oeis.org/A75068 : 6 105 85085 215656441 2928046583754721 50774191064678342417 8893257265710151560293840093 456136734556614681201275816106457 413876828984538288243690385880996726353717

size 70, time 41995: loop2 ((1 + (compr (x - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) (1 + y))) * x) (1 + y) (1 + (compr (x - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) (1 + x))) 1 x
 
B K K B L D H C K I C K C C C C D D F G D B K D J E B L D M D K F B L D B K K B L D H C K I C K C C C C D D F G D B K D J E B K D M D B K N

```
def f2(X):
  x = 1 + X
  for y in range (1,(2 + (X // (2 * (2 + (2 + 2))))) + 1):
    x = 2 if (x % (1 + y)) <= 0 else x
  return x

def f1(X,Y):
  x,i = 0,0
  while i <= 1 + Y:
    if (x - f2(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f4(X):
  x = 1 + X
  for y in range (1,(2 + (X // (2 * (2 + (2 + 2))))) + 1):
    x = 2 if (x % (1 + y)) <= 0 else x
  return x

def f3(X):
  x,i = 0,0
  while i <= 1 + X:
    if (x - f4(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  x,y = 1, X
  for z in range (1,(1 + f3(X)) + 1):
    x,y = ((1 + f1(x,y)) * x), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```

### Next larger integer with same binary weight (number of 1 bits) as n.	

https://oeis.org/A57168 : 2 4 5 8 6 9 11 16 10 12 13 17 14 19 23 32 18 20 21 24 22 25 27 33 26 28 29 35 30 39 47 64 34 36 37 40 38 41 43 48 42 44 
45 49 46 51 55 65 50 52 53 56 54 57 59 67 58 60 61 71 62 79 95 128 66 68 69 72 70 73 75

size 66, time 769824: loop2 ((loop2 ((loop (x + (loop2 (1 + (y mod (x + x))) y (2 + (y div (1 + (2 + 2)))) 1 (y div 2))) (y - 1) (if y <= 0 then 0
 else 1)) + x) (y div 2) (1 + (2 + (2 + (y div (2 * (2 * (2 * (2 + 2)))))))) 0 y) - x) x 2 (1 + x) x
 
K B L K K D H D L C L B C C D D G D B L C G N D L B E L A B I J K D L C G B C C L C C C C C D F F F G D D D A L N K E K C B K D K N

```
def f3(X,Y):
  x,y = 1, Y // 2
  for z in range (1,(2 + (Y // (1 + (2 + 2)))) + 1):
    x,y = (1 + (y % (x + x))), y
  return x

def f2(X,Y):
  x = 0 if Y <= 0 else 1
  for y in range (1,(Y - 1) + 1):
    x = x + f3(x,y)
  return x

def f1(X,Y):
  x,y = 0, Y
  for z in range (1,(1 + (2 + (2 + (Y // (2 * (2 * (2 * (2 + 2)))))))) + 1):
    x,y = (f2(x,y) + x), (y // 2)
  return x

def f0(X):
  x,y = 1 + X, X
  for z in range (1,2 + 1):
    x,y = (f1(x,y) - x), x
  return x

for x in range(32):
  print (f0(x))
```

### a(n) = 1^n + 2^n + ... + 6^n.


https://oeis.org/A1553 : 6 21 91 441 2275 12201 67171 376761 2142595 12313161 71340451 415998681 2438235715 14350108521 84740914531 501790686201 2
978035877635 17706908038281 105443761093411 628709267031321 3752628871164355 22418196307542441 134023513204581091

size 65, time 4565: (((1 + (loop ((x * x) + x) 1 (loop (x + x) x 1))) + (loop2 (x * y) y (x div 2) (loop (1 + 2) (x mod 2) 1) (1 + (2 * (2 + 2))))
) + (loop2 (x * y) y x 1 (1 + (2 + 2)))) + (loop2 (x * y) y x 1 (2 + (2 + 2)))

B K K F K D B K K D K B J J D K L F L K C G B C D K C H B J B C C C D F D N D K L F L K B B C C D D N D K L F L K B C C C D D N D

```
def f2(X):
  x = 1
  for y in range (1,X + 1):
    x = x + x
  return x

def f1(X):
  x = f2(X)
  for y in range (1,1 + 1):
    x = (x * x) + x
  return x

def f4(X):
  x = 1
  for y in range (1,(X % 2) + 1):
    x = 1 + 2
  return x

def f3(X):
  x,y = f4(X), 1 + (2 * (2 + 2))
  for z in range (1,(X // 2) + 1):
    x,y = (x * y), y
  return x

def f5(X):
  x,y = 1, 1 + (2 + 2)
  for z in range (1,X + 1):
    x,y = (x * y), y
  return x

def f6(X):
  x,y = 1, 2 + (2 + 2)
  for z in range (1,X + 1):
    x,y = (x * y), y
  return x

def f0(X):
  return (((1 + f1(X)) + f3(X)) + f5(X)) + f6(X)

for x in range(32):
  print (f0(x))
```

### Coordination sequence for C_4 lattice.	

https://oeis.org/A19560 : 1 32 192 608 1408 2720 4672 7392 11008 15648 21440 28512 36992 47008 58688 72160 87552 104992 124608 146528 170880 19779
2 227392 259808 295168 333600 375232 420192 468608

size 62, time 165867: loop2 (x + (loop2 (x + (loop2 ((loop2 ((loop ((((1 + 2) * x) div y) + x) y 1) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y) + x) (y - 1) (if y <= 0 then 1 else 2) 0 y)) (y - 1) (if y <= 0 then 1 else 2) 0 y)) (y - 1) (if x <= 0 then 1 else 2) 0 (x + x)

K K B C D K F L G K D L B J K D L B E L B C I A L N K D L B E L B C I A L N D L B E L B C I A L N D L B E K B C I A K K D N

```
def f4(X,Y):
  x = 1
  for y in range (1,Y + 1):
    x = (((1 + 2) * x) // y) + x
  return x

def f3(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f4(x,y) + x), (y - 1)
  return x

def f2(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (f3(x,y) + x), (y - 1)
  return x

def f1(X,Y):
  x,y = 0, Y
  for z in range (1,(1 if Y <= 0 else 2) + 1):
    x,y = (x + f2(x,y)), (y - 1)
  return x

def f0(X):
  x,y = 0, X + X
  for z in range (1,(1 if X <= 0 else 2) + 1):
    x,y = (x + f1(x,y)), (y - 1)
  return x

for x in range(32):
  print (f0(x))
```

### Number of perfect matchings on n edges which represent RNA secondary folding structures characterized by the Lyngso and Pedersen (L&P) family and the Cao and Chen (C&C) family.	

https://oeis.org/A289834 : 1 1 3 11 39 134 456 1557 5364 18674 65680 233182 834796 3010712 10929245 39904623 146451871 539972534 1999185777 742962
3640 27705320423 103636336176 388775988319 1462261313876 5513152229901 20832701135628 78884459229627

size 62, time 317700: (loop ((((1 + 2) * (x * y)) div (2 + y)) + x) x 1) + (((loop (2 * ((x - (x div y)) + x)) x 1) div (1 + x)) - (loop ((loop ((
(loop (2 * ((x - (x div y)) + x)) y 1) div (1 + y)) + x) (y - 1) 1) + x) x 1))

B C D K L F F C L D G K D K B J C K K L G E K D F K B J B K D G C K K L G E K D F L B J B L D G K D L B E B J K D K B J E D

```
def f1(X):
  x = 1
  for y in range (1,X + 1):
    x = (((1 + 2) * (x * y)) // (2 + y)) + x
  return x

def f2(X):
  x = 1
  for y in range (1,X + 1):
    x = 2 * ((x - (x // y)) + x)
  return x

def f5(X,Y):
  x = 1
  for y in range (1,Y + 1):
    x = 2 * ((x - (x // y)) + x)
  return x

def f4(X,Y):
  x = 1
  for y in range (1,(Y - 1) + 1):
    x = (f5(x,y) // (1 + y)) + x
  return x

def f3(X):
  x = 1
  for y in range (1,X + 1):
    x = f4(x,y) + x
  return x

def f0(X):
  return f1(X) + ((f2(X) // (1 + X)) - f3(X))

for x in range(32):
  print (f0(x))
```

### Determinant of inverse Hilbert matrix.

https://oeis.org/A5249 : 1 1 12 2160 6048000 266716800000 186313420339200000 2067909047925770649600000 365356847125734485878112256000000 1028781784378569697887052962909388800000000 46206893947914691316295628839036278726983680000000000

size 26, time 9806: loop (((loop (x * y) y 1) div (loop ((x * y) * y) (y div 2) 1)) * x) ((x - 1) + x) 1

K L F L B J K L F L F L C G B J G K F K B E K D B J

```
def f1(X,Y):
  x = 1
  for y in range (1,Y + 1):
    x = x * y
  return x

def f2(X,Y):
  x = 1
  for y in range (1,(Y // 2) + 1):
    x = (x * y) * y
  return x

def f0(X):
  x = 1
  for y in range (1,((X - 1) + X) + 1):
    x = (f1(x,y) // f2(x,y)) * x
  return x

for x in range(32):
  print (f0(x))
```

### Fibbinary numbers: if n = F(i1) + F(i2) + ... + F(ik) is the Zeckendorf representation of n (i.e., write n in Fibonacci number system) then a(n) = 2^(i1 - 2) + 2^(i2 - 2) + ... + 2^(ik - 2). Also numbers whose binary representation contains no two adjacent 1's.	

https://oeis.org/A3714 : 0 1 2 4 5 8 9 10 16 17 18 20 21 32 33 34 36 37 40 41 42 64 65 66 68 69 72 73 74 80 81 82 84 85 128 129 130 132 133 136 137 138 144 145 146 148 149 160 161 162 164 165 168 169 170 256 257 258 260 261 264

size 18, time 840641: compr (loop2 ((((y div 2) * y) mod 2) + x) (y div 2) x 0 x) x

L C G L F C H K D L C G K A K N K M

```
def f1(X):
  x,y = 0, X
  for z in range (1,X + 1):
    x,y = ((((y // 2) * y) % 2) + x), (y // 2)
  return x

def f0(X):
  x,i = 0,0
  while i <= X:
    if f1(x) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

for x in range(32):
  print (f0(x))
```

### Nimsum n + 16.	

https://oeis.org/A4457 : 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 80 81 82 83 84 85 86 87 88 89 90

size 22, time 3045: (2 * (2 * (2 * (loop (0 - x) ((((x div 2) div 2) div 2) div 2) 2)))) + x

C C C A K E K C G C G C G C G C J F F F K D

```
def f1(X):
  x = 2
  for y in range (1,((((X // 2) // 2) // 2) // 2) + 1):
    x = 0 - x
  return x

def f0(X):
  return (2 * (2 * (2 * f1(X)))) + X

for x in range(32):
  print (f0(x))
```

### Cumulative product of all divisors of 1..n.	

https://oeis.org/A92143 : 1 2 6 48 240 8640 60480 3870720 104509440 10450944000 114960384000 198651543552000 2582470066176000 506164132970496000 113886929918361600000 116620216236402278400000

size 22, time 11618: loop (x * (loop2 ((if (x mod y) <= 0 then y else 1) * x) (y - 1) y (1 + y) y)) x 1

K K L H L B I K F L B E L B L D L N F K B J


```
def f1(X,Y):
  x,y = 1 + Y, Y
  for z in range (1,Y + 1):
    x,y = ((y if (x % y) <= 0 else 1) * x), (y - 1)
  return x

def f0(X):
  x = 1
  for y in range (1,X + 1):
    x = x * f1(x,y)
  return x

for x in range(32):
  print (f0(x))
```

### Bessel polynomial y_n(-2).

https://oeis.org/A2119 : 1 ~1 7 ~71 1001 ~18089 398959 ~10391023 312129649 ~10622799089 403978495031 ~16977719590391 781379079653017 ~39085931702241241 2111421691000680031 ~122501544009741683039 7597207150294985028449 ~501538173463478753560673

size 27, time 12115: loop (0 - x) x (loop2 (((2 + (2 + ((x - 1) div y))) * x) + y) x (x - 1) 1 (1 + 2))

A K E K C C K B E L G D D K F L D K K B E B B C D N J

```
def f1(X):
  x,y = 1, 1 + 2
  for z in range (1,(X - 1) + 1):
    x,y = (((2 + (2 + ((x - 1) // y))) * x) + y), x
  return x

def f0(X):
  x = f1(X)
  for y in range (1,X + 1):
    x = 0 - x
  return x

for x in range(32):
  print (f0(x))
```

### a(n) = [ tau * a(n-1) ] + [ tau * a(n-2) ].	

https://oeis.org/A5913 : 1 3 5 12 27 62 143 331 766 1774 4109 9518 22048 51074 118313 274073 634893 1470737 3406980 7892311 18282636 42351953 9810
8825 227270312 526474502 1219584727 2825183178

size 39, time 8841: loop2 ((((((((x + y) * y) div x) + y) * y) div (x + y)) + x) + x) x (x - 2) (1 + (2 * (loop (2 - y) (2 - x) 2))) (1 + 2)

K L D L F K G L D L F K L D G K D K D K K C E B C C L E C K E C J F D B C D N

```
def f1(X):
  x = 2
  for y in range (1,(2 - X) + 1):
    x = 2 - y
  return x

def f0(X):
  x,y = 1 + (2 * f1(X)), 1 + 2
  for z in range (1,(X - 2) + 1):
    x,y = ((((((((x + y) * y) // x) + y) * y) // (x + y)) + x) + x), x
  return x

for x in range(32):
  print (f0(x))
```

### Divide odd numbers into groups with prime(n) elements and add together.	

https://oeis.org/A34960 : 4 21 75 189 495 897 1683 2565 4071 6641 8959 13209 17835 22317 28623 37577 48439 57401 71623 85697 98623 118737 138195 1
63493 196231 224321 249775 281945 310759 347249 420751 467801 525943 571985 656047

size 38, time 680635: loop2 ((loop (x * x) 1 (loop ((compr (1 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) ((x div 2) div 2) x)) y) + x) y 0)) - x) (1 + y) 2 0 x

K K F B B K B L D H A K I K C G C G K J E L M K D L A J J K E B L D C A K N

```
def f4(X):
  x = X
  for y in range (1,((X // 2) // 2) + 1):
    x = 0 if (x % (1 + y)) <= 0 else x
  return x

def f3(X,Y):
  x,i = 0,0
  while i <= Y:
    if (1 - f4(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f2(X,Y):
  x = 0
  for y in range (1,Y + 1):
    x = f3(x,y) + x
  return x

def f1(X,Y):
  x = f2(X,Y)
  for y in range (1,1 + 1):
    x = x * x
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,2 + 1):
    x,y = (f1(x,y) - x), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```

### The smallest numbers of every class in a classification of positive numbers (see comment).	

https://oeis.org/A247395 : 1 2 4 10 26 50 122 170 290 362 530 842 962 1370 1682 1850 2210 2810 3482 3722 4490 5042 5330 6242 6890 7922 9410 10202 
10610 11450 11882 12770 16130 17162 18770 19322 22202 22802 24650 26570 27890 29930 32042 32762

size 38, time 1283465: loop ((loop (x * x) 1 (compr (1 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x div 2) x)) y)) + 1) (x - 2) (2 + (loop (1 - y) (2 - x) 2))

K K F B B K B L D H A K I K C G K J E L M J B D K C E C B L E C K E C J D J

```
def f3(X):
  x = X
  for y in range (1,(X // 2) + 1):
    x = 0 if (x % (1 + y)) <= 0 else x
  return x

def f2(X,Y):
  x,i = 0,0
  while i <= Y:
    if (1 - f3(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f1(X,Y):
  x = f2(X,Y)
  for y in range (1,1 + 1):
    x = x * x
  return x

def f4(X):
  x = 2
  for y in range (1,(2 - X) + 1):
    x = 1 - y
  return x

def f0(X):
  x = 2 + f4(X)
  for y in range (1,(X - 2) + 1):
    x = f1(x,y) + 1
  return x

for x in range(32):
  print (f0(x))
```

### Number of odd unitary divisors of n. d is a unitary divisor of n if d divides n and gcd(d,n/d)=1.	

https://oeis.org/A68068 : 1 1 2 1 2 2 2 1 2 2 2 2 2 2 4 1 2 2 2 2 4 2 2 2 2 2 2 2 2 4 2 1 4 2 4 2 2 2 4 2 2 4 2 2 4 2 2 2 2 2 4 2 2 2 4 2 4 2 2 4 2 2 4 1 4 4 2 2 4 4 2 2 2 2 4 2 4 4 2 2 2 2 2 4 4 2 4 2 2 4 4 2 4 2 4 2 2 2 4 2 2 4 2 2 8

size 23, time 93870: (loop2 ((if (((x * x) + x) mod y) <= 0 then 2 else 1) + x) y x 1 (2 + (x + x))) - x

K K F K D L H C B I K D L K B C K K D D N K E

```
def f1(X):
  x,y = 1, 2 + (X + X)
  for z in range (1,X + 1):
    x,y = ((2 if (((x * x) + x) % y) <= 0 else 1) + x), y
  return x

def f0(X):
  return f1(X) - X

for x in range(32):
  print (f0(x))
```

### \[ exp(1/5) * n! \].

https://oeis.org/A30973 : 1 2 7 29 146 879 6155 49246 443222 4432226 48754489 585053875 7605700380 106479805323 1597197079850 25555153277608 434437605719351 7819876902948326 148577661156018207 2971553223120364157

size 25, time 21821: loop (x div (1 + (2 + 2))) x (loop ((((2 * (y + y)) + y) * x) + y) (1 + x) 0)

K B C C D D G K C L L D F L D K F L D B K D A J J


```
def f1(X):
  x = 0
  for y in range (1,(1 + X) + 1):
    x = (((2 * (y + y)) + y) * x) + y
  return x

def f0(X):
  x = f1(X)
  for y in range (1,X + 1):
    x = x // (1 + (2 + 2))
  return x

for x in range(32):
  print (f0(x))
```

### A second-order recursive sequence.	

https://oeis.org/A54469 : 1 7 28 85 218 499 1053 2092 3970 7272 12958 22596 38739 65535 109714 182185 300620 493635 807555 1317360 2144396 3485032 5657028 9174560 14869613 24088399 39009168 63156437 102233030 165466347 267786673

size 29, time 2907924: loop (loop (loop (((((loop2 (1 + (x + y)) x y 2 1) - 2) - y) - y) + x) y x) (2 + y) x) x 1

B K L D D K L C B N C E L E L E K D L K J C L D K J K B J

```
def f3(X,Y):
  x,y = 2, 1
  for z in range (1,Y + 1):
    x,y = (1 + (x + y)), x
  return x

def f2(X,Y):
  x = X
  for y in range (1,Y + 1):
    x = (((f3(x,y) - 2) - y) - y) + x
  return x

def f1(X,Y):
  x = X
  for y in range (1,(2 + Y) + 1):
    x = f2(x,y)
  return x

def f0(X):
  x = 1
  for y in range (1,X + 1):
    x = f1(x,y)
  return x

for x in range(32):
  print (f0(x))
```

### Smallest digit of n.

https://oeis.org/A54054 : 0 1 2 3 4 5 6 7 8 9 0 1 1 1 1 1 1 1 1 1 0 1 2 2 2 2 2 2 2 2 0 1 2 3 3 3 3 3 3 3 0 1 2 3 4 4 4 4 4 4 0 1 2 3 4 5 5 5 5 5 0 1 2 3 4 5 6 6 6 6 0 1 2 3 4 5 6 7 7 7 0 1 2 3 4 5 6 7 8 8 0 1 2 3 4 5 6 7 8 9 0 0 0 0 0

size 57, time 10920: ((loop (((if x <= 0 then 1 else (2 + (2 * (2 + 2)))) * x) - x) 1 (loop2 (((if y <= 0 then 0 else (0 - 1)) * x) - (y mod (2 + (2 * (2 + 2))))) (y div (2 + (2 * (2 + 2)))) 2 0 x)) + x) mod (2 + (2 * (2 + 2)))

K B C C C C D F D I K F K E B L A A B E I K F L C C C C D F D H E L C C C C D F D G C A K N J K D C C C C D F D H

```
def f2(X):
  x,y = 0, X
  for z in range (1,2 + 1):
    x,y = (((0 if y <= 0 else (0 - 1)) * x) - (y % (2 + (2 * (2 + 2))))), (y // (2 + (2 * (2 + 2))))
  return x

def f1(X):
  x = f2(X)
  for y in range (1,1 + 1):
    x = ((1 if x <= 0 else (2 + (2 * (2 + 2)))) * x) - x
  return x

def f0(X):
  return (f1(X) + X) % (2 + (2 * (2 + 2)))

for x in range(32):
  print (f0(x))
```

### Nicomachus triangle read by rows, T(n, k) = 2^(n - k) * 3^k, for 0 <= k <= n.	

https://oeis.org/A36561 : 1 2 3 4 6 9 8 12 18 27 16 24 36 54 81 32 48 72 108 162 243 64 96 144 216 324 486 729 128 192 288 432 648 972 1458 2187 256 384 576 864 1296 1944 2916 4374 6561 512 768 1152 1728 2592 3888 5832 8748 13122 19683

size 57, time 9543: (loop ((x + x) + x) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) 1) * (loop (x + x) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1)

K K D K D K L K E L A I E C K B C C D D G D K J B J K K D A K K A B L D I E C C K B C C C D F D G D D K J E B J F

```
def f2(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f1(X):
  x = 1
  for y in range (1,f2(X) + 1):
    x = (x + x) + x
  return x

def f4(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f3(X):
  x = 1
  for y in range (1,(0 - f4(X)) + 1):
    x = x + x
  return x

def f0(X):
  return f1(X) * f3(X)

for x in range(32):
  print (f0(x))
```

### Number of even semiprimes strictly between prime(n) and 2 * prime(n).	

https://oeis.org/A107347 : 0 1 1 1 1 2 2 3 3 3 4 4 4 5 5 6 6 7 7 8 9 9 9 9 9 10 11 11 12 13 12 13 13 14 13 14 15 15 15 16 16 17 18 19 19 20 19 18 18 19 20 21 22 23 23 23 24 25 25 25 26 27 26 27 28 28 28 28 28 29 30 30 30 31 32 32 32 32

size 51, time 5539354: x - (loop ((if (((loop (x * x) 1 (loop (x + x) (y div 2) 1)) + y) mod (1 + y)) <= 0 then 1 else 0) + x) (((compr (x - (loop (if ((1 + x) mod (1 + y)) <= 0 then y else x) x x)) (1 + x)) div 2) - 1) 0)

K K K F B K K D L C G B J J L D B L D H B A I K D K B K D B L D H L K I K K J E B K D M C G B E A J E

size 51, time 5369335: x - (loop ((if ((1 - (loop (x * x) 1 (loop (x + x) (y div 2) 1))) mod (1 + y)) <= 0 then 1 else 0) + x) (((compr (1 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) (1 + x)) div 2) - 1) 0)

K B K K F B K K D L C G B J J E B L D H B A I K D B K B L D H A K I K C E K J E B K D M C G B E A J E

```
def f3(X,Y):
  x = 1
  for y in range (1,(Y // 2) + 1):
    x = x + x
  return x

def f2(X,Y):
  x = f3(X,Y)
  for y in range (1,1 + 1):
    x = x * x
  return x

def f5(X):
  x = X
  for y in range (1,(X - 2) + 1):
    x = 0 if (x % (1 + y)) <= 0 else x
  return x

def f4(X):
  x,i = 0,0
  while i <= 1 + X:
    if (1 - f5(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f1(X):
  x = 0
  for y in range (1,((f4(X) // 2) - 1) + 1):
    x = (1 if ((1 - f2(x,y)) % (1 + y)) <= 0 else 0) + x
  return x

def f0(X):
  return X - f1(X)

for x in range(32):
  print (f0(x))
```

### Values x of the solutions (x,y) of the Diophantine equation 5\*(X-Y)^4 - 4\*X\*Y = 0 with X >= Y.	

https://oeis.org/A123379 : 0 20 5832 1866940 600952464 193501302500 62306755217496 20062580544024460 6460088608059172128 2080128468849137350580 669794906874257832297960 215671879884924524197142620

size 47, time 2216: (1 + (loop2 ((2 * ((2 * (2 * (x + x))) + x)) - y) x (x - 1) (1 + (2 * (2 + 2))) 1)) * (loop2 y ((2 * ((2 * (2 * (y + y))) + y)) - x) x 0 2)

B C C C K K D F F K D F L E K K B E B C C C D F D B N D L C C C L L D F F L D F K E K A C N F

```
def f1(X):
  x,y = 1 + (2 * (2 + 2)), 1
  for z in range (1,(X - 1) + 1):
    x,y = ((2 * ((2 * (2 * (x + x))) + x)) - y), x
  return x

def f2(X):
  x,y = 0, 2
  for z in range (1,X + 1):
    x,y = y, ((2 * ((2 * (2 * (y + y))) + y)) - x)
  return x

def f0(X):
  return (1 + f1(X)) * f2(X)

for x in range(32):
  print (f0(x))
```

### Half-convolution of Catalan sequence A000108 with itself.	

https://oeis.org/A201204 : 1 1 3 7 23 66 227 715 2529 8398 30275 104006 380162 1337220 4939443 17678835 65844845 238819350 895451117 3282060210 12374186318 45741281820 173257703723 644952073662 2452607696798 9183676536076 35042725663002 131873975875180 504697422982484 1907493251046152

size 46, time 11925: ((loop ((((1 + 2) * (x * y)) div (2 + y)) + x) x 1) + (loop (x * x) 1 (loop ((2 * ((2 * (x * y)) - x)) div (1 + y)) (x div 2) (1 - (x mod 2))))) div 2

B C D K L F F C L D G K D K B J K K F B C C K L F F K E F B L D G K C G B K C H E J J D C G

```
def f1(X):
  x = 1
  for y in range (1,X + 1):
    x = (((1 + 2) * (x * y)) // (2 + y)) + x
  return x

def f3(X):
  x = 1 - (X % 2)
  for y in range (1,(X // 2) + 1):
    x = (2 * ((2 * (x * y)) - x)) // (1 + y)
  return x

def f2(X):
  x = f3(X)
  for y in range (1,1 + 1):
    x = x * x
  return x

def f0(X):
  return (f1(X) + f2(X)) // 2

for x in range(32):
  print (f0(x))
```

### Composite evil numbers.	

https://oeis.org/A125494 : 6 9 10 12 15 18 20 24 27 30 33 34 36 39 40 45 46 48 51 54 57 58 60 63 65 66 68 72 75 77 78 80 85 86 90 92 95 96 99 102 105 106 108 111 114 116 119 120 123 125 126 129 130 132 135 136 141 142 144 147 150 153

size 34, time 259380: compr ((((loop2 (x + y) (y div 2) x 1 x) mod 2) - (loop (if (x mod (1 + y)) <= 0 then 1 else x) (x - 2) x)) mod (1 + x)) (1 + x)

K L D L C G K B K N C H K B L D H B K I K C E K J E B K D H B K D M

size 36, time 157854: compr ((((loop2 (x + y) (y div 2) x 1 x) mod 2) - (loop (if (x mod (1 + y)) <= 0 then 1 else x) ((x div 2) div 2) x)) mod (1 + x)) (1 + x)

K L D L C G K B K N C H K B L D H B K I K C G C G K J E B K D H B K D M

```
def f1(X):
  x,y = 1, X
  for z in range (1,X + 1):
    x,y = (x + y), (y // 2)
  return x

def f2(X):
  x = X
  for y in range (1,((X // 2) // 2) + 1):
    x = 1 if (x % (1 + y)) <= 0 else x
  return x

def f0(X):
  x,i = 0,0
  while i <= 1 + X:
    if (((f1(x) % 2) - f2(x)) % (1 + x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

for x in range(32):
  print (f0(x))
```

### Numbers k such that sin(k) > 0 and sin(k+2) < 0.	

https://oeis.org/A277094 : 2 3 8 9 14 15 20 21 27 28 33 34 39 40 46 47 52 53 58 59 64 65 71 72 77 78 83 84 90 91 96 97 102 103 108 109 115 116 121 122 127 128 134 135 140 141 146 147 152 153 159 160 165 166 171 172 178 179 184

size 28, time 2124: 1 + ((loop ((x div (2 + (2 * (2 + (2 + 2))))) + x) 1 (1 + (2 * (x - (x mod 2))))) + x)

B K C C C C C D D F D G K D B B C K K C H E F D J K D D

```
def f1(X):
  x = 1 + (2 * (X - (X % 2)))
  for y in range (1,1 + 1):
    x = (x // (2 + (2 * (2 + (2 + 2))))) + x
  return x

def f0(X):
  return 1 + (f1(X) + X)

for x in range(32):
  print (f0(x))
```

### a(n) is the number of edges (one-dimensional faces) in the convex polytope of real n X n doubly stochastic matrices.	

https://oeis.org/A59760 : 0 0 1 15 240 5040 147240 5959800 323850240 22800476160 2017745251200 219066851203200 28615863103027200 4425987756321331200 799788468703877452800 166940001463941433728000 39857401887591969128448000 10792266259145851457961984000

size 26, time 9245: (loop (x * y) x (loop (((loop (1 + (x * y)) (y - 1) 1) * y) + x) (x - 1) 0)) div 2

K L F K B K L F D L B E B J L F K D K B E A J J C G

```
def f3(X,Y):
  x = 1
  for y in range (1,(Y - 1) + 1):
    x = 1 + (x * y)
  return x

def f2(X):
  x = 0
  for y in range (1,(X - 1) + 1):
    x = (f3(x,y) * y) + x
  return x

def f1(X):
  x = f2(X)
  for y in range (1,X + 1):
    x = x * y
  return x

def f0(X):
  return f1(X) // 2

for x in range(32):
  print (f0(x))
```

### Numbers k such that cos(k) < cos(k+1).	

https://oeis.org/A246303 : 3 4 5 9 10 11 12 16 17 18 22 23 24 28 29 30 35 36 37 41 42 43 47 48 49 53 54 55 56 60 61 62 66 67 68 72 73 74 79 80 81 85 86 87 91 92 93 97 98 99 100 104 105 106 110 111 112 116 117 118 123 124

size 26, time 154435: (compr (((x - (loop (((x div (2 + 2)) + y) div (1 + 2)) x 0)) div 2) mod 2) (2 + x)) - 2

K K C C D G L D B C D G K A J E C G C H C K D M C E

```
def f2(X):
  x = 0
  for y in range (1,X + 1):
    x = ((x // (2 + 2)) + y) // (1 + 2)
  return x

def f1(X):
  x,i = 0,0
  while i <= 2 + X:
    if (((x - f2(x)) // 2) % 2) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  return f1(X) - 2

for x in range(32):
  print (f0(x))
```

### Numbers that contain an odd digit.	

https://oeis.org/A7957 : 1 3 5 7 9 10 11 12 13 14 15 16 17 18 19 21 23 25 27 29 30 31 32 33 34 35 36 37 38 39 41 43 45 47 49 50 51 52 53 54 55 56 57 58 59 61 63 65 67 69 70 71 72 73 74 75 76 77 78 79 81 83 85 87 89 90 91 92 93 94 95 96 97 98 99 100

size 25, time 3050846: loop (compr ((loop2 ((x * y) + x) ((y div 2) div (1 + (2 + 2))) x 1 x) mod 2) y) x 1

K L F K D L C G B C C D D G K B K N C H L M K B J

```
def f2(X):
  x,y = 1, X
  for z in range (1,X + 1):
    x,y = ((x * y) + x), ((y // 2) // (1 + (2 + 2)))
  return x

def f1(X,Y):
  x,i = 0,0
  while i <= Y:
    if (f2(x) % 2) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  x = 1
  for y in range (1,X + 1):
    x = f1(x,y)
  return x

for x in range(32):
  print (f0(x))
```

### Expand cos x / exp x and invert nonzero coefficients.	

https://oeis.org/A7452 : 1 ~1 0 3 ~6 30 0 ~630 2520 ~22680 0 1247400 ~7484400 97297200 0 ~10216206000 81729648000 ~1389404016000 0 237588086736000 ~2375880867360000 49893498214560000 0 ~12623055048283680000

size 34, time 4395: loop ((x * y) div 2) x (loop (0 - (x + x)) (x - (x div 2)) (loop2 y (0 - x) ((x div 2) mod (2 + 2)) 1 (x mod 2)))

K L F C G K A K K D E K K C G E L A K E K C G C C D H B K C H N J J

```
def f2(X):
  x,y = 1, X % 2
  for z in range (1,((X // 2) % (2 + 2)) + 1):
    x,y = y, (0 - x)
  return x

def f1(X):
  x = f2(X)
  for y in range (1,(X - (X // 2)) + 1):
    x = 0 - (x + x)
  return x

def f0(X):
  x = f1(X)
  for y in range (1,X + 1):
    x = (x * y) // 2
  return x

for x in range(32):
  print (f0(x))
```

### Length of longest integral ladder that can be moved horizontally around the right angled corner where two hallway corridors of integral widths meet.

https://oeis.org/A88896 : 125 1000 2197 3375 4913 8000 15625 17576 24389 27000 39304 42875 50653 59319 64000 68921 91125 125000 132651 140608 148877 166375 195112 216000 226981 274625 314432 343000 389017 405224 421875 474552 512000

size 40, time 69970: loop ((x * x) * x) 1 (compr (((1 + (loop2 ((if ((((x * x) * x) + x) mod (y + y)) <= 0 then 0 else 1) + x) y x 1 x)) div (1 + x)) mod 2) (1 + x))

K K F K F B B K K F K F K D L L D H A B I K D L K B K N D B K D G C H B K D M J

```
def f2(X):
  x,y = 1, X
  for z in range (1,X + 1):
    x,y = ((0 if ((((x * x) * x) + x) % (y + y)) <= 0 else 1) + x), y
  return x

def f1(X):
  x,i = 0,0
  while i <= 1 + X:
    if (((1 + f2(x)) // (1 + x)) % 2) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  x = f1(X)
  for y in range (1,1 + 1):
    x = (x * x) * x
  return x

for x in range(32):
  print (f0(x))
```

### Start with the symbol \*\*|\* and for each iteration replace \* with \*\*|\* . This sequence is the number of \*'s between each dash.	

https://oeis.org/A131989 : 2 3 1 2 3 3 1 2 1 2 3 1 2 3 3 1 2 3 3 1 2 1 2 3 1 2 1 2 3 1 2 3 3 1 2 1 2 3 1 2 3 3 1 2 3 3 1 2 1 2 3 1 2 3 3 1 2 3 3 1 2 1 2 3 1 2 1 2 3 1 2 3 3 1 2 1 2 3 1 2 1 2 3 1 2 3 3 1 2 1 2 3 1 2 3 3 1 2 3

size 40, time 1746526: loop2 ((compr ((loop2 (x + (loop2 (((2 + y) div (1 + 2)) + x) (y div (1 + 2)) y 0 y)) (y - 1) 2 0 x) mod 2) y) - x) (1 + y) 2 0 x

K C L D B C D G K D L B C D G L A L N D L B E C A K N C H L M K E B L D C A K N

```
def f3(X,Y):
  x,y = 0, Y
  for z in range (1,Y + 1):
    x,y = (((2 + y) // (1 + 2)) + x), (y // (1 + 2))
  return x

def f2(X):
  x,y = 0, X
  for z in range (1,2 + 1):
    x,y = (x + f3(x,y)), (y - 1)
  return x

def f1(X,Y):
  x,i = 0,0
  while i <= Y:
    if (f2(x) % 2) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  x,y = 0, X
  for z in range (1,2 + 1):
    x,y = (f1(x,y) - x), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```

### Number of triangles with perimeter n whose side lengths are even.	

https://oeis.org/A308066 : 0 0 0 0 0 1 0 0 0 1 0 1 0 2 0 1 0 3 0 2 0 4 0 3 0 5 0 4 0 7 0 5 0 8 0 7 0 10 0 8 0 12 0 10 0 14 0 12 0 16 0 14 0 19 0 16 0 21 0 19 0 24 0 21 0 27 0 24 0 30 0 27 0 33 0 30 0 37 0

size 61, time 122476: loop (loop2 (x + (loop2 ((loop ((2 + (loop ((y div 2) + x) x x)) div (1 + 2)) 1 (y div 2)) - x) (1 + y) 2 0 y)) ((((y - 2) - 2) - 2) - 2) (1 + (x div (2 * (2 + 2)))) 0 x) 1 (loop y ((x - 2) - 2) 2)

K C L C G K D K K J D B C D G B L C G J K E B L D C A L N D L C E C E C E C E B K C C C D F G D A K N B L K C E C E C J J

```
def f4(X):
  x = X
  for y in range (1,X + 1):
    x = (y // 2) + x
  return x

def f3(X,Y):
  x = Y // 2
  for y in range (1,1 + 1):
    x = (2 + f4(x)) // (1 + 2)
  return x

def f2(X,Y):
  x,y = 0, Y
  for z in range (1,2 + 1):
    x,y = (f3(x,y) - x), (1 + y)
  return x

def f1(X):
  x,y = 0, X
  for z in range (1,(1 + (X // (2 * (2 + 2)))) + 1):
    x,y = (x + f2(x,y)), ((((y - 2) - 2) - 2) - 2)
  return x

def f5(X):
  x = 2
  for y in range (1,((X - 2) - 2) + 1):
    x = y
  return x

def f0(X):
  x = f5(X)
  for y in range (1,1 + 1):
    x = f1(x)
  return x

for x in range(32):
  print (f0(x))
```

### Numbers that contain a digit 0.	

This program fails for 1011 - the OEIS sequence should be longer.

https://oeis.org/A11540 : 0 10 20 30 40 50 60 70 80 90 100 101 102 103 104 105 106 107 108 109 110 120 130 140 150 160 170 180 190 200 201 202 203 204 205 206 207 208 209 210 220 230 240 250 260 270 280 290 300 301 302

size 60, time 70370: compr ((loop2 ((if y <= 0 then 1 else (y mod (2 + (2 * (2 + 2))))) * x) (x div (2 + (2 * (2 + 2)))) 2 x x) - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (1 + (2 + (x div (2 * (2 * (2 + 2)))))) (1 + x))) ((if x <= 0 then 0 else 1) + x)

L B L C C C C D F D H I K F K C C C C D F D G C K K N K B L D H C K I B C K C C C C D F F G D D B K D J E K A B I K D M

```
def f1(X):
  x,y = X, X
  for z in range (1,2 + 1):
    x,y = ((1 if y <= 0 else (y % (2 + (2 * (2 + 2))))) * x), (x // (2 + (2 * (2 + 2))))
  return x

def f2(X):
  x = 1 + X
  for y in range (1,(1 + (2 + (X // (2 * (2 * (2 + 2)))))) + 1):
    x = 2 if (x % (1 + y)) <= 0 else x
  return x

def f0(X):
  x,i = 0,0
  while i <= (0 if X <= 0 else 1) + X:
    if (f1(x) - f2(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

for x in range(32):
  print (f0(x))
```

### Characteristic function of Sophie Germain primes.	

https://oeis.org/A156660 : 0 0 1 1 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

size 54, time 35554: (((if ((loop (if (((x - 1) + x) mod (1 + y)) <= 0 then 1 else x) (2 + (x div (2 * (2 + 2)))) (1 + x)) mod (1 + x)) <= 0 then 2 else 0) + (loop (if (x mod (1 + y)) <= 0 then 1 else x) ((x div 2) div 2) x)) div (1 + x)) mod 2

K B E K D B L D H B K I C K C C C D F G D B K D J B K D H C A I K B L D H B K I K C G C G K J D B K D G C H

```
def f1(X):
  x = 1 + X
  for y in range (1,(2 + (X // (2 * (2 + 2)))) + 1):
    x = 1 if (((x - 1) + x) % (1 + y)) <= 0 else x
  return x

def f2(X):
  x = X
  for y in range (1,((X // 2) // 2) + 1):
    x = 1 if (x % (1 + y)) <= 0 else x
  return x

def f0(X):
  return (((2 if (f1(X) % (1 + X)) <= 0 else 0) + f2(X)) // (1 + X)) % 2

for x in range(32):
  print (f0(x))
```

### Gaps between twin prime pairs.	

https://oeis.org/A167132 : 0 4 4 10 10 16 10 28 4 28 10 28 10 4 28 10 28 10 28 34 70 10 28 58 46 28 16 22 16 148 10 4 28 22 136 10 16 10 28 58 76 46 10 10 16 106 22 28 4 118 10 46 28 22 64 82 4 52 16 46 28 52 4 22 16 10 94 28 40 28 40 166

size 46, time 4983115: (2 * (loop2 ((compr (x - (loop (if (((2 + x) * x) mod (1 + y)) <= 0 then 1 else x) (2 + (x div (1 + (2 + 2)))) ((1 + x) + x))) (1 + y)) - x) (1 + y) 2 0 x)) - 2

C K C K D K F B L D H B K I C K B C C D D G D B K D K D J E B L D M K E B L D C A K N F C E

```
def f3(X):
  x = (1 + X) + X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = 1 if (((2 + x) * x) % (1 + y)) <= 0 else x
  return x

def f2(X,Y):
  x,i = 0,0
  while i <= 1 + Y:
    if (x - f3(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f1(X):
  x,y = 0, X
  for z in range (1,2 + 1):
    x,y = (f2(x,y) - x), (1 + y)
  return x

def f0(X):
  return (2 * f1(X)) - 2

for x in range(32):
  print (f0(x))
```

### Hypotenuses of primitive Pythagorean triangles.	

https://oeis.org/A8846 : 5 13 17 25 29 37 41 53 61 65 73 85 89 97 101 109 113 125 137 145 149 157 169 173 181 185 193 197 205 221 229 233 241 257 265 269 277 281 289 293 305 313 317 325 337 349 353 365 373 377 389 397 401 409 421 425 433

size 37, time 450435: 1 + (2 * (compr (((1 + (loop2 (1 + (if ((1 + (x * x)) mod (1 + y)) <= 0 then 0 else x)) y x 1 (x + x))) div (1 + x)) mod 2) (1 + x)))

B C B B B K K F D B L D H A K I D L K B K K D N D B K D G C H B K D M F D

```
def f2(X):
  x,y = 1, X + X
  for z in range (1,X + 1):
    x,y = (1 + (0 if ((1 + (x * x)) % (1 + y)) <= 0 else x)), y
  return x

def f1(X):
  x,i = 0,0
  while i <= 1 + X:
    if (((1 + f2(x)) // (1 + x)) % 2) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  return 1 + (2 * f1(X))

for x in range(32):
  print (f0(x))
```

### a(n) is the Y-coordinate of the n-th point of the Peano curve. Sequence A332380 gives X-coordinates.	

https://oeis.org/A332381 : 0 0 1 1 0 0 ~1 ~1 0 0 1 1 2 2 1 1 2 2 3 3 4 4 3 3 2 2 3 3 2 2 1 1 2 2 1 1 0 0 ~1 ~1 0 0 1 1 0 0 ~1 ~1 ~2 ~2 ~1 ~1 ~2 ~2 ~3 ~3 ~2 ~2 ~3 ~3 ~4 ~4 ~3 ~3 ~2 ~2 ~1 ~1 ~2 ~2 ~1 ~1 0 0 1 1 0

size 34, time 135769: loop2 (x + (loop2 (loop (0 - x) ((y div (1 + 2)) mod 2) x) (y div (1 + 2)) (1 + 2) 1 y)) (2 + y) (x div 2) 0 1

K A K E L B C D G C H K J L B C D G B C D B L N D C L D K C G A B N

```
def f2(X,Y):
  x = X
  for y in range (1,((Y // (1 + 2)) % 2) + 1):
    x = 0 - x
  return x

def f1(X,Y):
  x,y = 1, Y
  for z in range (1,(1 + 2) + 1):
    x,y = f2(x,y), (y // (1 + 2))
  return x

def f0(X):
  x,y = 0, 1
  for z in range (1,(X // 2) + 1):
    x,y = (x + f1(x,y)), (2 + y)
  return x

for x in range(32):
  print (f0(x))
```

### Fixed point reached by iterating the Kempner function A002034 starting at n.	

https://oeis.org/A25492 : 1 2 3 4 5 3 7 4 3 5 11 4 13 7 5 3 17 3 19 5 7 11 23 4 5 13 3 7 29 5 31 4 11 17 7 3 37 19 13 5 41 7 43 11 3 23 47 3 7 5 17 13 53 3 11 7 19 29 59 5 61 31 7 4 13 11 67 17 23 7 71 3 73 37 5 19 11 13 79 3 3 41 83 7 17

size 37, time 3780763: loop (loop2 (if (x mod y) <= 0 then y else x) (y - 1) (x - 2) x x) 1 (loop2 ((if ((loop (x * y) x 1) mod (1 + y)) <= 0 then 0 else 1) + x) y x 1 x)

K L H L K I L B E K C E K K N B K L F K B J B L D H A B I K D L K B K N J

```
def f1(X):
  x,y = X, X
  for z in range (1,(X - 2) + 1):
    x,y = (y if (x % y) <= 0 else x), (y - 1)
  return x

def f3(X):
  x = 1
  for y in range (1,X + 1):
    x = x * y
  return x

def f2(X):
  x,y = 1, X
  for z in range (1,X + 1):
    x,y = ((0 if (f3(x) % (1 + y)) <= 0 else 1) + x), y
  return x

def f0(X):
  x = f2(X)
  for y in range (1,1 + 1):
    x = f1(x)
  return x

for x in range(32):
  print (f0(x))
```

### Numbers k such that k^2 - k - 1 and k^2 - k + 1 are twin primes.	

https://oeis.org/A131530 : 3 4 6 7 9 16 21 22 25 39 42 51 55 60 67 90 102 132 139 142 154 156 165 177 189 204 207 210 216 219 232 237 247 289 291 310 315 352 379 396 406 454 456 457 496 501 519 531 552 561 625 645 669 687 721 729 744

size 31, time 4408507: 1 + (compr (x - (loop (if (((2 - x) * x) mod (1 + y)) <= 0 then 0 else x) (x - 2) (1 + ((x * x) + x)))) (2 + x))

B K C K E K F B L D H A K I K C E B K K F K D D J E C K D M D

```
def f2(X):
  x = 1 + ((X * X) + X)
  for y in range (1,(X - 2) + 1):
    x = 0 if (((2 - x) * x) % (1 + y)) <= 0 else x
  return x

def f1(X):
  x,i = 0,0
  while i <= 2 + X:
    if (x - f2(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  return 1 + f1(X)

for x in range(32):
  print (f0(x))
```

### Expansion of the exponential generating function arcsin(2\*x)/(2\*(1-2\*x)^(3/2)).	

https://oeis.org/A143165 : 0 1 6 49 468 5469 73362 1138005 19737000 383284665 8163588510 190709475705 4818820261500 131650382056725 3850053335966250 120466494638624925 4002649276431128400 141156781966460192625 5252646220794868029750 206149276075766825426625

size 30, time 66940: loop ((2 * (x * y)) + (loop (((2 * (x * y)) - x) + (loop2 (x * y) (y - 2) y 1 1)) y 0)) x 0

C K L F F C K L F F K E K L F L C E L B B N D L A J D K A J

```
def f2(X,Y):
  x,y = 1, 1
  for z in range (1,Y + 1):
    x,y = (x * y), (y - 2)
  return x

def f1(X,Y):
  x = 0
  for y in range (1,Y + 1):
    x = ((2 * (x * y)) - x) + f2(x,y)
  return x

def f0(X):
  x = 0
  for y in range (1,X + 1):
    x = (2 * (x * y)) + f1(x,y)
  return x

for x in range(32):
  print (f0(x))
```

### \[ exp(1/9)\*n! ].	

https://oeis.org/A30957 : 1 2 6 26 134 804 5632 45058 405525 4055253 44607785 535293421 6958814485 97423402796 1461351041944 23381616671119 397487483409030 7154774701362549 135940719325888433 2718814386517768672

size 29, time 29870: loop (x div (1 + (2 * (2 + 2)))) x (loop ((((2 * (2 * (y + y))) + y) * x) + y) (1 + x) 0)

K B C C C D F D G K C C L L D F F L D K F L D B K D A J J

```
def f1(X):
  x = 0
  for y in range (1,(1 + X) + 1):
    x = (((2 * (2 * (y + y))) + y) * x) + y
  return x

def f0(X):
  x = f1(X)
  for y in range (1,X + 1):
    x = x // (1 + (2 * (2 + 2)))
  return x

for x in range(32):
  print (f0(x))
```

### Sum of the products of the smaller and larger parts of the partitions of n into two parts with the smaller part odd.	

https://oeis.org/A295286 : 0 1 2 3 4 14 18 22 26 55 64 73 82 140 156 172 188 285 310 335 360 506 542 578 614 819 868 917 966 1240 1304 1368 1432 1785 1866 1947 2028 2470 2570 2670 2770 3311 3432 3553 3674 4324 4468 4612 4756 5525 5694

size 28, time 268039: (loop2 (((loop (loop (((y mod 2) * y) + x) (y div 2) x) y 0) * y) - x) (1 + y) 2 0 x) div 2

L C H L F K D L C G K J L A J L F K E B L D C A K N C G

```
def f3(X,Y):
  x = X
  for y in range (1,(Y // 2) + 1):
    x = ((y % 2) * y) + x
  return x

def f2(X,Y):
  x = 0
  for y in range (1,Y + 1):
    x = f3(x,y)
  return x

def f1(X):
  x,y = 0, X
  for z in range (1,2 + 1):
    x,y = ((f2(x,y) * y) - x), (1 + y)
  return x

def f0(X):
  return f1(X) // 2

for x in range(32):
  print (f0(x))
```

### Number of n X n matrices over GF(2) with rank n-1.	

https://oeis.org/A86699 : 1 9 294 37800 19373760 39687459840 325139829719040 10654345790226432000 1396491759480328106803200 732164571206732295657278668800 1535460761275478347250381697633484800

size 25, time 2501: ((loop (x + x) x 2) - 1) * (loop2 (((y * y) - (y div 2)) * x) (y + y) x 1 2)

K K D K C J B E L L F L C G E K F L L D K B C N F

```
def f1(X):
  x = 2
  for y in range (1,X + 1):
    x = x + x
  return x

def f2(X):
  x,y = 1, 2
  for z in range (1,X + 1):
    x,y = (((y * y) - (y // 2)) * x), (y + y)
  return x

def f0(X):
  return (f1(X) - 1) * f2(X)

for x in range(32):
  print (f0(x))
```

### Liouville's function L(n) = partial sums of A008836.

https://oeis.org/A2819 : 0 1 0 ~1 0 ~1 0 ~1 ~2 ~1 0 ~1 ~2 ~3 ~2 ~1 0 ~1 ~2 ~3 ~4 ~3 ~2 ~3 ~2 ~1 0 ~1 ~2 ~3 ~4 ~5 ~6 ~5 ~4 ~3 ~2 ~3 ~2 ~1 0 ~1 ~2 ~3 ~4 ~5 ~4 ~5 ~6 ~5 ~6 ~5 ~6 ~7 ~6 ~5 ~4 ~3 ~2 ~3 ~2 ~3 ~2 ~3 ~2 ~1 ~2 ~3 ~4 ~3 ~4 ~5 ~6 ~7 ~6 ~7 ~8 ~7 ~8 ~9 ~10 ~9 ~8 ~9 ~8 ~7 ~6

size 22, time 1797188: loop (((loop (if ((x * x) mod (1 + y)) <= 0 then (0 - x) else x) y y) div y) + x) x 0

K K F B L D H A K E K I L L J L G K D K A J

```
def f1(X,Y):
  x = Y
  for y in range (1,Y + 1):
    x = (0 - x) if ((x * x) % (1 + y)) <= 0 else x
  return x

def f0(X):
  x = 0
  for y in range (1,X + 1):
    x = (f1(x,y) // y) + x
  return x

for x in range(32):
  print (f0(x))
```

### Pascal's triangle read by rows: C(n,k) = binomial(n,k) = n!/(k!\*(n-k)!), 0 <= k <= n.

https://oeis.org/A7318 : 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 1 10 45 120 210 252 210 120 45 10 1 1 11 55 165 330 462 462 330 165 55 11 1

size 51, time 85098: (loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop y (x - y) x) x (1 + x))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)

K L F B L D A K K A B L D I E K K J E B L K L E K J K B K D J N K L F A K K A B L D I E K K J E B J G

```
def f2(X):
  x = X
  for y in range (1,X + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f4(X,Y):
  x = X
  for y in range (1,(X - Y) + 1):
    x = y
  return x

def f3(X):
  x = 1 + X
  for y in range (1,X + 1):
    x = f4(x,y)
  return x

def f1(X):
  x,y = 1, f3(X)
  for z in range (1,(0 - f2(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f6(X):
  x = X
  for y in range (1,X + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f5(X):
  x = 1
  for y in range (1,(0 - f6(X)) + 1):
    x = x * y
  return x

def f0(X):
  return f1(X) // f5(X)

for x in range(32):
  print (f0(x))
```

### Liouville's function lambda(n) = (-1)^k, where k is number of primes dividing n (counted with multiplicity).	

https://oeis.org/A8836 : 1 ~1 ~1 1 ~1 1 ~1 ~1 1 1 ~1 ~1 ~1 1 1 1 ~1 ~1 ~1 ~1 1 1 ~1 1 1 1 ~1 ~1 ~1 ~1 ~1 ~1 1 1 1 1 ~1 1 1 1 ~1 ~1 ~1 ~1 ~1 1 ~1 ~1 1 ~1 1 ~1 ~1 1 1 1 1 1 ~1 1 ~1 1 ~1 1 1 ~1 ~1 ~1 1 ~1 ~1 ~1 ~1 1 ~1 ~1 1 ~1 ~1 ~1 1 1 ~1 1 1 1 1 1 ~1 1 1 ~1 1 1 1 1 ~1 ~1 ~1 1 ~1

size 19, time 72013: (loop (if ((x * x) mod y) <= 0 then (0 - x) else x) x (1 + x)) div (1 + x)

K K F L H A K E K I K B K D J B K D G

```
def f1(X):
  x = 1 + X
  for y in range (1,X + 1):
    x = (0 - x) if ((x * x) % y) <= 0 else x
  return x

def f0(X):
  return f1(X) // (1 + X)

for x in range(32):
  print (f0(x))
```

### Molien series for invariants of finite Coxeter group A_7.	

https://oeis.org/A266776 : 1 0 1 1 2 2 4 4 7 7 11 12 18 19 27 30 40 44 58 64 82 91 113 126 155 171 207 230 274 303 358 395 462 509 589 649 746 818 934 1024 1161 1269 1432 1562 1753 1909 2131 2317 2577 2794 3095 3352 3698 3997 4396 4743 5200 5601 6121 6584 7177 7705 8377 8983 9741 10429 11285 12065

size 106, time 2276938: loop2 (loop2 (loop2 (loop2 ((loop ((2 + (loop ((y div 2) + x) x x)) div (1 + 2)) 1 (loop (y - x) y 1)) + x) (((y - 1) - 2) - 2) (1 + (y div (1 + (2 + 2)))) x y) (((y - 2) - 2) - 2) (1 + (y div (2 + (2 + 2)))) x y) ((((y - 1) - 2) - 2) - 2) (1 + (y div (1 + (2 + (2 + 2))))) x y) ((((y - 2) - 2) - 2) - 2) (1 + (x div (2 * (2 + 2)))) 0 x

C L C G K D K K J D B C D G B L K E L B J J K D L B E C E C E B L B C C D D G D K L N L C E C E C E B L C C C D D G D K L N L B E C E C E C E B L B C C C D D D G D K L N L C E C E C E C E B K C C C D F G D A K N

```
def f5(X):
  x = X
  for y in range (1,X + 1):
    x = (y // 2) + x
  return x

def f6(X,Y):
  x = 1
  for y in range (1,Y + 1):
    x = y - x
  return x

def f4(X,Y):
  x = f6(X,Y)
  for y in range (1,1 + 1):
    x = (2 + f5(x)) // (1 + 2)
  return x

def f3(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 + 2)))) + 1):
    x,y = (f4(x,y) + x), (((y - 1) - 2) - 2)
  return x

def f2(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + (2 + 2)))) + 1):
    x,y = f3(x,y), (((y - 2) - 2) - 2)
  return x

def f1(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 + (2 + 2))))) + 1):
    x,y = f2(x,y), ((((y - 1) - 2) - 2) - 2)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,(1 + (X // (2 * (2 + 2)))) + 1):
    x,y = f1(x,y), ((((y - 2) - 2) - 2) - 2)
  return x

for x in range(32):
  print (f0(x))
```

### Hosoya triangle of Lucas type.	

https://oeis.org/A284115 : 1 3 3 4 9 4 7 12 12 7 11 21 16 21 11 18 33 28 28 33 18 29 54 44 49 44 54 29 47 87 72 77 77 72 87 47 76 141 116 126 121 126 116 141 76 123 228 188 203 198 198 203 188 228 123 199 369 304 329 319 324 319 329 304 369 199

size 63, time 12446: (loop2 (x + y) x (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x) 1 2) * (loop2 (x + y) x (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 2)

K L D K K L K E L A I E C C K B C C C D F D G D D K J B C N K L D K A K K A B L D I E C C K B C C C D F D G D D K J E B C N F

size 39, time 37070: (loop2 (x + y) x (loop (x - (if (y - x) <= 0 then y else 0)) x x) 1 2) * (loop2 (x + y) x (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 2)

K L D K K L K E L A I E K K J B C N K L D K A K K A B L D I E K K J E B C N F

```
def f2(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f1(X):
  x,y = 1, 2
  for z in range (1,f2(X) + 1):
    x,y = (x + y), x
  return x

def f4(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f3(X):
  x,y = 1, 2
  for z in range (1,(0 - f4(X)) + 1):
    x,y = (x + y), x
  return x

def f0(X):
  return f1(X) * f3(X)

for x in range(32):
  print (f0(x))
```

### For each prime p take the sum of nonprimes < p.	

https://oeis.org/A45717 : 1 1 5 11 38 50 95 113 176 306 336 506 623 665 800 1050 1330 1390 1710 1917 1989 2369 2612 3042 3693 3990 4092 4407 4515 4848 6408 6795 7465 7603 8899 9049 9819 10619 11114 11964 12844 13024 14698 14890 15475

size 59, time 2796366: loop (((1 + y) * (if (((loop (x * x) 1 (loop (x + x) (y div 2) 1)) + y) mod (1 + y)) <= 0 then 0 else 1)) + x) (compr (x - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) (1 + x)) 1

B L D K K F B K K D L C G B J J L D B L D H A B I F K D K K B L D H C K I C K C C C C D D F G D B K D J E B K D M B J

```
def f2(X,Y):
  x = 1
  for y in range (1,(Y // 2) + 1):
    x = x + x
  return x

def f1(X,Y):
  x = f2(X,Y)
  for y in range (1,1 + 1):
    x = x * x
  return x

def f4(X):
  x = 1 + X
  for y in range (1,(2 + (X // (2 * (2 + (2 + 2))))) + 1):
    x = 2 if (x % (1 + y)) <= 0 else x
  return x

def f3(X):
  x,i = 0,0
  while i <= 1 + X:
    if (x - f4(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  x = 1
  for y in range (1,f3(X) + 1):
    x = ((1 + y) * (0 if ((f1(x,y) + y) % (1 + y)) <= 0 else 1)) + x
  return x

for x in range(32):
  print (f0(x))
```

### Primes p for which the continued fraction expansion of sqrt(p) does not have a 1 in the second position.	

https://oeis.org/A307508 : 2 5 11 17 19 29 37 41 53 67 71 83 89 101 103 107 109 127 131 149 151 173 179 181 197 199 227 229 233 239 257 263 269 271 293 331 337 367 373 379 401 409 419 443 449 457 461 487 491 499 503 541 547 577 587 593 599

size 55, time 692880: compr ((loop ((((loop (((2 * (y + y)) div ((2 + x) * x)) + x) x 1) + x) mod 2) + x) 1 (loop (if (x mod (1 + y)) <= 0 then 2 else x) (1 + (2 + (x div (2 * (2 * (2 + 2)))))) x)) mod (1 + x)) (2 + x)

C L L D F C K D K F G K D K B J K D C H K D B K B L D H C K I B C K C C C C D F F G D D K J J B K D H C K D M

```
def f2(X):
  x = 1
  for y in range (1,X + 1):
    x = ((2 * (y + y)) // ((2 + x) * x)) + x
  return x

def f3(X):
  x = X
  for y in range (1,(1 + (2 + (X // (2 * (2 * (2 + 2)))))) + 1):
    x = 2 if (x % (1 + y)) <= 0 else x
  return x

def f1(X):
  x = f3(X)
  for y in range (1,1 + 1):
    x = ((f2(x) + x) % 2) + x
  return x

def f0(X):
  x,i = 0,0
  while i <= 2 + X:
    if (f1(x) % (1 + x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

for x in range(32):
  print (f0(x))
```

### Triangle of denominators in Leibniz's Harmonic Triangle a(n,k), n >= 1, 1 <= k <= n.	

https://oeis.org/A3506 : 1 2 2 3 6 3 4 12 12 4 5 20 30 20 5 6 30 60 60 30 6 7 42 105 140 105 42 7 8 56 168 280 280 168 56 8 9 72 252 504 630 504 252 72 9 10 90 360 840 1260 1260 840 360 90 10 11 110 495 1320 2310 2772 2310 1320 495 110 11

size 51, time 60456: (loop2 (x * y) (1 + y) (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop y (x - y) x) x (1 + x))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)

K L F B L D B K K A B L D I E K K J E B L K L E K J K B K D J N K L F A K K A B L D I E K K J E B J G

```
def f2(X):
  x = X
  for y in range (1,X + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f4(X,Y):
  x = X
  for y in range (1,(X - Y) + 1):
    x = y
  return x

def f3(X):
  x = 1 + X
  for y in range (1,X + 1):
    x = f4(x,y)
  return x

def f1(X):
  x,y = 1, f3(X)
  for z in range (1,(1 - f2(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f6(X):
  x = X
  for y in range (1,X + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f5(X):
  x = 1
  for y in range (1,(0 - f6(X)) + 1):
    x = x * y
  return x

def f0(X):
  return f1(X) // f5(X)

for x in range(32):
  print (f0(x))
```

### Luhn algorithm double-and-add sum of digits of n.	

https://oeis.org/A93017 : 0 1 2 3 4 5 6 7 8 9 2 3 4 5 6 7 8 9 10 11 4 5 6 7 8 9 10 11 12 13 6 7 8 9 10 11 12 13 14 15 8 9 10 11 12 13 14 15 16 17 1 2 3 4 5 6 7 8 9 10 3 4 5 6 7 8 9 10 11 12 5 6 7 8 9 10 11 12 13 14 7 8 9 10 11 12 13

size 44, time 10092: loop2 ((y mod (2 + (2 * (2 + 2)))) + x) (y div (2 + (2 * (2 + 2)))) (1 + 2) (x mod (2 + (2 * (2 + 2)))) (2 * (x div (2 + (2 * (2 + 2)))))

L C C C C D F D H K D L C C C C D F D G B C D K C C C C D F D H C K C C C C D F D G F N

```
def f0(X):
  x,y = X % (2 + (2 * (2 + 2))), 2 * (X // (2 + (2 * (2 + 2))))
  for z in range (1,(1 + 2) + 1):
    x,y = ((y % (2 + (2 * (2 + 2)))) + x), (y // (2 + (2 * (2 + 2))))
  return x

for x in range(32):
  print (f0(x))
```

### Expansion of f(x) = f(x, -x^2) in powers of x where f(, ) is Ramanujan's general theta function.	

https://oeis.org/A121373 : 1 1 ~1 0 0 ~1 0 ~1 0 0 0 0 ~1 0 0 1 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 ~1 0 0 0 0 0 0 0 0 0 0 ~1 0 0 0 0 0 ~1 0 0 0 0 0 0 0 0 0 0 0 0 ~1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0

size 43, time 1695513: loop (0 - x) x (loop2 ((loop (if (x mod (1 + y)) <= 0 then (0 - x) else x) 2 (loop ((y div (loop (x + y) x 1)) + x) y 0)) - x) (1 + y) 2 0 ((x + x) + x))

A K E K K B L D H A K E K I C L K L D K B J G K D L A J J K E B L D C A K K D K D N J

```
def f4(X):
  x = 1
  for y in range (1,X + 1):
    x = x + y
  return x

def f3(X,Y):
  x = 0
  for y in range (1,Y + 1):
    x = (y // f4(x)) + x
  return x

def f2(X,Y):
  x = f3(X,Y)
  for y in range (1,2 + 1):
    x = (0 - x) if (x % (1 + y)) <= 0 else x
  return x

def f1(X):
  x,y = 0, (X + X) + X
  for z in range (1,2 + 1):
    x,y = (f2(x,y) - x), (1 + y)
  return x

def f0(X):
  x = f1(X)
  for y in range (1,X + 1):
    x = 0 - x
  return x

for x in range(32):
  print (f0(x))
```

### The Akiyama-Tanigawa algorithm applied to 1/(1,2,3,5,... old prime numbers). Reduced numerators of the second row.	

https://oeis.org/A227127 : 1 1 2 8 20 12 28 16 36 60 22 72 52 28 60 96 102 36 114 80 42 132 92 144 200 104 54 112 58 120 434 128 198 68 350 72 222 228 156 240 246 84 430 88 180 92 564 576 196 100 204 312 106 540 330 336 342 116 354 240 122

size 39, time 956489: (loop2 ((compr (1 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) y) - x) (1 + y) 2 0 x) * ((loop2 (x + y) 0 (x - 2) 1 x) - y)

B K B L D H A K I K C E K J E L M K E B L D C A K N K L D A K C E B K N L E F

size 41, time 252581: (loop2 ((compr (1 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x div (2 + 2)) x)) y) - x) (1 + y) 2 0 x) * ((loop2 (x + y) 0 (x - 2) 1 x) - y)

B K B L D H A K I K C C D G K J E L M K E B L D C A K N K L D A K C E B K N L E F

```
def f3(X):
  x = X
  for y in range (1,(X // (2 + 2)) + 1):
    x = 0 if (x % (1 + y)) <= 0 else x
  return x

def f2(X,Y):
  x,i = 0,0
  while i <= Y:
    if (1 - f3(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f1(X):
  x,y = 0, X
  for z in range (1,2 + 1):
    x,y = (f2(x,y) - x), (1 + y)
  return x

def f4(X):
  x,y = 1, X
  for z in range (1,(X - 2) + 1):
    x,y = (x + y), 0
  return x

def f0(X):
  return f1(X) * (f4(X) - Y)

for x in range(32):
  print (f0(x))
```

### Number of steps to fixed point of "n -> n/2 or (n+1)/2 until result is prime".	

https://oeis.org/A39637 : 1 1 1 2 1 2 1 3 2 2 1 3 1 2 4 4 1 3 1 3 2 2 1 4 2 2 3 3 1 5 1 5 2 2 4 4 1 2 4 4 1 3 1 3 2 2 1 5 3 3 3 3 1 4 4 4 2 2 1 6 1 2 6 6 3 3 1 3 5 5 1 5 1 2 3 3 5 5 1 5 2 2 1 4 2 2 4 4 1 3 3 3 2 2 6 6 1 4 4 4 1 4

size 38, time 2211066: loop2 (loop2 ((if (((loop (x * x) 1 (loop (x + x) (y div 2) 1)) + y) mod (1 + y)) <= 0 then 0 else 1) + x) (y div 2) x 1 y) y (1 + x) 1 x

K K F B K K D L C G B J J L D B L D H A B I K D L C G K B L N L B K D B K N

```
def f3(X,Y):
  x = 1
  for y in range (1,(Y // 2) + 1):
    x = x + x
  return x

def f2(X,Y):
  x = f3(X,Y)
  for y in range (1,1 + 1):
    x = x * x
  return x

def f1(X,Y):
  x,y = 1, Y
  for z in range (1,X + 1):
    x,y = ((0 if ((f2(x,y) + y) % (1 + y)) <= 0 else 1) + x), (y // 2)
  return x

def f0(X):
  x,y = 1, X
  for z in range (1,(1 + X) + 1):
    x,y = f1(x,y), y
  return x

for x in range(32):
  print (f0(x))
```

### Squares that are not the sum of 2 nonzero squares.	


https://oeis.org/A548 : 1 4 9 16 36 49 64 81 121 144 196 256 324 361 441 484 529 576 729 784 961 1024 1089 1296 1444 1764 1849 1936 2116 2209 2304 2401 2916 3136 3249 3481 3844 3969 4096 4356 4489

size 38, time 47831: loop (x * x) 1 (compr ((1 + (loop2 ((if ((((x * x) * x) + x) mod (y + y)) <= 0 then 0 else 1) + x) y (x - 1) 1 x)) mod (1 + x)) (1 + x))

K K F B B K K F K F K D L L D H A B I K D L K B E B K N D B K D H B K D M J

```
def f2(X):
  x,y = 1, X
  for z in range (1,(X - 1) + 1):
    x,y = ((0 if ((((x * x) * x) + x) % (y + y)) <= 0 else 1) + x), y
  return x

def f1(X):
  x,i = 0,0
  while i <= 1 + X:
    if ((1 + f2(x)) % (1 + x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  x = f1(X)
  for y in range (1,1 + 1):
    x = x * x
  return x

for x in range(32):
  print (f0(x))
```

### Number of symbols in Babylonian numeral representation of n.	

https://oeis.org/A131650 : 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 10 2 3 4 5 6 7 8 9 10 11 3 4 5 6 7 8 9 10 11 12 4 5 6 7 8 9 10 11 12 13 5 6 7 8 9 10 11 12 13 14 1 2 3 4 5 6 7 8 9 10 2 3 4 5 6 7 8 9 10 11 3 4

size 46, time 10182: loop (loop2 (loop2 ((y mod (2 + (2 + 2))) + x) (y div (2 + (2 + 2))) y x y) 0 1 (x mod (2 + (2 * (2 + 2)))) (x div (2 + (2 * (2 + 2))))) 1 (1 + x)

L C C C D D H K D L C C C D D G L K L N A B K C C C C D F D H K C C C C D F D G N B B K D J

```
def f2(X,Y):
  x,y = X, Y
  for z in range (1,Y + 1):
    x,y = ((y % (2 + (2 + 2))) + x), (y // (2 + (2 + 2)))
  return x

def f1(X):
  x,y = X % (2 + (2 * (2 + 2))), X // (2 + (2 * (2 + 2)))
  for z in range (1,1 + 1):
    x,y = f2(x,y), 0
  return x

def f0(X):
  x = 1 + X
  for y in range (1,1 + 1):
    x = f1(x)
  return x

for x in range(32):
  print (f0(x))
```

### Divisors of 2^30 - 1.	

https://oeis.org/A3538 : 1 3 7 9 11 21 31 33 63 77 93 99 151 217 231 279 331 341 453 651 693 993 1023 1057 1359 1661 1953 2317 2387 2979 3069 3171 3641 4681 4983 6951 7161 9513 10261 10923 11627 14043 14949 20853 21483 25487

size 28, time 3007604: 1 + (compr ((loop ((loop (x + x) x 1) - 1) 1 ((2 * (loop (x * x) 2 2)) - 2)) mod (1 + x)) x)

B K K D K B J B E B C K K F C C J F C E J B K D H K M D

```
def f3(X):
  x = 1
  for y in range (1,X + 1):
    x = x + x
  return x

def f4(X):
  x = 2
  for y in range (1,2 + 1):
    x = x * x
  return x

def f2(X):
  x = (2 * f4(X)) - 2
  for y in range (1,1 + 1):
    x = f3(x) - 1
  return x

def f1(X):
  x,i = 0,0
  while i <= X:
    if (f2(x) % (1 + x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  return 1 + f1(X)

for x in range(32):
  print (f0(x))
```

### Maximal length of rook tour on an n X n+4 board.	

https://oeis.org/A152135 : 12 36 74 134 216 328 470 650 868 1132 1442 1806 2224 2704 3246 3858 4540 5300 6138 7062 8072 9176 10374 11674 13076 14588 16210 17950 19808 21792 23902 26146 28524 31044 33706 36518 39480 42600 45878

size 22, time 15093: 2 * (loop (2 + (((2 * (((y * y) div 2) + y)) + x) + y)) (1 + x) 1)

C C C L L F C G L D F K D L D D B K D B J F

```
def f1(X):
  x = 1
  for y in range (1,(1 + X) + 1):
    x = 2 + (((2 * (((y * y) // 2) + y)) + x) + y)
  return x

def f0(X):
  return 2 * f1(X)

for x in range(32):
  print (f0(x))
```

### Number of partitions of n into at most 8 parts.	

https://oeis.org/A8637 : 1 1 2 3 5 7 11 15 22 29 40 52 70 89 116 146 186 230 288 352 434 525 638 764 919 1090 1297 1527 1801 2104 2462 2857 3319 3828 4417 5066 5812 6630 7564 8588 9749 11018 12450 14012 15765 17674 19805 22122

size 118, time 275220: loop2 (loop2 (loop2 (loop2 (loop2 (1 + ((((y * y) + y) div (1 + (2 + 2))) + x)) (((y - 2) - 2) - 2) (1 + (y div (2 + (2 + 2)))) x y) (((y - 2) - 2) - 2) (1 + (y div (2 + (2 + 2)))) x y) ((((y - 2) - 2) - 2) - 2) (1 + (y div (2 * (2 + 2)))) x y) ((((y - 1) - 2) - 2) - 2) (1 + (y div (1 + (2 + (2 + 2))))) x y) ((((y - 2) - 2) - 2) - 2) (1 + (x div (2 * (2 + 2)))) 0 x

B L L F L D B C C D D G K D D L C E C E C E B L C C C D D G D K L N L C E C E C E B L C C C D D G D K L N L C E C E C E C E B L C C C D F G D K L N L B E C E C E C E B L B C C C D D D G D K L N L C E C E C E C E B K C C C D F G D A K N

```
def f4(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + (2 + 2)))) + 1):
    x,y = (1 + ((((y * y) + y) // (1 + (2 + 2))) + x)), (((y - 2) - 2) - 2)
  return x

def f3(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + (2 + 2)))) + 1):
    x,y = f4(x,y), (((y - 2) - 2) - 2)
  return x

def f2(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 * (2 + 2)))) + 1):
    x,y = f3(x,y), ((((y - 2) - 2) - 2) - 2)
  return x

def f1(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 + (2 + 2))))) + 1):
    x,y = f2(x,y), ((((y - 1) - 2) - 2) - 2)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,(1 + (X // (2 * (2 + 2)))) + 1):
    x,y = f1(x,y), ((((y - 2) - 2) - 2) - 2)
  return x

for x in range(32):
  print (f0(x))
```

### A Jacobsthal triangle.	

https://oeis.org/A113953 : 1 0 1 0 2 1 0 0 4 1 0 0 4 6 1 0 0 0 12 8 1 0 0 0 8 24 10 1 0 0 0 0 32 40 12 1 0 0 0 0 16 80 60 14 1 0 0 0 0 0 80 160 84 16 1 0 0 0 0 0 32 240 280 112 18 1 0 0 0 0 0 0 192 560 448 144 20 1 0 0 0 0 0 0 64 672 1120 672 180 22 1

size 53, time 104286: (loop2 (2 * (x * y)) (y - 1) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (x - (if (y - x) <= 0 then y else 0)) x x)) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)

C K L F F L B E A K K A B L D I E K K J E B K L K E L A I E K K J N K L F A K K A B L D I E K K J E B J G

```
def f2(X):
  x = X
  for y in range (1,X + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f3(X):
  x = X
  for y in range (1,X + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f1(X):
  x,y = 1, f3(X)
  for z in range (1,(0 - f2(X)) + 1):
    x,y = (2 * (x * y)), (y - 1)
  return x

def f5(X):
  x = X
  for y in range (1,X + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f4(X):
  x = 1
  for y in range (1,(0 - f5(X)) + 1):
    x = x * y
  return x

def f0(X):
  return f1(X) // f4(X)

for x in range(32):
  print (f0(x))
```

### Unique monotonic sequence of nonnegative integers satisfying a(a(n)) = 3n.

"a subject of the 5th problem of the 27th British Mathematical Olympiad in 1992" described in A. Gardiner, The Mathematical Olympiad Handbook: An Introduction to Problem Solving" (the problem was to find f(1992) ). 

https://oeis.org/A3605 : 0 2 3 6 7 8 9 12 15 18 19 20 21 22 23 24 25 26 27 30 33 36 39 42 45 48 51 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 84 87 90 93 96 99 102 105 108 111 114 117 120

size 31, time 121597: (x + x) - (loop ((loop (0 - 1) ((loop (loop y (x div (1 + 2)) x) (1 + 2) y) - 1) 1) + x) (x - 1) 0)

K K D A B E L K B C D G K J B C D L J B E B J K D K B E A J E

The invented program is wrong. Here is the explanation:

My Python program gives a different answer: 3789 . The "mistake" that the program generator did was introducing the constant 3 in f3 in the python code. But it should be an infinite loop. f3 is supposed to find the first digit of a given number Y written in ternary. But currently, it performs at most 3 divisions, so it fails to calculate correctly f3(X,81) -- it is supposed to be 1, but
the program outputs 3. Therefore, the generated function f0(82) = 165 whereas the correct f(82) = 163.

The code:
```
def f(x):
     if x == 0: return 0
     a = 1
     while a <= x: a *= 3
     if x >= 2 * a // 3: return 3*x - a
     else: return x + a // 3

print(*(f(x) for x in range(100)))

for x in range(10000):
     assert f(x) < f(x+1)
     assert f(f(x)) == 3*x

print(f(1992))
```

The invented Python code:
```
def f4(X):
  x = X
  for y in range (1,(X // (1 + 2)) + 1):
    x = y
  return x

def f3(X,Y):
  x = Y
  for y in range (1,(1 + 2) + 1):
    x = f4(x)
  return x

def f2(X,Y):
  x = 1
  for y in range (1,(f3(X,Y) - 1) + 1):
    x = 0 - 1
  return x

def f1(X):
  x = 0
  for y in range (1,(X - 1) + 1):
    x = f2(x,y) + x
  return x

def f0(X):
  return (X + X) - f1(X)

for x in range(32):
  print (f0(x))
```

### Numbers n that are not coprime to the numerator of zeta(2\*n)/(Pi^(2\*n)).	

https://oeis.org/A266214 : 14 22 26 28 30 38 42 44 46 50 52 54 56 58 60 62 70 74 76 78 82 84 86 88 90 92 94 98 100 102 104 106 108 110 112 114 116 118 120 122 124 126 134 138 140 142 146 148 150 152 154 156 158 162 164 166 168 170

size 29, time 92515: 2 * (compr ((loop2 ((((if (2 - x) <= 0 then 0 else 1) + x) * (y mod 2)) + x) (y div 2) x 0 x) mod 2) (1 + x))

C C K E A B I K D L C H F K D L C G K A K N C H B K D M F

```
def f2(X):
  x,y = 0, X
  for z in range (1,X + 1):
    x,y = ((((0 if (2 - x) <= 0 else 1) + x) * (y % 2)) + x), (y // 2)
  return x

def f1(X):
  x,i = 0,0
  while i <= 1 + X:
    if (f2(x) % 2) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  return 2 * f1(X)

for x in range(32):
  print (f0(x))
```

### Molien series for invariants of finite Coxeter group A_9.	

https://oeis.org/A266778 : 1 0 1 1 2 2 4 4 7 8 12 13 20 22 31 36 48 55 73 83 107 123 154 177 220 251 306 351 422 481 575 652 771 875 1024 1158 1348 1518 1754 1973 2265 2538 2901 3241 3684 4109 4646 5167 5823 6457 7246 8020 8965 9898 11031 12150 13495 14837 16428 18022 19905 21789 23999 26228 28813

size 156, time 5616664: loop2 (loop2 (loop2 (loop2 (loop2 (loop2 ((loop ((2 + (loop ((y div 2) + x) x x)) div (1 + 2)) 1 (loop (y - x) y 1)) + x) (((y - 1) - 2) - 2) (1 + (y div (1 + (2 + 2)))) x y) (((y - 2) - 2) - 2) (1 + (y div (2 + (2 + 2)))) x y) ((((y - 1) - 2) - 2) - 2) (1 + (y div (1 + (2 + (2 + 2))))) x y) ((((y - 2) - 2) - 2) - 2) (1 + (y div (2 * (2 + 2)))) x y) (((((y - 1) - 2) - 2) - 2) - 2) (1 + (y div (1 + (2 * (2 + 2))))) x y) (((((y - 2) - 2) - 2) - 2) - 2) (1 + (x div (2 + (2 * (2 + 2))))) 0 x

C L C G K D K K J D B C D G B L K E L B J J K D L B E C E C E B L B C C D D G D K L N L C E C E C E B L C C C D D G D K L N L B E C E C E C E B L B C C C D D D G D K L N L C E C E C E C E B L C C C D F G D K L N L B E C E C E C E C E B L B C C C D F D G D K L N L C E C E C E C E C E B K C C C C D F D G D A K N

```
def f7(X):
  x = X
  for y in range (1,X + 1):
    x = (y // 2) + x
  return x

def f8(X,Y):
  x = 1
  for y in range (1,Y + 1):
    x = y - x
  return x

def f6(X,Y):
  x = f8(X,Y)
  for y in range (1,1 + 1):
    x = (2 + f7(x)) // (1 + 2)
  return x

def f5(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 + 2)))) + 1):
    x,y = (f6(x,y) + x), (((y - 1) - 2) - 2)
  return x

def f4(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + (2 + 2)))) + 1):
    x,y = f5(x,y), (((y - 2) - 2) - 2)
  return x

def f3(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 + (2 + 2))))) + 1):
    x,y = f4(x,y), ((((y - 1) - 2) - 2) - 2)
  return x

def f2(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 * (2 + 2)))) + 1):
    x,y = f3(x,y), ((((y - 2) - 2) - 2) - 2)
  return x

def f1(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 * (2 + 2))))) + 1):
    x,y = f2(x,y), (((((y - 1) - 2) - 2) - 2) - 2)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,(1 + (X // (2 + (2 * (2 + 2))))) + 1):
    x,y = f1(x,y), (((((y - 2) - 2) - 2) - 2) - 2)
  return x

for x in range(32):
  print (f0(x))
```

### Solution to Tower of Hanoi puzzle encoded in pairs with the moves (1,2),(2,3),(3,1),(2,1),(3,2),(1,3). The disks are moved from peg 1 to 2. For a tower of k disks use the first 2^k-1 number pairs.	

https://oeis.org/A101608 : 1 2 1 3 2 3 1 2 3 1 3 2 1 2 1 3 2 3 2 1 3 1 2 3 1 2 1 3 2 3 1 2 3 1 3 2 1 2 3 1 2 3 2 1 3 1 3 2 1 2 1 3 2 3 1 2 3 1 3 2 1 2 1 3 2 3 2 1 3 1 2 3 1 2 1 3 2 3 2 1 3 1 3 2 1 2 3 1 2 3 2 1 3 1 2 3 1 2 1 3 2 3

size 103, time 9878: 1 + ((loop2 (((loop2 (loop (loop2 (2 + (loop (loop2 (loop2 (2 + (loop (loop2 (loop2 (loop2 ((if y <= 0 then 0 else 1) + x) (y div 2) ((2 * (y mod (2 + 2))) - 1) 2 y) 0 (y mod 2) 2 y) 0 (x mod 2) 1 (x div 2)) 1 (y div 2))) 0 (y mod 2) 2 y) 0 (x mod 2) 1 (x div 2)) 1 (y div 2))) 0 (x mod 2) 2 x) 1 (y div 2)) 0 (y mod 2) 0 y) mod 2) - x) (1 + y) 2 x x) mod (1 + 2))

B C C L A B I K D L C G C L C C D H F B E C L N A L C H C L N A K C H B K C G N B L C G J D A L C H C L N A K C H B K C G N B L C G J D A K C H C K N B L C G J A L C H A L N C H K E B L D C K K N B C D H D

```
def f11(X,Y):
  x,y = 2, Y
  for z in range (1,((2 * (Y % (2 + 2))) - 1) + 1):
    x,y = ((0 if y <= 0 else 1) + x), (y // 2)
  return x

def f10(X,Y):
  x,y = 2, Y
  for z in range (1,(Y % 2) + 1):
    x,y = f11(x,y), 0
  return x

def f9(X):
  x,y = 1, X // 2
  for z in range (1,(X % 2) + 1):
    x,y = f10(x,y), 0
  return x

def f8(X,Y):
  x = Y // 2
  for y in range (1,1 + 1):
    x = f9(x)
  return x

def f7(X,Y):
  x,y = 2, Y
  for z in range (1,(Y % 2) + 1):
    x,y = (2 + f8(x,y)), 0
  return x

def f6(X):
  x,y = 1, X // 2
  for z in range (1,(X % 2) + 1):
    x,y = f7(x,y), 0
  return x

def f5(X,Y):
  x = Y // 2
  for y in range (1,1 + 1):
    x = f6(x)
  return x

def f4(X):
  x,y = 2, X
  for z in range (1,(X % 2) + 1):
    x,y = (2 + f5(x,y)), 0
  return x

def f3(X,Y):
  x = Y // 2
  for y in range (1,1 + 1):
    x = f4(x)
  return x

def f2(X,Y):
  x,y = 0, Y
  for z in range (1,(Y % 2) + 1):
    x,y = f3(x,y), 0
  return x

def f1(X):
  x,y = X, X
  for z in range (1,2 + 1):
    x,y = ((f2(x,y) % 2) - x), (1 + y)
  return x

def f0(X):
  return 1 + (f1(X) % (1 + 2))

for x in range(32):
  print (f0(x))
```

### Sierpiński's triangle, read by rows, starting from 1: T(n,k) = (T(n-1,k) + T(n-1,k-1)) mod 2.	

https://oeis.org/A90971 : 1 0 1 1 1 1 0 0 0 1 1 0 0 1 1 0 1 0 1 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1

size 84, time 43540: ((loop2 ((if y <= 0 then 0 else (1 + y)) * x) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1)) mod 2

L A B L D I K F B L D A K K A B L D I E C K B C C D D G D K J E B B K L K E L A I E C K B C C D D G D K J D N K L F A K K A B L D I E C K B C C D D G D K J E B J G C H

size 91, time 37485: ((loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (1 + (2 + (x div (1 + (2 + (2 + 2)))))) x)) 1 (2 + (loop (x - (if (y - x) <= 0 then y else 0)) (1 + (2 + (x div (1 + (2 + (2 + 2)))))) x))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (1 + (2 + (x div (1 + (2 + (2 + 2)))))) x)) 1)) mod 2

K L F B L D A K K A B L D I E B C K B C C C D D D G D D K J E B C K L K E L A I E B C K B C C C D D D G D D K J D N K L F A K K A B L D I E B C K B C C C D D D G D D K J E B J G C H


```
def f2(X):
  x = X
  for y in range (1,(1 + (2 + (X // (1 + (2 + (2 + 2)))))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f3(X):
  x = X
  for y in range (1,(1 + (2 + (X // (1 + (2 + (2 + 2)))))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f1(X):
  x,y = 1, 2 + f3(X)
  for z in range (1,(0 - f2(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f5(X):
  x = X
  for y in range (1,(1 + (2 + (X // (1 + (2 + (2 + 2)))))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f4(X):
  x = 1
  for y in range (1,(0 - f5(X)) + 1):
    x = x * y
  return x

def f0(X):
  return (f1(X) // f4(X)) % 2

for x in range(32):
  print (f0(x))
```

### a(1) = 1; if a(n-1) + n is prime then a(n) = a(n-1) + n, else a(n) = a(n-1).	

https://oeis.org/A83743 : 1 3 3 7 7 13 13 13 13 23 23 23 23 37 37 53 53 71 71 71 71 71 71 71 71 97 97 97 97 127 127 127 127 127 127 163 163 163 163 163 163 163 163 163 163 163 163 211 211 211 211 263 263 317 317 373 373 431 431 491

size 32, time 1179046: loop (loop ((if ((y * y) mod x) <= 0 then 1 else 0) + x) (loop2 (1 + (if (x mod (1 + y)) <= 0 then 0 else x)) (y - 1) y x y) x) x 1

L L F K H B A I K D B K B L D H A K I D L B E L K L N K J K B J

```
def f2(X,Y):
  x,y = X, Y
  for z in range (1,Y + 1):
    x,y = (1 + (0 if (x % (1 + y)) <= 0 else x)), (y - 1)
  return x

def f1(X,Y):
  x = X
  for y in range (1,f2(X,Y) + 1):
    x = (1 if ((y * y) % x) <= 0 else 0) + x
  return x

def f0(X):
  x = 1
  for y in range (1,X + 1):
    x = f1(x,y)
  return x

for x in range(32):
  print (f0(x))
```

### Order of Burnside group B(6,n) of exponent 6 and rank n.	

https://oeis.org/A79683 : 1 6 227442304239437611008

size 26, time 642: (1 + (loop2 ((loop (2 * ((x + x) + x)) x 1) * (loop (x + x) y x)) 2 x 1 x)) div 2

B C K K D K D F K B J K K D L K J F C K B K N D C G

```
def f2(X):
  x = 1
  for y in range (1,X + 1):
    x = 2 * ((x + x) + x)
  return x

def f3(X,Y):
  x = X
  for y in range (1,Y + 1):
    x = x + x
  return x

def f1(X):
  x,y = 1, X
  for z in range (1,X + 1):
    x,y = (f2(x) * f3(x,y)), 2
  return x

def f0(X):
  return (1 + f1(X)) // 2

for x in range(32):
  print (f0(x))
```

### a(n) is the number of unitary divisors of n (d such that d divides n, gcd(d, n/d) = 1).	

https://oeis.org/A34444 : 1 2 2 2 2 4 2 2 2 4 2 4 2 4 4 2 2 4 2 4 4 4 2 4 2 4 2 4 2 8 2 2 4 4 4 4 2 4 4 4 2 8 2 4 4 4 2 4 2 4 4 4 2 4 4 4 4 4 2 8 2 4 4 2 4 8 2 4 4 8 2 4 2 4 4 4 4 8 2 4 2 4 2 8 4 4 4 4 2 8 4 4 4 4 4 4 2 4 4 4 2 8 2 4 8

size 25, time 115920: (loop2 ((if (((x * x) + x) mod (1 + y)) <= 0 then (2 + y) else 1) + x) y x 1 x) div (1 + x)

K K F K D B L D H C L D B I K D L K B K N B K D G

```
def f1(X):
  x,y = 1, X
  for z in range (1,X + 1):
    x,y = (((2 + y) if (((x * x) + x) % (1 + y)) <= 0 else 1) + x), y
  return x

def f0(X):
  return f1(X) // (1 + X)

for x in range(32):
  print (f0(x))
```

### Number of partitions of n in which any two parts differ by at most 7.

https://oeis.org/A218509 : 1 1 2 3 5 7 11 15 22 30 41 54 72 93 120 153 194 242 302 372 457 556 675 812 975 1162 1381 1632 1923 2254 2636 3068 3562 4119 4752 5462 6265 7162 8170 9293 10549 11942 13495 15211 17115 19214 21534 24083 26892

size 127, time 3448752: loop (loop2 (loop2 (loop2 (loop2 (loop2 (1 + ((((y * y) + y) div (1 + (2 + 2))) + x)) (((y - 2) - 2) - 2) (1 + (y div (2 + (2 + 2)))) x y) (((y - 2) - 2) - 2) (1 + (y div (2 + (2 + 2)))) x y) ((((y - 1) - 2) - 2) - 2) (1 + (y div (1 + (2 + (2 + 2))))) x y) ((((y - 2) - 2) - 2) - 2) (1 + (y div (2 * (2 + 2)))) x y) ((((y - 1) - 2) - 2) - 2) (1 + (y div (1 + (2 + (2 + 2))))) 0 (1 + y)) (x - 1) 1

B L L F L D B C C D D G K D D L C E C E C E B L C C C D D G D K L N L C E C E C E B L C C C D D G D K L N L B E C E C E C E B L B C C C D D D G D K L N L C E C E C E C E B L C C C D F G D K L N L B E C E C E C E B L B C C C D D D G D A B L D N K B E B J


```
def f5(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + (2 + 2)))) + 1):
    x,y = (1 + ((((y * y) + y) // (1 + (2 + 2))) + x)), (((y - 2) - 2) - 2)
  return x

def f4(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + (2 + 2)))) + 1):
    x,y = f5(x,y), (((y - 2) - 2) - 2)
  return x

def f3(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 + (2 + 2))))) + 1):
    x,y = f4(x,y), ((((y - 1) - 2) - 2) - 2)
  return x

def f2(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 * (2 + 2)))) + 1):
    x,y = f3(x,y), ((((y - 2) - 2) - 2) - 2)
  return x

def f1(X,Y):
  x,y = 0, 1 + Y
  for z in range (1,(1 + (Y // (1 + (2 + (2 + 2))))) + 1):
    x,y = f2(x,y), ((((y - 1) - 2) - 2) - 2)
  return x

def f0(X):
  x = 1
  for y in range (1,(X - 1) + 1):
    x = f1(x,y)
  return x

for x in range(32):
  print (f0(x))
```

### Triangle T(n,k) of coefficients relating to Bezier curve continuity.	

https://oeis.org/A65109 : 1 2 ~1 4 ~4 1 8 ~12 6 ~1 16 ~32 24 ~8 1 32 ~80 80 ~40 10 ~1 64 ~192 240 ~160 60 ~12 1 128 ~448 672 ~560 280 ~84 14 ~1 256 ~1024 1792 ~1792 1120 ~448 112 ~16 1 512 ~2304 4608 ~5376 4032 ~2016 672 ~144 18 ~1 1024 ~5120 11520 ~15360 13440

size 120, time 21572: (loop (0 - x) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x) 1) * ((loop2 (2 * (x * y)) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1))

A K E K L K E L A I E C C K B C C C D F D G D D K J B J C K L F F B L D A K K A B L D I E C C K B C C C D F D G D D K J E B B K L K E L A I E C C K B C C C D F D G D D K J D N K L F A K K A B L D I E C C K B C C C D F D G D D K J E B J G F

```
def f2(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f1(X):
  x = 1
  for y in range (1,f2(X) + 1):
    x = 0 - x
  return x

def f4(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f5(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f3(X):
  x,y = 1, 1 + f5(X)
  for z in range (1,(0 - f4(X)) + 1):
    x,y = (2 * (x * y)), (1 + y)
  return x

def f7(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f6(X):
  x = 1
  for y in range (1,(0 - f7(X)) + 1):
    x = x * y
  return x

def f0(X):
  return f1(X) * (f3(X) // f6(X))

for x in range(32):
  print (f0(x))
```

### Triangle read by rows, Sierpinski's gasket, A047999 \* (1,2,4,8,...) diagonalized.	

https://oeis.org/A166555 : 1 1 2 1 0 4 1 2 4 8 1 0 0 0 16 1 2 0 0 16 32 1 0 4 0 16 0 64 1 2 4 8 16 32 64 128 1 0 0 0 0 0 0 0 256 1 2 0 0 0 0 0 0 256 512 1 0 4 0 0 0 0 0 256 0 1024

size 120, time 24408: (loop (x + x) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x) 1) * (((loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1)) mod 2)

K K D K L K E L A I E C C K B C C C D F D G D D K J B J K L F B L D A K K A B L D I E C C K B C C C D F D G D D K J E B B K L K E L A I E C C K B C C C D F D G D D K J D N K L F A K K A B L D I E C C K B C C C D F D G D D K J E B J G C H F

```
def f2(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f1(X):
  x = 1
  for y in range (1,f2(X) + 1):
    x = x + x
  return x

def f4(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f5(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f3(X):
  x,y = 1, 1 + f5(X)
  for z in range (1,(0 - f4(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f7(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f6(X):
  x = 1
  for y in range (1,(0 - f7(X)) + 1):
    x = x * y
  return x

def f0(X):
  return f1(X) * ((f3(X) // f6(X)) % 2)

for x in range(32):
  print (f0(x))
```

### A masked Pascal triangle.	

https://oeis.org/A119467 : 1 0 1 1 0 1 0 3 0 1 1 0 6 0 1 0 5 0 10 0 1 1 0 15 0 15 0 1 0 7 0 35 0 21 0 1 1 0 28 0 70 0 28 0 1 0 9 0 84 0 126 0 36 0 1 1 0 45 0 210 0 210 0 45 0 1 0 11 0 165 0 462 0 330 0 55 0 1 1 0 66 0 495 0 924

size 104, time 38188: (loop (1 - x) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1) * ((loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1))

B K E A K K A B L D I E C K B C C D D G D K J E B J K L F B L D A K K A B L D I E C K B C C D D G D K J E B B K L K E L A I E C K B C C D D G D K J D N K L F A K K A B L D I E C K B C C D D G D K J E B J G F

```
def f2(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f1(X):
  x = 1
  for y in range (1,(0 - f2(X)) + 1):
    x = 1 - x
  return x

def f4(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f5(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f3(X):
  x,y = 1, 1 + f5(X)
  for z in range (1,(0 - f4(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f7(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f6(X):
  x = 1
  for y in range (1,(0 - f7(X)) + 1):
    x = x * y
  return x

def f0(X):
  return f1(X) * (f3(X) // f6(X))

for x in range(32):
  print (f0(x))
```

### Numbers that are the sum of two powers of 12.	

https://oeis.org/A194887 : 2 13 24 145 156 288 1729 1740 1872 3456 20737 20748 20880 22464 41472 248833 248844 248976 250560 269568 497664 2985985 2985996 2986128 2987712 3006720 3234816 5971968 35831809 35831820 35831952 35833536 35852544 36080640

size 63, time 5316: loop (2 * (2 * ((x + x) + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) (1 + (loop (2 * (2 * ((x + x) + x))) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1))

C C K K D K D F F K L K E L A I E C K B C C D D G D K J B C C K K D K D F F A K K A B L D I E C K B C C D D G D K J E B J D J

```
def f1(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f3(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f2(X):
  x = 1
  for y in range (1,(0 - f3(X)) + 1):
    x = 2 * (2 * ((x + x) + x))
  return x

def f0(X):
  x = 1 + f2(X)
  for y in range (1,f1(X) + 1):
    x = 2 * (2 * ((x + x) + x))
  return x

for x in range(32):
  print (f0(x))
```

### Central factorial numbers.

https://oeis.org/A1824 : 1 10 259 12916 1057221 128816766 21878089479 4940831601000 1432009163039625 518142759828635250 228929627246078500875 121292816354463333793500 75908014254880833434338125 55399444912646408707007883750 46636497509226736668824289999375

size 28, time 14103: loop (((loop (x * x) 1 (1 + (y + y))) * x) + (loop2 ((x * y) * y) (2 + y) y 1 1)) x 1

K K F B B L L D D J K F K L F L F C L D L B B N D K B J

```
def f1(X,Y):
  x = 1 + (Y + Y)
  for y in range (1,1 + 1):
    x = x * x
  return x

def f2(X,Y):
  x,y = 1, 1
  for z in range (1,Y + 1):
    x,y = ((x * y) * y), (2 + y)
  return x

def f0(X):
  x = 1
  for y in range (1,X + 1):
    x = (f1(x,y) * x) + f2(x,y)
  return x

for x in range(32):
  print (f0(x))
```

### Number of inequivalent ways to color faces of a cube using at most n colors.

https://oeis.org/A47780 : 0 1 10 57 240 800 2226 5390 11712 23355 43450 76351 127920 205842 319970 482700 709376 1018725 1433322 1980085 2690800 3602676 4758930 6209402 8011200 10229375 12937626 16219035 20166832 24885190 30490050

size 24, time 151776: loop2 ((((y * y) + y) div 2) + x) (y - 1) (x * x) 0 (((x * x) + x) div 2)

L L F L D C G K D L B E K K F A K K F K D C G N

```
def f0(X):
  x,y = 0, ((X * X) + X) // 2
  for z in range (1,(X * X) + 1):
    x,y = ((((y * y) + y) // 2) + x), (y - 1)
  return x

for x in range(32):
  print (f0(x))
```

### Number of partitions of n into at most 11 parts.

https://oeis.org/A8640 : 1 1 2 3 5 7 11 15 22 30 42 56 76 99 131 169 219 278 355 445 560 695 863 1060 1303 1586 1930 2331 2812 3370 4035 4802 5708 6751 7972 9373 11004 12866 15021 17475 20298 23501 27169 31316 36043 41373 47420 54218 61903 70515 80215 91058 103226 116792 131970 148847

size 197, time 2214281: loop2 (loop2 (loop2 (loop2 (loop2 (loop2 (loop2 (loop2 (1 + ((((y * y) + y) div (1 + (2 + 2))) + x)) (((y - 2) - 2) - 2) (1 + (y div (2 + (2 + 2)))) x y) (((y - 2) - 2) - 2) (1 + (y div (2 + (2 + 2)))) x y) ((((y - 1) - 2) - 2) - 2) (1 + (y div (1 + (2 + (2 + 2))))) x y) ((((y - 2) - 2) - 2) - 2) (1 + (y div (2 * (2 + 2)))) x y) (((((y - 1) - 2) - 2) - 2) - 2) (1 + (y div (1 + (2 * (2 + 2))))) x y) ((((y - 2) - 2) - 2) - 2) (1 + (y div (2 * (2 + 2)))) x y) (((((y - 2) - 2) - 2) - 2) - 2) (1 + (y div (2 + (2 * (2 + 2))))) x y) ((((((y - 1) - 2) - 2) - 2) - 2) - 2) (1 + (x div (1 + (2 + (2 * (2 + 2)))))) 0 x

B L L F L D B C C D D G K D D L C E C E C E B L C C C D D G D K L N L C E C E C E B L C C C D D G D K L N L B E C E C E C E B L B C C C D D D G D K L N L C E C E C E C E B L C C C D F G D K L N L B E C E C E C E C E B L B C C C D F D G D K L N L C E C E C E C E B L C C C D F G D K L N L C E C E C E C E C E B L C C C C D F D G D K L N L B E C E C E C E C E C E B K B C C C C D F D D G D A K N

```
def f7(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + (2 + 2)))) + 1):
    x,y = (1 + ((((y * y) + y) // (1 + (2 + 2))) + x)), (((y - 2) - 2) - 2)
  return x

def f6(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + (2 + 2)))) + 1):
    x,y = f7(x,y), (((y - 2) - 2) - 2)
  return x

def f5(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 + (2 + 2))))) + 1):
    x,y = f6(x,y), ((((y - 1) - 2) - 2) - 2)
  return x

def f4(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 * (2 + 2)))) + 1):
    x,y = f5(x,y), ((((y - 2) - 2) - 2) - 2)
  return x

def f3(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 * (2 + 2))))) + 1):
    x,y = f4(x,y), (((((y - 1) - 2) - 2) - 2) - 2)
  return x

def f2(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 * (2 + 2)))) + 1):
    x,y = f3(x,y), ((((y - 2) - 2) - 2) - 2)
  return x

def f1(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + (2 * (2 + 2))))) + 1):
    x,y = f2(x,y), (((((y - 2) - 2) - 2) - 2) - 2)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,(1 + (X // (1 + (2 + (2 * (2 + 2)))))) + 1):
    x,y = f1(x,y), ((((((y - 1) - 2) - 2) - 2) - 2) - 2)
  return x

for x in range(32):
  print (f0(x))
```

### The (1,2)-Pascal triangle (or Lucas triangle) read by rows.	

https://oeis.org/A29635 : 2 1 2 1 3 2 1 4 5 2 1 5 9 7 2 1 6 14 16 9 2 1 7 20 30 25 11 2 1 8 27 50 55 36 13 2 1 9 35 77 105 91 49 15 2 1 10 44 112 182 196 140 64 17 2 1 11 54 156 294 378 336 204 81 19 2 1 12 65 210 450 672 714 540 285 100

size 177, time 44222: ((loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1)) + ((loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1))

K L F B L D A K K A B L D I E C C K B C C C D F D G D D K J E B K L K E L A I E C C K B C C C D F D G D D K J N K L F A K K A B L D I E C C K B C C C D F D G D D K J E B J G K L F B L D A K K A B L D I E C C K B C C C D F D G D D K J E B B K L K E L A I E C C K B C C C D F D G D D K J D N K L F A K K A B L D I E C C K B C C C D F D G D D K J E B J G D

size 103, time 179073: ((loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop (y - 1) (x - y) x) x x)) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)) + ((loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (x - (if (y - x) <= 0 then y else 0)) x x)) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1))

K L F B L D A K K A B L D I E K K J E B L B E K L E K J K K J N K L F A K K A B L D I E K K J E B J G K L F B L D A K K A B L D I E K K J E B K L K E L A I E K K J N K L F A K K A B L D I E K K J E B J G D

```
def f2(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f3(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f1(X):
  x,y = 1, f3(X)
  for z in range (1,(0 - f2(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f5(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f4(X):
  x = 1
  for y in range (1,(0 - f5(X)) + 1):
    x = x * y
  return x

def f7(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f8(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f6(X):
  x,y = 1, 1 + f8(X)
  for z in range (1,(0 - f7(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f10(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f9(X):
  x = 1
  for y in range (1,(0 - f10(X)) + 1):
    x = x * y
  return x

def f0(X):
  return (f1(X) // f4(X)) + (f6(X) // f9(X))

for x in range(32):
  print (f0(x))
```

### Rows of Fibonacci-Pascal triangle.	

https://oeis.org/A45995 : 1 1 1 1 1 1 1 2 2 1 1 3 8 3 1 1 5 55 55 5 1 1 8 610 6765 610 8 1 1 13 10946 9227465 9227465 10946 13 1 1 21 317811 225851433717 190392490709135 225851433717 317811 21 1 1 34 14930352

size 61, time 40976: loop (loop2 (x + y) x x 0 1) 1 ((loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop (y - 1) (x - y) x) x x)) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1))

K L D K K A B N B K L F B L D A K K A B L D I E K K J E B L B E K L E K J K K J N K L F A K K A B L D I E K K J E B J G J

```
def f1(X):
  x,y = 0, 1
  for z in range (1,X + 1):
    x,y = (x + y), x
  return x

def f3(X):
  x = X
  for y in range (1,X + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f5(X,Y):
  x = X
  for y in range (1,(X - Y) + 1):
    x = y - 1
  return x

def f4(X):
  x = X
  for y in range (1,X + 1):
    x = f5(x,y)
  return x

def f2(X):
  x,y = 1, f4(X)
  for z in range (1,(0 - f3(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f7(X):
  x = X
  for y in range (1,X + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f6(X):
  x = 1
  for y in range (1,(0 - f7(X)) + 1):
    x = x * y
  return x

def f0(X):
  x = f2(X) // f6(X)
  for y in range (1,1 + 1):
    x = f1(x)
  return x

for x in range(32):
  print (f0(x))
```

### Number of restricted 3 X 3 matrices with row and column sums n.

https://oeis.org/A5045 : 0 0 1 3 6 10 17 25 37 51 70 92 121 153 194 240 296 358 433 515 612 718 841 975 1129 1295 1484 1688 1917 2163 2438 2732 3058 3406 3789 4197 4644 5118 5635 6183 6777 7405 8084 8800 9571 10383 11254

size 45, time 85460: loop2 (((loop2 (1 + (((((y * y) div (1 + 2)) + y) div 2) + x)) ((y - 2) - 2) (1 + (y div (2 + 2))) 0 y) - 1) + x) (y - 2) (1 + (x div 2)) 0 x

B L L F B C D G L D C G K D D L C E C E B L C C D G D A L N B E K D L C E B K C G D A K N

```
def f1(X,Y):
  x,y = 0, Y
  for z in range (1,(1 + (Y // (2 + 2))) + 1):
    x,y = (1 + (((((y * y) // (1 + 2)) + y) // 2) + x)), ((y - 2) - 2)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,(1 + (X // 2)) + 1):
    x,y = ((f1(x,y) - 1) + x), (y - 2)
  return x

for x in range(32):
  print (f0(x))
```

### Fermat coefficients.

https://oeis.org/A971 : 1 9 42 132 334 728 1428 2584 4389 7084 10963 16380 23751 33563 46376 62832 83657 109668 141778 181001 228459 285384 353127 433160 527085 636636 763686 910252 1078500 1270752 1489488 1737355 2017169 2331924

size 24, time 17408: ((loop (((2 * ((x + x) + x)) div y) + x) (x + x) 1) + x) div (1 + (x + x))

C K K D K D F L G K D K K D B J K D B K K D D G

```
def f1(X):
  x = 1
  for y in range (1,(X + X) + 1):
    x = ((2 * ((x + x) + x)) // y) + x
  return x

def f0(X):
  return (f1(X) + X) // (1 + (X + X))

for x in range(32):
  print (f0(x))
```

### Pseudoperfect (or semiperfect) numbers n: some subset of the proper divisors of n sums to n.

https://oeis.org/A5835 : 6 12 18 20 24 28 30 36 40 42 48 54 56 60 66 72 78 80 84 88 90 96 100 102 104 108 112 114 120 126 132 138 140 144 150 156 160 162 168 174 176 180 186 192 196 198 200 204 208 210 216 220 222 224 228 234 240 246 252 258 260 264

size 25, time 524622: compr (x mod (loop2 ((if (y mod x) <= 0 then 0 else 1) + x) (y - x) (x - 1) 2 (x - 1))) (1 + x)

K L K H A B I K D L K E K B E C K B E N H B K D M

```
def f1(X):
  x,y = 2, X - 1
  for z in range (1,(X - 1) + 1):
    x,y = ((0 if (y % x) <= 0 else 1) + x), (y - x)
  return x

def f0(X):
  x,i = 0,0
  while i <= 1 + X:
    if (x % f1(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

for x in range(32):
  print (f0(x))
```

### Molien series for invariants of finite Coxeter group D_10 (bisected).	

https://oeis.org/A266773 : 1 1 2 3 5 8 12 17 25 35 49 66 90 119 158 206 267 342 437 551 694 865 1074 1324 1627 1985 2414 2919 3518 4219 5045 6003 7125 8422 9927 11660 13660 15949 18578 21575 24998 28884 33303 38298 43955 50329 57513 65581 74645 84786

size 162, time 1243175: loop2 (loop2 (loop2 (loop2 (loop2 (loop2 (loop2 (1 + ((((y * y) + y) div (1 + (2 + 2))) + x)) (((y - 1) - 2) - 2) (1 + (y div (1 + (2 + 2)))) x y) (((y - 2) - 2) - 2) (1 + (y div (2 + (2 + 2)))) x y) (((y - 2) - 2) - 2) (1 + (y div (2 + (2 + 2)))) x y) ((((y - 1) - 2) - 2) - 2) (1 + (y div (1 + (2 + (2 + 2))))) x y) ((((y - 2) - 2) - 2) - 2) (1 + (y div (2 * (2 + 2)))) x y) (((((y - 1) - 2) - 2) - 2) - 2) (1 + (y div (1 + (2 * (2 + 2))))) x y) ((((y - 2) - 2) - 2) - 2) (1 + (x div (2 * (2 + 2)))) 0 x

B L L F L D B C C D D G K D D L B E C E C E B L B C C D D G D K L N L C E C E C E B L C C C D D G D K L N L C E C E C E B L C C C D D G D K L N L B E C E C E C E B L B C C C D D D G D K L N L C E C E C E C E B L C C C D F G D K L N L B E C E C E C E C E B L B C C C D F D G D K L N L C E C E C E C E B K C C C D F G D A K N

```
def f6(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 + 2)))) + 1):
    x,y = (1 + ((((y * y) + y) // (1 + (2 + 2))) + x)), (((y - 1) - 2) - 2)
  return x

def f5(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + (2 + 2)))) + 1):
    x,y = f6(x,y), (((y - 2) - 2) - 2)
  return x

def f4(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + (2 + 2)))) + 1):
    x,y = f5(x,y), (((y - 2) - 2) - 2)
  return x

def f3(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 + (2 + 2))))) + 1):
    x,y = f4(x,y), ((((y - 1) - 2) - 2) - 2)
  return x

def f2(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 * (2 + 2)))) + 1):
    x,y = f3(x,y), ((((y - 2) - 2) - 2) - 2)
  return x

def f1(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 * (2 + 2))))) + 1):
    x,y = f2(x,y), (((((y - 1) - 2) - 2) - 2) - 2)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,(1 + (X // (2 * (2 + 2)))) + 1):
    x,y = f1(x,y), ((((y - 2) - 2) - 2) - 2)
  return x

for x in range(32):
  print (f0(x))
```

### Orders of non-Abelian Z-groups.	

https://oeis.org/A69209 : 6 10 12 14 18 20 21 22 24 26 28 30 34 36 38 39 40 42 44 46 48 50 52 54 55 56 57 58 60 62 63 66 68 70 72 74 76 78 80 82 84 86 88 90 92 93 94 96 98 100 102 104 105 106 108 110 111 112 114 116 117 118

size 41, time 126085: 1 + (compr ((loop2 (1 + (if (x mod (1 + y)) <= 0 then 0 else x)) (y - 1) x 0 x) mod (loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + 2) (1 + x))) (1 + x))

B B K B L D H A K I D L B E K A K N K B L D H B L D K I C C D B K D J H B K D M D

```
def f2(X):
  x,y = 0, X
  for z in range (1,X + 1):
    x,y = (1 + (0 if (x % (1 + y)) <= 0 else x)), (y - 1)
  return x

def f3(X):
  x = 1 + X
  for y in range (1,(2 + 2) + 1):
    x = (1 + y) if (x % (1 + y)) <= 0 else x
  return x

def f1(X):
  x,i = 0,0
  while i <= 1 + X:
    if (f2(x) % f3(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f0(X):
  return 1 + f1(X)

for x in range(32):
  print (f0(x))
```

### Coordination sequence for A_4 lattice.	

https://oeis.org/A8383 : 1 20 110 340 780 1500 2570 4060 6040 8580 11750 15620 20260 25740 32130 39500 47920 57460 68190 80180 93500 108220 124410 142140 161480 182500 205270 229860 256340 284780 315250 347820 382560 419540 458830 500500 544620

size 69, time 395770: loop2 ((loop2 ((loop2 ((loop2 ((loop2 ((loop (((loop (x * x) 1 (2 + (2 + y))) * x) div (y * y)) (y - 1) (if y <= 0 then 0 else 1)) - x) (1 + y) 2 0 y) - x) (y - 1) 2 0 y) - x) (y - 1) 2 0 y) - x) (y - 1) 2 0 y) - x) (y - 1) 2 0 x

K K F B C C L D D J K F L L F G L B E L A B I J K E B L D C A L N K E L B E C A L N K E L B E C A L N K E L B E C A L N K E L B E C A K N

```
def f6(X,Y):
  x = 2 + (2 + Y)
  for y in range (1,1 + 1):
    x = x * x
  return x

def f5(X,Y):
  x = 0 if Y <= 0 else 1
  for y in range (1,(Y - 1) + 1):
    x = (f6(x,y) * x) // (y * y)
  return x

def f4(X,Y):
  x,y = 0, Y
  for z in range (1,2 + 1):
    x,y = (f5(x,y) - x), (1 + y)
  return x

def f3(X,Y):
  x,y = 0, Y
  for z in range (1,2 + 1):
    x,y = (f4(x,y) - x), (y - 1)
  return x

def f2(X,Y):
  x,y = 0, Y
  for z in range (1,2 + 1):
    x,y = (f3(x,y) - x), (y - 1)
  return x

def f1(X,Y):
  x,y = 0, Y
  for z in range (1,2 + 1):
    x,y = (f2(x,y) - x), (y - 1)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,2 + 1):
    x,y = (f1(x,y) - x), (y - 1)
  return x

for x in range(32):
  print (f0(x))
```

### Determinant of the Cayley addition table of Z_{n}.	

https://oeis.org/A70896 : 0 ~1 ~9 96 1250 ~19440 ~352947 7340032 172186884 ~4500000000 ~129687123005 4086546038784 139788510734886 ~5159146026151936 ~204350482177734375 8646911284551352320 389289535005334947848 ~18580248257778920521728

size 18, time 2588: (loop2 (x * y) (1 - (1 + y)) x x (0 - (1 + x))) div 2

K L F B B L D E K K A B K D E N C G

```
def f1(X):
  x,y = X, 0 - (1 + X)
  for z in range (1,X + 1):
    x,y = (x * y), (1 - (1 + y))
  return x

def f0(X):
  return f1(X) // 2

for x in range(32):
  print (f0(x))
```

### Number of "sets of lists": number of partitions of {1,...,n} into any number of lists, where a list means an ordered subset.

https://oeis.org/A262 : 1 1 3 13 73 501 4051 37633 394353 4596553 58941091 824073141 12470162233 202976401213 3535017524403 65573803186921 1290434218669921 26846616451246353 588633468315403843 13564373693588558173 327697927886085654441 8281153039765859726341

size 75, time 862493: loop2 ((loop ((loop2 ((1 + y) * (x * y)) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (x - (if (y - x) <= 0 then y else 0)) x x)) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)) 1 y) + x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

B L D K L F F B L D A K K A B L D I E K K J E B K L K E L A I E K K J N K L F A K K A B L D I E K K J E B J G B L J K D B L D B K D A K K F K D C G N

```
def f3(X):
  x = X
  for y in range (1,X + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f4(X):
  x = X
  for y in range (1,X + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f2(X):
  x,y = 1, f4(X)
  for z in range (1,(0 - f3(X)) + 1):
    x,y = ((1 + y) * (x * y)), (1 + y)
  return x

def f6(X):
  x = X
  for y in range (1,X + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f5(X):
  x = 1
  for y in range (1,(0 - f6(X)) + 1):
    x = x * y
  return x

def f1(X,Y):
  x = Y
  for y in range (1,1 + 1):
    x = f2(x) // f5(x)
  return x

def f0(X):
  x,y = 0, ((X * X) + X) // 2
  for z in range (1,(1 + X) + 1):
    x,y = (f1(x,y) + x), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```

### Dying rabbits: a(n) = a(n-1) + a(n-2) - a(n-6).

https://oeis.org/A23436 : 0 1 1 2 3 5 8 12 19 29 45 69 106 163 250 384 589 904 1387 2128 3265 5009 7685 11790 18088 27750 42573 65314 100202 153726 235840 361816 555083 851585 1306466 2004325 3074951

size 35, time 22943: if x <= 0 then 0 else (loop2 (1 + ((((((((((y * y) + y) div x) + y) * y) div x) + y) * y) div (x + y)) + x)) x (x - 2) 1 0)

K A B L L F L D K G L D L F K G L D L F K L D G K D D K K C E B A N I

```
def f1(X):
  x,y = 1, 0
  for z in range (1,(X - 2) + 1):
    x,y = (1 + ((((((((((y * y) + y) // x) + y) * y) // x) + y) * y) // (x + y)) + x)), x
  return x

def f0(X):
  return 0 if X <= 0 else f1(X)

for x in range(32):
  print (f0(x))
```

### Number of partitions of n into at most 12 parts.

https://oeis.org/A8641 : 1 1 2 3 5 7 11 15 22 30 42 56 77 100 133 172 224 285 366 460 582 725 905 1116 1380 1686 2063 2503 3036 3655 4401 5262 6290 7476 8877 10489 12384 14552 17084 19978 23334 27156 31570 36578 42333 48849 56297

size 219, time 2789189: loop2 (loop2 (loop2 (loop2 (loop2 (loop2 (loop2 (loop2 (loop2 ((loop (((x * x) + x) div (2 + (2 + 2))) 1 (2 + (y div 2))) + x) ((y - 1) - 2) (1 + (y div (1 + 2))) x y) ((y - 2) - 2) (1 + (y div (2 + 2))) x y) (((y - 1) - 2) - 2) (1 + (y div (1 + (2 + 2)))) x y) ((((y - 1) - 2) - 2) - 2) (1 + (y div (1 + (2 + (2 + 2))))) x y) ((((y - 2) - 2) - 2) - 2) (1 + (y div (2 * (2 + 2)))) x y) (((((y - 1) - 2) - 2) - 2) - 2) (1 + (y div (1 + (2 * (2 + 2))))) x y) (((((y - 2) - 2) - 2) - 2) - 2) (1 + (y div (2 + (2 * (2 + 2))))) x y) ((((((y - 1) - 2) - 2) - 2) - 2) - 2) (1 + (y div (1 + (2 + (2 * (2 + 2)))))) x y) ((((((y - 2) - 2) - 2) - 2) - 2) - 2) (1 + (x div (2 * (2 + (2 + 2))))) 0 x

K K F K D C C C D D G B C L C G D J K D L B E C E B L B C D G D K L N L C E C E B L C C D G D K L N L B E C E C E B L B C C D D G D K L N L B E C E C E C E B L B C C C D D D G D K L N L C E C E C E C E B L C C C D F G D K L N L B E C E C E C E C E B L B C C C D F D G D K L N L C E C E C E C E C E B L C C C C D F D G D K L N L B E C E C E C E C E C E B L B C C C C D F D D G D K L N L C E C E C E C E C E C E B K C C C C D D F G D A K N

```
def f9(X,Y):
  x = 2 + (Y // 2)
  for y in range (1,1 + 1):
    x = ((x * x) + x) // (2 + (2 + 2))
  return x

def f8(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + 2))) + 1):
    x,y = (f9(x,y) + x), ((y - 1) - 2)
  return x

def f7(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + 2))) + 1):
    x,y = f8(x,y), ((y - 2) - 2)
  return x

def f6(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 + 2)))) + 1):
    x,y = f7(x,y), (((y - 1) - 2) - 2)
  return x

def f5(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 + (2 + 2))))) + 1):
    x,y = f6(x,y), ((((y - 1) - 2) - 2) - 2)
  return x

def f4(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 * (2 + 2)))) + 1):
    x,y = f5(x,y), ((((y - 2) - 2) - 2) - 2)
  return x

def f3(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 * (2 + 2))))) + 1):
    x,y = f4(x,y), (((((y - 1) - 2) - 2) - 2) - 2)
  return x

def f2(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (2 + (2 * (2 + 2))))) + 1):
    x,y = f3(x,y), (((((y - 2) - 2) - 2) - 2) - 2)
  return x

def f1(X,Y):
  x,y = X, Y
  for z in range (1,(1 + (Y // (1 + (2 + (2 * (2 + 2)))))) + 1):
    x,y = f2(x,y), ((((((y - 1) - 2) - 2) - 2) - 2) - 2)
  return x

def f0(X):
  x,y = 0, X
  for z in range (1,(1 + (X // (2 * (2 + (2 + 2))))) + 1):
    x,y = f1(x,y), ((((((y - 2) - 2) - 2) - 2) - 2) - 2)
  return x

for x in range(32):
  print (f0(x))
```

### Generalized Catalan numbers.	

https://oeis.org/A68764 : 1 1 4 18 88 456 2464 13736 78432 456416 2697088 16141120 97632000 595912960 3665728512 22703097472 141448381952 885934151168 5575020435456 35230798994432 223485795258368 1422572226146304 9083682419818496 58169612565614592 373486362257899520 2403850703479816192

size 132, time 595851: loop2 ((loop ((loop (2 * ((2 * ((2 * (x * y)) - x)) div (1 + y))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) (loop2 (x * y) (y - 1) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1)) 1 y) - x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

C C C K L F F K E F B L D G F K L K E L A I E C K B C C D D G D K J K L F L B E A K K A B L D I E C K B C C D D G D K J E B B K L K E L A I E C K B C C D D G D K J D N J K L F A K K A B L D I E C K B C C D D G D K J E B J G B L J K E B L D B K D A K K F K D C G N

```
def f3(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f5(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f6(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f4(X):
  x,y = 1, 1 + f6(X)
  for z in range (1,(0 - f5(X)) + 1):
    x,y = (x * y), (y - 1)
  return x

def f2(X):
  x = f4(X)
  for y in range (1,f3(X) + 1):
    x = 2 * ((2 * ((2 * (x * y)) - x)) // (1 + y))
  return x

def f8(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f7(X):
  x = 1
  for y in range (1,(0 - f8(X)) + 1):
    x = x * y
  return x

def f1(X,Y):
  x = Y
  for y in range (1,1 + 1):
    x = f2(x) // f7(x)
  return x

def f0(X):
  x,y = 0, ((X * X) + X) // 2
  for z in range (1,(1 + X) + 1):
    x,y = (f1(x,y) - x), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```

### Subtrees in rooted plane trees on n nodes.

https://oeis.org/A7856 : 1 3 12 52 236 1109 5366 26639 135300 701269 3700400 19834973 107784622 592705377 3292970302 18458954896 104276682820 593056996445 3392898090908 19512100041995 112729617387020 653965783541960 3807766434556940

size 144, time 807351: loop2 ((loop ((loop ((2 * ((2 * (x * y)) - x)) div (1 + y)) (loop (x - (if (y - x) <= 0 then y else 0)) x x) (loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1 (((loop2 ((if y <= 0 then 0 else 1) + x) (y - x) (2 + (x div (1 + (2 + 2)))) 2 x) - 1) + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1)) 1 y) + x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

C C K L F F K E F B L D G K L K E L A I E K K J K L F B L D A K K A B L D I E C K B C C D D G D K J E B L A B I K D L K E C K B C C D D G D C K N B E K L K E L A I E C K B C C D D G D K J D N J K L F A K K A B L D I E C K B C C D D G D K J E B J G B L J K D B L D B K D A K K F K D C G N

```
def f3(X):
  x = X
  for y in range (1,X + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f5(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f6(X):
  x,y = 2, X
  for z in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x,y = ((0 if y <= 0 else 1) + x), (y - x)
  return x

def f7(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f4(X):
  x,y = 1, (f6(X) - 1) + f7(X)
  for z in range (1,(0 - f5(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f2(X):
  x = f4(X)
  for y in range (1,f3(X) + 1):
    x = (2 * ((2 * (x * y)) - x)) // (1 + y)
  return x

def f9(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f8(X):
  x = 1
  for y in range (1,(0 - f9(X)) + 1):
    x = x * y
  return x

def f1(X,Y):
  x = Y
  for y in range (1,1 + 1):
    x = f2(x) // f8(x)
  return x

def f0(X):
  x,y = 0, ((X * X) + X) // 2
  for z in range (1,(1 + X) + 1):
    x,y = (f1(x,y) + x), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```

### Sums of ménage numbers.

https://oeis.org/A271 : 1 0 0 1 3 16 96 675 5413 48800 488592 5379333 64595975 840192288 11767626752 176574062535 2825965531593 48052401132800 865108807357216 16439727718351881 328839946389605643 6906458590966507696

size 122, time 280548: loop2 ((loop ((loop (x * y) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) (loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1 (1 + (2 * (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x))))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1)) 1 y) - x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

K L F K L K E L A I E C K B C C D D G D K J K L F B L D A K K A B L D I E C K B C C D D G D K J E B B C K L K E L A I E C K B C C D D G D K J F D N J K L F A K K A B L D I E C K B C C D D G D K J E B J G B L J K E B L D B K D A K K F K D C G N

```
def f3(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f5(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f6(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f4(X):
  x,y = 1, 1 + (2 * f6(X))
  for z in range (1,(0 - f5(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f2(X):
  x = f4(X)
  for y in range (1,f3(X) + 1):
    x = x * y
  return x

def f8(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f7(X):
  x = 1
  for y in range (1,(0 - f8(X)) + 1):
    x = x * y
  return x

def f1(X,Y):
  x = Y
  for y in range (1,1 + 1):
    x = f2(x) // f7(x)
  return x

def f0(X):
  x,y = 0, ((X * X) + X) // 2
  for z in range (1,(1 + X) + 1):
    x,y = (f1(x,y) - x), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```

### Number of ways to place n non-attacking bishops on a 2 X 2n board.	

https://oeis.org/A199033 : 1 4 22 128 771 4744 29618 186880 1188679 7608764 48953224 316283264 2050706932 13336273528 86953633242 568221290496 3720529001823 24403423540348 160314652983158 1054635453261568 6946703172803003 45809043607167328 302395650703501688

size 175, time 478543: loop2 ((loop ((((loop2 (x * y) (1 + y) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) 1 (2 - (2 * (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)))) div (loop (x * y) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) 1)) * (loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1 (2 + (2 * (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x))))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1)) 1 y) + x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

K L F B L D K L K E L A I E C K B C C D D G D K J B C C K K A B L D I E C K B C C D D G D K J F E N K L F K L K E L A I E C K B C C D D G D K J B J G K L F B L D A K K A B L D I E C K B C C D D G D K J E B C C K L K E L A I E C K B C C D D G D K J F D N F K L F A K K A B L D I E C K B C C D D G D K J E B J G B L J K D B L D B K D A K K F K D C G N

```
def f3(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f4(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f2(X):
  x,y = 1, 2 - (2 * f4(X))
  for z in range (1,f3(X) + 1):
    x,y = (x * y), (1 + y)
  return x

def f6(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f5(X):
  x = 1
  for y in range (1,f6(X) + 1):
    x = x * y
  return x

def f8(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f9(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f7(X):
  x,y = 1, 2 + (2 * f9(X))
  for z in range (1,(0 - f8(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f11(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f10(X):
  x = 1
  for y in range (1,(0 - f11(X)) + 1):
    x = x * y
  return x

def f1(X,Y):
  x = Y
  for y in range (1,1 + 1):
    x = ((f2(x) // f5(x)) * f7(x)) // f10(x)
  return x

def f0(X):
  x,y = 0, ((X * X) + X) // 2
  for z in range (1,(1 + X) + 1):
    x,y = (f1(x,y) + x), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```

### Motzkin numbers: number of ways of drawing any number of nonintersecting chords joining n (labeled) points on a circle.

https://oeis.org/A1006 : 1 1 2 4 9 21 51 127 323 835 2188 5798 15511 41835 113634 310572 853467 2356779 6536382 18199284 50852019 142547559 400763223 1129760415 3192727797 9043402501 25669818476 73007772802 208023278209 593742784829

size 130, time 1298534: loop2 ((loop ((loop ((((1 + 2) * (x * y)) div (2 + y)) + x) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) (loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1)) 1 y) - x) (1 + y) x 1 (1 + (((x * x) + x) div 2))

B C D K L F F C L D G K D K L K E L A I E C K B C C D D G D K J K L F B L D A K K A B L D I E C K B C C D D G D K J E B B K L K E L A I E C K B C C D D G D K J D N J K L F A K K A B L D I E C K B C C D D G D K J E B J G B L J K E B L D K B B K K F K D C G D N

```
def f3(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f5(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f6(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f4(X):
  x,y = 1, 1 + f6(X)
  for z in range (1,(0 - f5(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f2(X):
  x = f4(X)
  for y in range (1,f3(X) + 1):
    x = (((1 + 2) * (x * y)) // (2 + y)) + x
  return x

def f8(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f7(X):
  x = 1
  for y in range (1,(0 - f8(X)) + 1):
    x = x * y
  return x

def f1(X,Y):
  x = Y
  for y in range (1,1 + 1):
    x = f2(x) // f7(x)
  return x

def f0(X):
  x,y = 1, 1 + (((X * X) + X) // 2)
  for z in range (1,X + 1):
    x,y = (f1(x,y) - x), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```

### Number of pairs of functions (f,g) from a set of n elements into itself satisfying f(x) = f(g(f(x))).	

https://oeis.org/A239768 : 1 1 10 195 6808 362745 26848656 2621263519 324981308800 49669569764433 9146879704748800 1993011341241988551 506190915590699695104 148000190814308473203433 49289886405448749446514688 18529196186934893511062427375 7800708229072237749055062900736 3652486190893312491910941333813537

size 200, time 406817: loop2 ((loop ((((loop2 ((loop2 (x * y) y x 1 (y - 1)) * ((loop2 (x * y) (1 + y) x 1 y) div (loop (x * y) x 1))) 0 1 (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (x div (1 + (2 + 2))))) (1 + x)))) * (loop2 (x * y) y (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) 1 ((loop2 ((if y <= 0 then 0 else 1) + x) (y - x) (2 + (x div (1 + (2 + 2)))) 2 x) - 2))) * (loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1 (loop (loop y (x - y) x) x (1 + x)))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else x)) 1 x)) 1)) 1 y) + x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

K L F L K B L B E N K L F B L D K B L N K L F K B J G F A B K L K E L A I E C K B C C D D G D K J B K K A L I E B C K B C C D D G D D B K D J E N K L F L K L K E L A I E C K B C C D D G D K J B L A B I K D L K E C K B C C D D G D C K N C E N F K L F B L D A K K A B L D I E C K B C C D D G D K J E B L K L E K J K B K D J N F K L F A K K A K I E B K J E B J G B L J K D B L D B K D A K K F K D C G N

```
def f3(X,Y):
  x,y = 1, Y - 1
  for z in range (1,X + 1):
    x,y = (x * y), y
  return x

def f4(X,Y):
  x,y = 1, Y
  for z in range (1,X + 1):
    x,y = (x * y), (1 + y)
  return x

def f5(X):
  x = 1
  for y in range (1,X + 1):
    x = x * y
  return x

def f6(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f7(X):
  x = 1 + X
  for y in range (1,(1 + (2 + (X // (1 + (2 + 2))))) + 1):
    x = x - (0 if x <= 0 else y)
  return x

def f2(X):
  x,y = f6(X), 1 - f7(X)
  for z in range (1,1 + 1):
    x,y = (f3(x,y) * (f4(x,y) // f5(x))), 0
  return x

def f9(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f10(X):
  x,y = 2, X
  for z in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x,y = ((0 if y <= 0 else 1) + x), (y - x)
  return x

def f8(X):
  x,y = 1, f10(X) - 2
  for z in range (1,f9(X) + 1):
    x,y = (x * y), y
  return x

def f12(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f14(X,Y):
  x = X
  for y in range (1,(X - Y) + 1):
    x = y
  return x

def f13(X):
  x = 1 + X
  for y in range (1,X + 1):
    x = f14(x,y)
  return x

def f11(X):
  x,y = 1, f13(X)
  for z in range (1,(0 - f12(X)) + 1):
    x,y = (x * y), (1 + y)
  return x

def f16(X):
  x = X
  for y in range (1,1 + 1):
    x = x - (0 if x <= 0 else x)
  return x

def f15(X):
  x = 1
  for y in range (1,(0 - f16(X)) + 1):
    x = x * y
  return x

def f1(X,Y):
  x = Y
  for y in range (1,1 + 1):
    x = ((f2(x) * f8(x)) * f11(x)) // f15(x)
  return x

def f0(X):
  x,y = 0, ((X * X) + X) // 2
  for z in range (1,(1 + X) + 1):
    x,y = (f1(x,y) + x), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```

### Domb numbers: number of 2n-step polygons on diamond lattice.

https://oeis.org/A2895 : 1 4 28 256 2716 31504 387136 4951552 65218204 878536624 12046924528 167595457792 2359613230144 33557651538688 481365424895488 6956365106016256 101181938814289564 1480129751586116848 21761706991570726096 321401321741959062016

size 145, time 136520: loop2 ((loop (loop2 ((loop (2 * ((x - (x div y)) + x)) x 1) * ((((((loop2 (x * y) (1 + y) x 1 (1 + y)) div (loop (x * y) x 1)) * (loop2 (x * y) (1 + y) y 1 (1 + y))) div (loop (x * y) y 1)) * (loop2 (x * y) (1 + y) x 1 (1 + y))) div (loop (x * y) x 1))) 0 1 (0 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

C K K L G E K D F K B J K L F B L D K B B L D N K L F K B J G K L F B L D L B B L D N F K L F L B J G K L F B L D K B B L D N F K L F K B J G F A B A K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D B K D A K K F K D C G N

```
def f3(X):
  x = 1
  for y in range (1,X + 1):
    x = 2 * ((x - (x // y)) + x)
  return x

def f4(X,Y):
  x,y = 1, 1 + Y
  for z in range (1,X + 1):
    x,y = (x * y), (1 + y)
  return x

def f5(X):
  x = 1
  for y in range (1,X + 1):
    x = x * y
  return x

def f6(X,Y):
  x,y = 1, 1 + Y
  for z in range (1,Y + 1):
    x,y = (x * y), (1 + y)
  return x

def f7(X,Y):
  x = 1
  for y in range (1,Y + 1):
    x = x * y
  return x

def f8(X,Y):
  x,y = 1, 1 + Y
  for z in range (1,X + 1):
    x,y = (x * y), (1 + y)
  return x

def f9(X):
  x = 1
  for y in range (1,X + 1):
    x = x * y
  return x

def f10(X):
  x = 1 + X
  for y in range (1,(1 + (2 + (2 + (X // (1 + (2 * (2 + 2))))))) + 1):
    x = x - (0 if x <= 0 else y)
  return x

def f11(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f2(X):
  x,y = 0 - f10(X), f11(X)
  for z in range (1,1 + 1):
    x,y = (f3(x) * (((((f4(x,y) // f5(x)) * f6(x,y)) // f7(x,y)) * f8(x,y)) // f9(x))), 0
  return x

def f1(X,Y):
  x = Y
  for y in range (1,1 + 1):
    x = f2(x)
  return x

def f0(X):
  x,y = 0, ((X * X) + X) // 2
  for z in range (1,(1 + X) + 1):
    x,y = (f1(x,y) + x), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```

### Convolution of primes with themselves.	

https://oeis.org/A14342 : 4 12 29 58 111 188 305 462 679 968 1337 1806 2391 3104 3953 4978 6175 7568 9185 11030 13143 15516 18177 21150 24471 28152 32197 36678 41543 46828 52621 58874 65659 73000 80949 89462 98631 108396 118869 130102 142071

size 127, time 3130033: loop2 ((loop (loop2 ((1 + (compr (x - (loop2 (loop (if (x mod (2 + y)) <= 0 then 0 else x) (y div (2 * (2 + 2))) (1 + y)) 0 (1 - (x mod 2)) 1 x)) (1 + x))) * (compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) y)) 0 1 (0 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

B K K C L D H A K I L C C C D F G B L D J A B K C H E B K N E B K D M D C K B L D H A K I K C E K J E L M F A B A K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D B K D A K K F K D C G N

size 125, time 3536319: loop2 ((loop (loop2 ((1 + (compr (x - (loop2 (loop (if (x mod (2 + y)) <= 0 then 2 else x) (2 + (y div (2 * (2 + (2 + (2 + 2)))))) (1 + y)) 0 (1 - (x mod 2)) 1 x)) (1 + x))) * (compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) y)) 0 1 (0 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (x div (1 + (2 + 2))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) 1 y) + x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

B K K C L D H C K I C L C C C C C D D D F G D B L D J A B K C H E B K N E B K D M D C K B L D H A K I K C E K J E L M F A B A K K A L I E B C K B C C D D G D D B K D J E K L K E L A I E C K B C C D D G D K J N B L J K D B L D B K D A K K F K D C G N

```
def f5(X,Y):
  x = 1 + Y
  for y in range (1,(Y // (2 * (2 + 2))) + 1):
    x = 0 if (x % (2 + y)) <= 0 else x
  return x

def f4(X):
  x,y = 1, X
  for z in range (1,(1 - (X % 2)) + 1):
    x,y = f5(x,y), 0
  return x

def f3(X):
  x,i = 0,0
  while i <= 1 + X:
    if (x - f4(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f7(X):
  x = X
  for y in range (1,(X - 2) + 1):
    x = 0 if (x % (1 + y)) <= 0 else x
  return x

def f6(X,Y):
  x,i = 0,0
  while i <= Y:
    if (2 - f7(x)) <= 0:
      i = i + 1
    x = x + 1
  return x - 1

def f8(X):
  x = 1 + X
  for y in range (1,(1 + (2 + (2 + (X // (1 + (2 * (2 + 2))))))) + 1):
    x = x - (0 if x <= 0 else y)
  return x

def f9(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f2(X):
  x,y = 0 - f8(X), f9(X)
  for z in range (1,1 + 1):
    x,y = ((1 + f3(x)) * f6(x,y)), 0
  return x

def f1(X,Y):
  x = Y
  for y in range (1,1 + 1):
    x = f2(x)
  return x

def f0(X):
  x,y = 0, ((X * X) + X) // 2
  for z in range (1,(1 + X) + 1):
    x,y = (f1(x,y) + x), (1 + y)
  return x

for x in range(32):
  print (f0(x))
```
