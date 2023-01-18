exp26-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp26-chk/stats_sol-size 33, time 1666555: (if x <= 0 then 2 else 1) + (compr (((loop (x + x) (x mod 2) (loop (x * x) 1 (loop (x + x) (x div 2) 1))) + x) mod (1 + x)) x)

exp26-chk/stats_sol-K C B I K K D K C H K K F B K K D K C G B J J J K D B K D H K M D

--

exp31-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp31-chk/stats_sol-size 27, time 1614622: 1 + (compr ((((loop (x * x) 1 (loop (x + x) (x div 2) 1)) + x) * x) mod (1 + x)) (1 + x))

exp31-chk/stats_sol-B K K F B K K D K C G B J J K D K F B K D H B K D M D

--

exp33-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp33-chk/stats_sol-size 25, time 1578039: 1 + (compr (((loop (x * x) 1 (loop (x + x) (x div 2) 1)) + x) mod (1 + x)) (1 + x))

exp33-chk/stats_sol-B K K F B K K D K C G B J J K D B K D H B K D M D

exp33-chk/stats_sol-size 25, time 620769: 2 + (compr ((loop2 (1 + (if (x mod (1 + y)) <= 0 then 0 else x)) (y - 1) x 1 x) mod (1 + x)) x)

exp33-chk/stats_sol-C B K B L D H A K I D L B E K B K N B K D H K M D

--

exp35-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp35-chk/stats_sol-size 25, time 1578039: 1 + (compr (((loop (x * x) 1 (loop (x + x) (x div 2) 1)) + x) mod (1 + x)) (1 + x))

exp35-chk/stats_sol-B K K F B K K D K C G B J J K D B K D H B K D M D

exp35-chk/stats_sol-size 25, time 515990: 1 + (compr ((loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) x (1 + x)) mod (1 + x)) (1 + x))

exp35-chk/stats_sol-B K B L D H B L D K I K B K D J B K D H B K D M D

--

exp37-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp37-chk/stats_sol-size 25, time 1578039: 1 + (compr (((loop (x * x) 1 (loop (x + x) (x div 2) 1)) + x) mod (1 + x)) (1 + x))

exp37-chk/stats_sol-B K K F B K K D K C G B J J K D B K D H B K D M D

exp37-chk/stats_sol-size 33, time 98390: 1 + (compr ((loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 + (2 + 2)))) (1 + x)) mod (1 + x)) (1 + x))

exp37-chk/stats_sol-B K B L D H B L D K I C K C C C D D G D B K D J B K D H B K D M D

--

exp38-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp38-chk/stats_sol-size 33, time 98390: 1 + (compr ((loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 + (2 + 2)))) (1 + x)) mod (1 + x)) (1 + x))

exp38-chk/stats_sol-B K B L D H B L D K I C K C C C D D G D B K D J B K D H B K D M D

exp38-chk/stats_sol-size 23, time 519654: compr ((1 + (loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) x x)) mod (1 + x)) (2 + x)

exp38-chk/stats_sol-B K B L D H B L D K I K K J D B K D H C K D M

--

exp40-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp40-chk/stats_sol-size 35, time 96410: 1 + (compr ((loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (1 + ((2 + x) div (2 + (2 + 2)))) (1 + x)) mod (1 + x)) (1 + x))

exp40-chk/stats_sol-B K B L D H B L D K I B C K D C C C D D G D B K D J B K D H B K D M D

exp40-chk/stats_sol-size 23, time 519654: compr ((1 + (loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) x x)) mod (1 + x)) (2 + x)

exp40-chk/stats_sol-B K B L D H B L D K I K K J D B K D H C K D M

--

exp41-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp41-chk/stats_sol-size 35, time 96410: 1 + (compr ((loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (1 + ((2 + x) div (2 + (2 + 2)))) (1 + x)) mod (1 + x)) (1 + x))

exp41-chk/stats_sol-B K B L D H B L D K I B C K D C C C D D G D B K D J B K D H B K D M D

exp41-chk/stats_sol-size 19, time 517494: compr (x - (loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) x x)) (2 + x)

exp41-chk/stats_sol-K K B L D H B L D K I K K J E C K D M

--

exp42-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp42-chk/stats_sol-size 35, time 96410: 1 + (compr ((loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (1 + ((2 + x) div (2 + (2 + 2)))) (1 + x)) mod (1 + x)) (1 + x))

exp42-chk/stats_sol-B K B L D H B L D K I B C K D C C C D D G D B K D J B K D H B K D M D

exp42-chk/stats_sol-size 19, time 223464: compr (x - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (x div 2) x)) (2 + x)

exp42-chk/stats_sol-K K B L D H C K I K C G K J E C K D M

--

exp43-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp43-chk/stats_sol-size 33, time 94610: 1 + (compr ((loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (1 + (x div (2 + (2 + 2)))) (1 + x)) mod (1 + x)) (1 + x))

exp43-chk/stats_sol-B K B L D H B L D K I B K C C C D D G D B K D J B K D H B K D M D

exp43-chk/stats_sol-size 19, time 444324: compr ((x - (loop (if (x mod (1 + y)) <= 0 then y else x) x x)) - 2) (2 + x)

exp43-chk/stats_sol-K K B L D H L K I K K J E C E C K D M

--

exp46-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp46-chk/stats_sol-size 35, time 56104: 1 + (compr ((loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x)) mod (1 + x)) (1 + x))

exp46-chk/stats_sol-B K B L D H B L D K I C K C C C C D D F G D B K D J B K D H B K D M D

exp46-chk/stats_sol-size 19, time 444324: compr ((x - (loop (if (x mod (1 + y)) <= 0 then y else x) x x)) - 1) (2 + x)

exp46-chk/stats_sol-K K B L D H L K I K K J E B E C K D M

--

exp47-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp47-chk/stats_sol-size 33, time 54484: 1 + (compr (x - (loop (if (x mod (1 + y)) <= 0 then (1 + y) else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) (1 + x))

exp47-chk/stats_sol-B K K B L D H B L D K I C K C C C C D D F G D B K D J E B K D M D

exp47-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp47-chk/stats_sol-C K B L D H A K I K C E K J E K M

--

exp59-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp59-chk/stats_sol-size 31, time 47552: 1 + (compr (x - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (2 + (x div (2 * (2 + (2 + 2))))) (1 + x))) (1 + x))

exp59-chk/stats_sol-B K K B L D H C K I C K C C C C D D F G D B K D J E B K D M D

exp59-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp59-chk/stats_sol-C K B L D H A K I K C E K J E K M

--

exp65-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp65-chk/stats_sol-size 33, time 42140: 1 + (compr (x - (loop (if (x mod (1 + y)) <= 0 then 2 else x) (1 + (2 + (x div (2 * (2 * (2 + 2)))))) (1 + x))) (1 + x))

exp65-chk/stats_sol-B K K B L D H C K I B C K C C C C D F F G D D B K D J E B K D M D

exp65-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp65-chk/stats_sol-C K B L D H A K I K C E K J E K M

--

exp98-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp98-chk/stats_sol-size 40, time 27698: 1 + (compr (x - (loop2 (loop (if (x mod (1 + y)) <= 0 then 2 else x) (2 + (y div (2 * (2 + (2 + 2))))) (1 + y)) 0 (1 - (x mod 2)) 1 x)) (1 + x))

exp98-chk/stats_sol-B K K B L D H C K I C L C C C C D D F G D B L D J A B K C H E B K N E B K D M D

exp98-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp98-chk/stats_sol-C K B L D H A K I K C E K J E K M

--

exp102-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp102-chk/stats_sol-size 42, time 24956: 1 + (compr (x - (loop2 (loop (if (x mod (1 + y)) <= 0 then 2 else x) (1 + (2 + (y div (2 * (2 * (2 + 2)))))) (1 + y)) 0 (1 - (x mod 2)) 1 x)) (1 + x))

exp102-chk/stats_sol-B K K B L D H C K I B C L C C C C D F F G D D B L D J A B K C H E B K N E B K D M D

exp102-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp102-chk/stats_sol-C K B L D H A K I K C E K J E K M

--

exp103-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp103-chk/stats_sol-size 42, time 23336: 1 + (compr (x - (loop2 (loop (if (x mod (2 + y)) <= 0 then 2 else x) (2 + (y div (2 * ((2 + 2) + (2 + 2))))) (1 + y)) 0 (1 - (x mod 2)) 1 x)) (1 + x))

exp103-chk/stats_sol-B K K C L D H C K I C L C C C D C C D D F G D B L D J A B K C H E B K N E B K D M D

exp103-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp103-chk/stats_sol-C K B L D H A K I K C E K J E K M

--

exp130-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp130-chk/stats_sol-size 40, time 23066: 1 + (compr (x - (loop2 (loop (if (x mod (2 + y)) <= 0 then 2 else x) (2 + (y div (2 * (2 * (2 + 2))))) (1 + y)) 0 (1 - (x mod 2)) 1 x)) (1 + x))

exp130-chk/stats_sol-B K K C L D H C K I C L C C C C D F F G D B L D J A B K C H E B K N E B K D M D

exp130-chk/stats_sol-size 17, time 437742: compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) x

exp130-chk/stats_sol-C K B L D H A K I K C E K J E K M

--

exp131-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp131-chk/stats_sol-size 40, time 23066: 1 + (compr (x - (loop2 (loop (if (x mod (2 + y)) <= 0 then 2 else x) (2 + (y div (2 * (2 * (2 + 2))))) (1 + y)) 0 (1 - (x mod 2)) 1 x)) (1 + x))

exp131-chk/stats_sol-B K K C L D H C K I C L C C C C D F F G D B L D J A B K C H E B K N E B K D M D

exp131-chk/stats_sol-size 17, time 509394: 2 + (compr (loop (x - (if (x mod (1 + y)) <= 0 then 0 else 1)) x x) x)

exp131-chk/stats_sol-C K K B L D H A B I E K K J K M D

--

exp146-chk/stats_sol:https://oeis.org/A40 : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271

exp146-chk/stats_sol-size 17, time 509394: 2 + (compr (loop (x - (if (x mod (1 + y)) <= 0 then 0 else 1)) x x) x)

exp146-chk/stats_sol-C K K B L D H A B I E K K J K M D

exp146-chk/stats_sol-size 38, time 19701: loop (1 + x) (1 - x) (1 + (2 * (compr (x - (loop (if (x mod (2 + y)) <= 0 then 1 else x) (2 + (x div (2 * (2 + 2)))) (1 + (x + x)))) x)))

exp146-chk/stats_sol-B K D B K E B C K K C L D H B K I C K C C C D F G D B K K D D J E K M F D J

