We got https://en.wikipedia.org/wiki/Motzkin_number .

Motzkin numbers: number of ways of drawing any number of nonintersecting chords joining n (labeled) points on a circle.
  
https://oeis.org/A1006 : 1 1 2 4 9 21 51 127 323 835 2188 5798 15511 41835 113634 310572 853467 2356779 6536382 18199284 50852019 142547559 400763223 1129760415 3192727797 9043402501 25669818476 73007772802 208023278209 593742784829

size 130, time 1298534: loop2 ((loop ((loop ((((1 + 2) * (x * y)) div (2 + y)) + x) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) (loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1)) 1 y) - x) (1 + y) x 1 (1 + (((x * x) + x) div 2))

B C D K L F F C L D G K D K L K E L A I E C K B C C D D G D K J K L F B L D A K K A B L D I E C K B C C D D G D K J E B B K L K E L A I E C K B C C D D G D K J D N J K L F A K K A B L D I E C K B C C D D G D K J E B J G B L J K E B L D K B B K K F K D C G D N

This looks nice. I examined the helper functions, and all of them can be expressed in a reasonable way. It also invented an encoding of pairs into naturals, so that it can calculate binary functions on a unary input. I am not yet sure why the output formula gives the Motzkin numbers but it should be just some "combinatorial non-counting" :-). I am attaching a code where I wrote alternatives to the functions f0, ..., f8. Enjoy!

The final formula
```
motzkin(n) = sum(
    binom(n,k) * catalan(k+1) * (-1)^(n-k)
    for k in 0..n
)
```
can be derived from the [formula for obtaining Catalan number from Motzkin](https://en.wikipedia.org/wiki/Motzkin_number#Properties):
```
catalan(n+1) = sum(
    binom(n,k) * motzkin(k)
    for k in 0..n
)
```
and the [inverse binomial transform](https://en.wikipedia.org/wiki/Binomial_transform#Definition)
```
a(n) = sum(binom(n,k) * t(k))
<=>
t(n) = sum((-1)^(n-k) * binom(n,k) * a(k))
```

The full Python program is in https://github.com/Anon52MI4/oeis-alien/blob/master/programs/motzkin.py .
