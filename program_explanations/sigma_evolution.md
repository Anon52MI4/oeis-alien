exp114-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp114-chk/stats_sol-size 79, time 5102279: loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

exp114-chk/stats_sol-L K H K A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D B K D A K K F K D C G N

--

exp115-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp115-chk/stats_sol-size 80, time 5020946: loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + y) else 0) 0 1 (0 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) x 1 (loop (x + y) x 1)

exp115-chk/stats_sol-K B L D H B L D A I A B A K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B K L D K B J N

exp115-chk/stats_sol-size 75, time 5558411: loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (2 + ((x div (1 + (2 + (2 + 2)))) + 2)) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) x 1 (((x * x) + x) div 2)

exp115-chk/stats_sol-L K H K A I A B B K K A L I E C K B C C C D D D G C D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B K K F K D C G N

--

exp117-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp117-chk/stats_sol-size 83, time 5014401: loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + y) else 0) 0 1 (0 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) x 1 (1 + (((x * x) + x) div 2))

exp117-chk/stats_sol-K B L D H B L D A I A B A K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B B K K F K D C G D N

exp117-chk/stats_sol-size 75, time 5558411: loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (2 + ((x div (1 + (2 + (2 + 2)))) + 2)) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) x 1 (((x * x) + x) div 2)

exp117-chk/stats_sol-L K H K A I A B B K K A L I E C K B C C C D D D G C D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B K K F K D C G N

--

exp118-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp118-chk/stats_sol-size 77, time 5000933: loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) x 1 (((x * x) + x) div 2)

exp118-chk/stats_sol-L K H K A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B K K F K D C G N

exp118-chk/stats_sol-size 75, time 5558411: loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (2 + ((x div (1 + (2 + (2 + 2)))) + 2)) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) x 1 (((x * x) + x) div 2)

exp118-chk/stats_sol-L K H K A I A B B K K A L I E C K B C C C D D D G C D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B K K F K D C G N

--

exp119-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp119-chk/stats_sol-size 81, time 4836629: loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (2 + y) else 1) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) x 1 (((x * x) - x) div 2)

exp119-chk/stats_sol-K B L D H C L D B I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B K K F K E C G N

exp119-chk/stats_sol-size 75, time 5558411: loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (2 + ((x div (1 + (2 + (2 + 2)))) + 2)) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) x 1 (((x * x) + x) div 2)

exp119-chk/stats_sol-L K H K A I A B B K K A L I E C K B C C C D D D G C D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B K K F K D C G N

--

exp120-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp120-chk/stats_sol-size 89, time 2510347: (1 + x) + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + y) else 0) 0 1 (0 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) (x - (x div 2)) 0 (((x * x) + x) div 2))

exp120-chk/stats_sol-B K D K B L D H B L D A I A B A K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K K C G E A K K F K D C G N D

exp120-chk/stats_sol-size 75, time 5558411: loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (2 + ((x div (1 + (2 + (2 + 2)))) + 2)) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) x 1 (((x * x) + x) div 2)

exp120-chk/stats_sol-L K H K A I A B B K K A L I E C K B C C C D D D G C D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B K K F K D C G N

--

exp121-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp121-chk/stats_sol-size 89, time 2422399: (1 + x) + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + y) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) (x - (x div 2)) 0 (((x * x) - x) div 2))

exp121-chk/stats_sol-B K D K B L D H B L D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K K C G E A K K F K E C G N D

exp121-chk/stats_sol-size 75, time 5558411: loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (2 + ((x div (1 + (2 + (2 + 2)))) + 2)) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) x 1 (((x * x) + x) div 2)

exp121-chk/stats_sol-L K H K A I A B B K K A L I E C K B C C C D D D G C D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B K K F K D C G N

--

exp122-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp122-chk/stats_sol-size 87, time 2422259: loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + y) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) (x - (x div 2)) (1 + x) (((x * x) - x) div 2)

exp122-chk/stats_sol-K B L D H B L D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K K C G E B K D K K F K E C G N

exp122-chk/stats_sol-size 75, time 5248475: loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (2 * (2 + 2)))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) x 1 (((x * x) + x) div 2)

exp122-chk/stats_sol-L K H K A I A B B K K A L I E B C C K C C C D F G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B K K F K D C G N

--

exp126-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp126-chk/stats_sol-size 90, time 2375380: (if x <= 0 then 1 else 2) + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + y) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) (x div 2) x (1 + (((x * x) - x) div 2)))

exp126-chk/stats_sol-K B C I K B L D H B L D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K C G K B K K F K E C G D N D

exp126-chk/stats_sol-size 75, time 5248475: loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (2 * (2 + 2)))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) x 1 (((x * x) + x) div 2)

exp126-chk/stats_sol-L K H K A I A B B K K A L I E B C C K C C C D F G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B K K F K D C G N

--

exp127-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp127-chk/stats_sol-size 90, time 2375380: (if x <= 0 then 1 else 2) + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + y) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) (x div 2) x (1 + (((x * x) - x) div 2)))

exp127-chk/stats_sol-K B C I K B L D H B L D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K C G K B K K F K E C G D N D

exp127-chk/stats_sol-size 72, time 5668652: loop2 ((loop (loop2 (if (y mod x) <= 0 then (1 + (y div x)) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (2 + 2))) x)) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) 1 y) + x) (y - 1) (x - (x div 2)) 1 (loop (x + y) x x)

exp127-chk/stats_sol-L K H B L K G D A I A B B K K A B L D I E C K C C D G D K J E K L K E L A I E C K B C C D D G D K J N B L J K D L B E K K C G E B K L D K K J N

--

exp128-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp128-chk/stats_sol-size 72, time 5659132: (1 + x) + (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (2 + 2))) x)) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) 1 y) + x) (y - 1) (x - (x div 2)) 0 (loop (x + y) x x))

exp128-chk/stats_sol-B K D L K H K A I A B B K K A B L D I E C K C C D G D K J E K L K E L A I E C K B C C D D G D K J N B L J K D L B E K K C G E A K L D K K J N D

exp128-chk/stats_sol-size 90, time 2375380: (if x <= 0 then 1 else 2) + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + y) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) (x div 2) x (1 + (((x * x) - x) div 2)))

exp128-chk/stats_sol-K B C I K B L D H B L D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K C G K B K K F K E C G D N D

--

exp129-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp129-chk/stats_sol-size 90, time 2375380: (if x <= 0 then 1 else 2) + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + y) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) (x div 2) x (1 + (((x * x) - x) div 2)))

exp129-chk/stats_sol-K B C I K B L D H B L D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K C G K B K K F K E C G D N D

exp129-chk/stats_sol-size 70, time 5658992: x + (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (2 + 2))) x)) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) 1 y) + x) (y - 1) (x - (x div 2)) 1 (loop (x + y) x x))

exp129-chk/stats_sol-K L K H K A I A B B K K A B L D I E C K C C D G D K J E K L K E L A I E C K B C C D D G D K J N B L J K D L B E K K C G E B K L D K K J N D

--

exp131-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp131-chk/stats_sol-size 70, time 5658992: 1 + (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (2 + 2))) x)) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) 1 y) + x) (y - 1) (x - (x div 2)) x (loop (x + y) x x))

exp131-chk/stats_sol-B L K H K A I A B B K K A B L D I E C K C C D G D K J E K L K E L A I E C K B C C D D G D K J N B L J K D L B E K K C G E K K L D K K J N D

exp131-chk/stats_sol-size 90, time 2375380: (if x <= 0 then 1 else 2) + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + y) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) (x div 2) x (1 + (((x * x) - x) div 2)))

exp131-chk/stats_sol-K B C I K B L D H B L D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K C G K B K K F K E C G D N D

--

exp133-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp133-chk/stats_sol-size 70, time 5658992: 1 + (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (2 + 2))) x)) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) 1 y) + x) (y - 1) (x - (x div 2)) x (loop (x + y) x x))

exp133-chk/stats_sol-B L K H K A I A B B K K A B L D I E C K C C D G D K J E K L K E L A I E C K B C C D D G D K J N B L J K D L B E K K C G E K K L D K K J N D

exp133-chk/stats_sol-size 92, time 2328674: (if x <= 0 then 1 else (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + y) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) ((x - 1) div 2) 2 (1 + (((x * x) - x) div 2)))) + x

exp133-chk/stats_sol-K B K B L D H B L D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D K B E C G C B K K F K E C G D N I K D

--

exp136-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp136-chk/stats_sol-size 70, time 5658992: 1 + (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (2 + 2))) x)) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) 1 y) + x) (y - 1) (x - (x div 2)) x (loop (x + y) x x))

exp136-chk/stats_sol-B L K H K A I A B B K K A B L D I E C K C C D G D K J E K L K E L A I E C K B C C D D G D K J N B L J K D L B E K K C G E K K L D K K J N D

exp136-chk/stats_sol-size 88, time 2324050: if x <= 0 then 1 else (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) (0 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) x))) 1 y) + x) (1 + y) ((x - 1) div 2) (2 + x) (1 + (((x * x) - x) div 2)))

exp136-chk/stats_sol-K B L K H K A I A B B K L K E L A I E C C K B C C C D F D G D D K J D A K K A L I E B C C K B C C C D F D G D D D K J E N B L J K D B L D K B E C G C K D B K K F K E C G D N I

--

exp137-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp137-chk/stats_sol-size 70, time 5658992: 1 + (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (2 + 2))) x)) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) 1 y) + x) (y - 1) (x - (x div 2)) x (loop (x + y) x x))

exp137-chk/stats_sol-B L K H K A I A B B K K A B L D I E C K C C D G D K J E K L K E L A I E C K B C C D D G D K J N B L J K D L B E K K C G E K K L D K K J N D

exp137-chk/stats_sol-size 88, time 2324050: (if x <= 0 then 1 else (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) (0 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) x))) 1 y) + x) (1 + y) ((x - 1) div 2) 2 (1 + (((x * x) - x) div 2)))) + x

exp137-chk/stats_sol-K B L K H K A I A B B K L K E L A I E C C K B C C C D F D G D D K J D A K K A L I E B C C K B C C C D F D G D D D K J E N B L J K D B L D K B E C G C B K K F K E C G D N I K D

--

exp139-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp139-chk/stats_sol-size 70, time 5658992: 1 + (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (2 + 2))) x)) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) 1 y) + x) (y - 1) (x - (x div 2)) x (loop (x + y) x x))

exp139-chk/stats_sol-B L K H K A I A B B K K A B L D I E C K C C D G D K J E K L K E L A I E C K B C C D D G D K J N B L J K D L B E K K C G E K K L D K K J N D

exp139-chk/stats_sol-size 99, time 1602349: (1 + (x mod 2)) + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + (x div (1 + y))) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) ((1 + x) div (1 + 2)) (x mod 2) (((x * x) - x) div 2))

exp139-chk/stats_sol-B K C H D K B L D H B K B L D G D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D B K D B C D G K C H K K F K E C G N D

--

exp140-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp140-chk/stats_sol-size 70, time 5649192: 1 + (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (1 + (x div (2 + 2))) x)) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) 1 y) + x) (y - 1) (x - (x div 2)) x (loop (x + y) x x))

exp140-chk/stats_sol-B L K H K A I A B B K K A B L D I E B K C C D G D K J E K L K E L A I E C K B C C D D G D K J N B L J K D L B E K K C G E K K L D K K J N D

exp140-chk/stats_sol-size 99, time 1602349: (1 + (x mod 2)) + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + (x div (1 + y))) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) ((1 + x) div (1 + 2)) (x mod 2) (((x * x) - x) div 2))

exp140-chk/stats_sol-B K C H D K B L D H B K B L D G D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D B K D B C D G K C H K K F K E C G N D

--

exp141-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp141-chk/stats_sol-size 97, time 1601929: 1 + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + (x div (1 + y))) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) ((1 + x) div (1 + 2)) (2 * (x mod 2)) (((x * x) - x) div 2))

exp141-chk/stats_sol-B K B L D H B K B L D G D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D B K D B C D G C K C H F K K F K E C G N D

exp141-chk/stats_sol-size 70, time 5649192: 1 + (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (1 + (x div (2 + 2))) x)) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) 1 y) + x) (y - 1) (x - (x div 2)) x (loop (x + y) x x))

exp141-chk/stats_sol-B L K H K A I A B B K K A B L D I E B K C C D G D K J E K L K E L A I E C K B C C D D G D K J N B L J K D L B E K K C G E K K L D K K J N D

--

exp149-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp149-chk/stats_sol-size 97, time 1601929: 1 + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + (x div (1 + y))) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) ((1 + x) div (1 + 2)) (2 * (x mod 2)) (((x * x) - x) div 2))

exp149-chk/stats_sol-B K B L D H B K B L D G D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D B K D B C D G C K C H F K K F K E C G N D

exp149-chk/stats_sol-size 69, time 6791055: loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) (0 - (loop (x - (if x <= 0 then 0 else y)) (1 + (x div 2)) x))) 1 y) + x) (1 + y) (x - (x div 2)) (1 + x) (((x * x) - x) div 2)

exp149-chk/stats_sol-L K H K A I A B B K L K E L A I E C K B C C D D G D K J D A K K A L I E B K C G D K J E N B L J K D B L D K K C G E B K D K K F K E C G N

--

exp151-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp151-chk/stats_sol-size 97, time 1601929: 1 + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + (x div (1 + y))) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) ((1 + x) div (1 + 2)) (2 * (x mod 2)) (((x * x) - x) div 2))

exp151-chk/stats_sol-B K B L D H B K B L D G D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D B K D B C D G C K C H F K K F K E C G N D

exp151-chk/stats_sol-size 69, time 6791055: 1 + (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) (0 - (loop (x - (if x <= 0 then 0 else y)) (1 + (x div 2)) x))) 1 y) + x) (1 + y) (x - (x div 2)) x (((x * x) - x) div 2))

exp151-chk/stats_sol-B L K H K A I A B B K L K E L A I E C K B C C D D G D K J D A K K A L I E B K C G D K J E N B L J K D B L D K K C G E K K K F K E C G N D

--

exp154-chk/stats_sol:https://oeis.org/A203 : 1 3 4 7 6 12 8 15 13 18 12 28 14 24 24 31 18 39 20 42 32 36 24 60 31 42 40 56 30 72 32 63 48 54 48 91 38 60 56 90 42 96 44 84 78 72 48 124 57 93 72 98 54 120 72 120 80 90 60 168 62 96 104 127 84 144 68 126 96 144

exp154-chk/stats_sol-size 97, time 1601929: 1 + (loop2 ((loop (loop2 (if (x mod (1 + y)) <= 0 then (1 + (x div (1 + y))) else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) ((1 + x) div (1 + 2)) (2 * (x mod 2)) (((x * x) - x) div 2))

exp154-chk/stats_sol-B K B L D H B K B L D G D A I A B B K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D B K D B C D G C K C H F K K F K E C G N D

exp154-chk/stats_sol-size 68, time 6264446: 1 + (loop2 ((loop (loop2 (if (y mod x) <= 0 then x else 0) 0 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (1 + (x div (2 + 2))) x)) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (2 + 2))) x)) 1 y) + x) (y - 1) (x - (x div 2)) x (loop (x + y) x x))

exp154-chk/stats_sol-B L K H K A I A B B K K A B L D I E B K C C D G D K J E K L K E L A I E C K C C D G D K J N B L J K D L B E K K C G E K K L D K K J N D

