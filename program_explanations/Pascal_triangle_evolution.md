# Evolution of the programs for Pascal's trianlge. The first one found only in iter 68 - after 50k reached.

exp68-chk/stats_sol:https://oeis.org/A7318 : 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 1 10 45 120 210 252 210 120 45 10 1 1 11 55 165 330 462 462 330 165 55 11 1

exp68-chk/stats_sol-size 51, time 85098: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop y (x - y) x) x (1 + x))) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)

exp68-chk/stats_sol-K L F B L D A K K A B L D I E K K J E B L K L E K J K B K D J N K L F A K K A B L D I E K K J E B J G

--

exp69-chk/stats_sol:https://oeis.org/A7318 : 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 1 10 45 120 210 252 210 120 45 10 1 1 11 55 165 330 462 462 330 165 55 11 1

exp69-chk/stats_sol-size 77, time 25094: (loop2 ((x \* y) + x) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1 (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1)

exp69-chk/stats_sol-K L F K D B L D A K K A B L D I E C K B C C D D G D K J E B K L K E L A I E C K B C C D D G D K J N K L F A K K A B L D I E C K B C C D D G D K J E B J G

exp69-chk/stats_sol-size 51, time 85098: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop y (x - y) x) x (1 + x))) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)

exp69-chk/stats_sol-K L F B L D A K K A B L D I E K K J E B L K L E K J K B K D J N K L F A K K A B L D I E K K J E B J G

--

exp70-chk/stats_sol:https://oeis.org/A7318 : 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 1 10 45 120 210 252 210 120 45 10 1 1 11 55 165 330 462 462 330 165 55 11 1

exp70-chk/stats_sol-size 89, time 23294: (loop2 ((x \* y) + x) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1 (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1)

exp70-chk/stats_sol-K L F K D B L D A K K A B L D I E C C K B C C C D F D G D D K J E B K L K E L A I E C C K B C C C D F D G D D K J N K L F A K K A B L D I E C C K B C C C D F D G D D K J E B J G

exp70-chk/stats_sol-size 51, time 85098: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop y (x - y) x) x (1 + x))) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)

exp70-chk/stats_sol-K L F B L D A K K A B L D I E K K J E B L K L E K J K B K D J N K L F A K K A B L D I E K K J E B J G

--

exp71-chk/stats_sol:https://oeis.org/A7318 : 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 1 10 45 120 210 252 210 120 45 10 1 1 11 55 165 330 462 462 330 165 55 11 1

exp71-chk/stats_sol-size 89, time 22878: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1 (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) (1 + x))) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1)

exp71-chk/stats_sol-K L F B L D A K K A B L D I E C C K B C C C D F D G D D K J E B K L K E L A I E C C K B C C C D F D G D D B K D J N K L F A K K A B L D I E C C K B C C C D F D G D D K J E B J G

exp71-chk/stats_sol-size 51, time 85098: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop y (x - y) x) x (1 + x))) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)

exp71-chk/stats_sol-K L F B L D A K K A B L D I E K K J E B L K L E K J K B K D J N K L F A K K A B L D I E K K J E B J G

--

exp72-chk/stats_sol:https://oeis.org/A7318 : 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 1 10 45 120 210 252 210 120 45 10 1 1 11 55 165 330 462 462 330 165 55 11 1

exp72-chk/stats_sol-size 89, time 22878: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x))) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1)

exp72-chk/stats_sol-K L F B L D A K K A B L D I E C C K B C C C D F D G D D K J E B B K L K E L A I E C C K B C C C D F D G D D K J D N K L F A K K A B L D I E C C K B C C C D F D G D D K J E B J G

exp72-chk/stats_sol-size 51, time 112629: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop (y - 1) (x - y) x) x x)) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)

exp72-chk/stats_sol-K L F B L D A K K A B L D I E K K J E B L B E K L E K J K K J N K L F A K K A B L D I E K K J E B J G

--

exp73-chk/stats_sol:https://oeis.org/A7318 : 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 1 10 45 120 210 252 210 120 45 10 1 1 11 55 165 330 462 462 330 165 55 11 1

exp73-chk/stats_sol-size 89, time 22878: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x))) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1)

exp73-chk/stats_sol-K L F B L D A K K A B L D I E C C K B C C C D F D G D D K J E B B K L K E L A I E C C K B C C C D F D G D D K J D N K L F A K K A B L D I E C C K B C C C D F D G D D K J E B J G

exp73-chk/stats_sol-size 51, time 112629: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop (y - 1) (x - y) x) x x)) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)

exp73-chk/stats_sol-K L F B L D A K K A B L D I E K K J E B L B E K L E K J K K J N K L F A K K A B L D I E K K J E B J G

--

exp74-chk/stats_sol:https://oeis.org/A7318 : 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 1 10 45 120 210 252 210 120 45 10 1 1 11 55 165 330 462 462 330 165 55 11 1

exp74-chk/stats_sol-size 89, time 22878: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x))) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1)

exp74-chk/stats_sol-K L F B L D A K K A B L D I E C C K B C C C D F D G D D K J E B B K L K E L A I E C C K B C C C D F D G D D K J D N K L F A K K A B L D I E C C K B C C C D F D G D D K J E B J G

exp74-chk/stats_sol-size 51, time 112629: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop (y - 1) (x - y) x) x x)) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)

exp74-chk/stats_sol-K L F B L D A K K A B L D I E K K J E B L B E K L E K J K K J N K L F A K K A B L D I E K K J E B J G

--

exp75-chk/stats_sol:https://oeis.org/A7318 : 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 1 10 45 120 210 252 210 120 45 10 1 1 11 55 165 330 462 462 330 165 55 11 1

exp75-chk/stats_sol-size 89, time 22878: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x))) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1)

exp75-chk/stats_sol-K L F B L D A K K A B L D I E C C K B C C C D F D G D D K J E B B K L K E L A I E C C K B C C C D F D G D D K J D N K L F A K K A B L D I E C C K B C C C D F D G D D K J E B J G

exp75-chk/stats_sol-size 51, time 112629: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop (y - 1) (x - y) x) x x)) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)

exp75-chk/stats_sol-K L F B L D A K K A B L D I E K K J E B L B E K L E K J K K J N K L F A K K A B L D I E K K J E B J G

--

exp76-chk/stats_sol:https://oeis.org/A7318 : 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 1 10 45 120 210 252 210 120 45 10 1 1 11 55 165 330 462 462 330 165 55 11 1

exp76-chk/stats_sol-size 89, time 22878: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1 (1 + (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x))) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x)) 1)

exp76-chk/stats_sol-K L F B L D A K K A B L D I E C C K B C C C D F D G D D K J E B B K L K E L A I E C C K B C C C D F D G D D K J D N K L F A K K A B L D I E C C K B C C C D F D G D D K J E B J G

exp76-chk/stats_sol-size 51, time 112629: (loop2 (x \* y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1 (loop (loop (y - 1) (x - y) x) x x)) div (loop (x \* y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) x x)) 1)

exp76-chk/stats_sol-K L F B L D A K K A B L D I E K K J E B L B E K L E K J K K J N K L F A K K A B L D I E K K J E B J G

--

exp77-chk/stats_sol:https://oeis.org/A7318 : 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 1 10 45 120 210 252 210 120 45 10 1 1 11 55 165 330 462 462 330 165 55 11 1

exp77-chk/stats_sol-size 85, time 22566: (loop2 (x \* y) (1 + y) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x) 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x))) div (loop (x \* y) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x) 1)

exp77-chk/stats_sol-K L F B L D K L K E L A I E C C K B C C C D F D G D D K J B B K K A B L D I E C C K B C C C D F D G D D K J E N K L F K L K E L A I E C C K B C C C D F D G D D K J B J G

exp77-chk/stats_sol-size 46, time 106236: (loop2 (x \* y) (y - 1) (loop (x - (if (y - x) <= 0 then y else 0)) x x) 1 (loop (y div (2 + x)) (x + x) 0)) div (loop (x \* y) (loop (x - (if (y - x) <= 0 then y else 0)) x x) 1)

exp77-chk/stats_sol-K L F L B E K L K E L A I E K K J B L C K D G K K D A J N K L F K L K E L A I E K K J B J G

--

exp78-chk/stats_sol:https://oeis.org/A7318 : 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 1 10 45 120 210 252 210 120 45 10 1 1 11 55 165 330 462 462 330 165 55 11 1

exp78-chk/stats_sol-size 85, time 22566: (loop2 (x \* y) (1 + y) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x) 1 (1 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x))) div (loop (x \* y) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 \* (2 + 2)))))) x) 1)

exp78-chk/stats_sol-K L F B L D K L K E L A I E C C K B C C C D F D G D D K J B B K K A B L D I E C C K B C C C D F D G D D K J E N K L F K L K E L A I E C C K B C C C D F D G D D K J B J G

exp78-chk/stats_sol-size 46, time 106236: (loop2 (x \* y) (y - 1) (loop (x - (if (y - x) <= 0 then y else 0)) x x) 1 (loop (y div (2 + x)) (x + x) 0)) div (loop (x \* y) (loop (x - (if (y - x) <= 0 then y else 0)) x x) 1)
