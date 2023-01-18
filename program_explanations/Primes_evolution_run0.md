exp54-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp54-chk/stats_sol-size 30, time 1631442: 1 + (compr ((1 - (loop x (x mod 2) (loop (x * x) 1 (loop (x + x) (x div 2) 1)))) mod (1 + x)) (1 + x))

exp54-chk/stats_sol-B B K K C H K K F B K K D K C G B J J J E B K D H B K D M D

--

exp55-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp55-chk/stats_sol-size 25, time 1577710: 1 + (compr ((1 - (loop (x * x) 1 (loop (x + x) (x div 2) 1))) mod (1 + x)) (1 + x))

exp55-chk/stats_sol-B B K K F B K K D K C G B J J E B K D H B K D M D

--

exp57-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp57-chk/stats_sol-size 25, time 1578039: 1 + (compr (((loop (x * x) 1 (loop (x + x) (x div 2) 1)) + x) mod (1 + x)) (1 + x))

exp57-chk/stats_sol-B K K F B K K D K C G B J J K D B K D H B K D M D

exp57-chk/stats_sol-size 25, time 1577710: 1 + (compr ((1 - (loop (x * x) 1 (loop (x + x) (x div 2) 1))) mod (1 + x)) (1 + x))

exp57-chk/stats_sol-B B K K F B K K D K C G B J J E B K D H B K D M D

--

exp61-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp61-chk/stats_sol-size 23, time 619149: 2 + (compr (x - (loop2 (1 + (if (x mod (1 + y)) <= 0 then 0 else x)) (y - 1) x 1 x)) x)

exp61-chk/stats_sol-C K B K B L D H A K I D L B E K B K N E K M D

--

exp72-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp72-chk/stats_sol-size 33, time 98390: 1 + (compr ((loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 + (2 + 2)))) (1 + x)) mod (1 + x)) (1 + x))

exp72-chk/stats_sol-B K B L D H B L D K I C K C C C D D G D B K D J B K D H B K D M D

exp72-chk/stats_sol-size 23, time 619149: 2 + (compr (x - (loop2 (1 + (if (x mod (1 + y)) <= 0 then 0 else x)) (y - 1) x 1 x)) x)

exp72-chk/stats_sol-C K B K B L D H A K I D L B E K B K N E K M D

--

exp73-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp73-chk/stats_sol-size 33, time 98390: 1 + (compr ((loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 + (2 + 2)))) (1 + x)) mod (1 + x)) (1 + x))

exp73-chk/stats_sol-B K B L D H B L D K I C K C C C D D G D B K D J B K D H B K D M D

exp73-chk/stats_sol-size 23, time 619149: 2 + (compr (x - (loop2 (1 + (if (x mod (1 + y)) <= 0 then 0 else x)) (y - 1) x 1 x)) x)

exp73-chk/stats_sol-C K B K B L D H A K I D L B E K B K N E K M D

--

exp77-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp77-chk/stats_sol-size 31, time 96770: 1 + (compr (x - (loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 + (2 + 2)))) (1 + x))) (1 + x))

exp77-chk/stats_sol-B K K B L D H B L D K I C K C C C D D G D B K D J E B K D M D

exp77-chk/stats_sol-size 19, time 517494: compr (x - (loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) x x)) (2 + x)

exp77-chk/stats_sol-K K B L D H B L D K I K K J E C K D M

--

exp79-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp79-chk/stats_sol-size 31, time 96770: 1 + (compr (x - (loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 + (2 + 2)))) (1 + x))) (1 + x))

exp79-chk/stats_sol-B K K B L D H B L D K I C K C C C D D G D B K D J E B K D M D

exp79-chk/stats_sol-size 19, time 223464: compr (x - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (x div 2) x)) (2 + x)

exp79-chk/stats_sol-K K B L D H C K I K C G K J E C K D M

--

exp81-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp81-chk/stats_sol-size 31, time 96770: 1 + (compr (x - (loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 + (2 + 2)))) (1 + x))) (1 + x))

exp81-chk/stats_sol-B K K B L D H B L D K I C K C C C D D G D B K D J E B K D M D

exp81-chk/stats_sol-size 19, time 437844: compr (x - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) (2 + x)

exp81-chk/stats_sol-K K B L D H A K I K C E K J E C K D M

--

exp85-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp85-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp85-chk/stats_sol-C K B L D H A K I K C E K J E K M

exp85-chk/stats_sol-size 54, time 90730: loop2 (x + y) ((y div 2) div (1 + (2 + 2))) (1 + x) (0 + (1 * (compr ((loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x)) mod (1 + x)) (1 + x)))) 1

exp85-chk/stats_sol-K L D L C G B C C D D G B K D A B K B L D H B L D K I C K C C C C D D F G D B K D J B K D H B K D M F D B N

--

exp86-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp86-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp86-chk/stats_sol-C K B L D H A K I K C E K J E K M

exp86-chk/stats_sol-size 52, time 89110: loop2 (x + y) ((y div 2) div (1 + (2 + 2))) (1 + x) (0 + (1 * (compr (x - (loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) (1 + x)))) 1

exp86-chk/stats_sol-K L D L C G B C C D D G B K D A B K K B L D H B L D K I C K C C C C D D F G D B K D J E B K D M F D B N

--

exp87-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp87-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp87-chk/stats_sol-C K B L D H A K I K C E K J E K M

exp87-chk/stats_sol-size 50, time 88994: loop2 (x + y) ((y div 2) div (1 + (2 + 2))) (1 + x) (0 + (compr (x - (loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) (1 + x))) 1

exp87-chk/stats_sol-K L D L C G B C C D D G B K D A K K B L D H B L D K I C K C C C C D D F G D B K D J E B K D M D B N

--

exp88-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp88-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp88-chk/stats_sol-C K B L D H A K I K C E K J E K M

exp88-chk/stats_sol-size 48, time 88878: loop2 (x + y) ((y div 2) div (1 + (2 + 2))) (1 + x) (compr (x - (loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) (1 + x)) 1

exp88-chk/stats_sol-K L D L C G B C C D D G B K D K K B L D H B L D K I C K C C C C D D F G D B K D J E B K D M B N

--

exp90-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp90-chk/stats_sol-size 63, time 86496: if (loop2 ((((y div 2) + y) mod 2) + x) (((y mod 2) * y) div 2) (2 * (2 * (2 + 2))) 1 x) <= 0 then 1 else (1 + (compr ((loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x)) mod (1 + x)) (1 + x)))

exp90-chk/stats_sol-L C G L D C H K D L C H L F C G C C C C D F F B K N B B K B L D H B L D K I C K C C C C D D F G D B K D J B K D H B K D M D I

exp90-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp90-chk/stats_sol-C K B L D H A K I K C E K J E K M

--

exp94-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp94-chk/stats_sol-size 58, time 77596: if (loop2 ((1 - ((if y <= 0 then 1 else y) mod 2)) + x) (y div 2) (2 * (2 * (2 + (2 + 2)))) 1 x) <= 0 then 1 else (1 + (compr (x - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) (1 + x)))

exp94-chk/stats_sol-B L B L I C H E K D L C G C C C C C D D F F B K N B B K K B L D H C K I C K C C C C D D F G D B K D J E B K D M D I

exp94-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp94-chk/stats_sol-C K B L D H A K I K C E K J E K M



