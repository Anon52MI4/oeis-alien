# Proliferation of coding of pairs of numbers (triangular index) in the iterations

The code:
```
(loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)
```

# Our explanation of the code:

To me, there are a few little steps between f3 and triangle_index. Such as

- Number 3+X//5 is large enough for it to basically be a while loop
- f3 makes one more step than triangle_index, that's why there must be one more subtraction afterwards in f3a.
- f3 starts with subtracting 2, so there is some +-1 shift.

```
def triangle_index(x):
  y = 0
  while x > y:
    y += 1
    x -= y
  return y,x

def f3(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f3a(X):
  a,b = triangle_index(X)
  return b-a

for x in range(100):
  assert f3(x) == f3a(x)
```

```
exp50-chk/stats_sol:0
exp51-chk/stats_sol:0
exp52-chk/stats_sol:0
exp53-chk/stats_sol:0
exp54-chk/stats_sol:0
exp55-chk/stats_sol:0
exp56-chk/stats_sol:0
exp57-chk/stats_sol:3
exp58-chk/stats_sol:6
exp59-chk/stats_sol:17
exp60-chk/stats_sol:25
exp61-chk/stats_sol:32
exp62-chk/stats_sol:34
exp63-chk/stats_sol:37
exp64-chk/stats_sol:48
exp65-chk/stats_sol:65
exp66-chk/stats_sol:84
exp67-chk/stats_sol:102
exp68-chk/stats_sol:114
exp69-chk/stats_sol:121
exp70-chk/stats_sol:138
exp71-chk/stats_sol:161
exp72-chk/stats_sol:185
exp73-chk/stats_sol:217
exp74-chk/stats_sol:244
exp75-chk/stats_sol:248
exp76-chk/stats_sol:273
exp77-chk/stats_sol:327
exp78-chk/stats_sol:385
exp79-chk/stats_sol:471
exp80-chk/stats_sol:505
exp81-chk/stats_sol:518
exp82-chk/stats_sol:530
exp83-chk/stats_sol:534
exp84-chk/stats_sol:539
exp85-chk/stats_sol:547
exp86-chk/stats_sol:554
exp87-chk/stats_sol:561
exp88-chk/stats_sol:560
exp89-chk/stats_sol:574
exp90-chk/stats_sol:565
exp91-chk/stats_sol:577
exp92-chk/stats_sol:609
exp93-chk/stats_sol:674
exp94-chk/stats_sol:775
exp95-chk/stats_sol:854
exp96-chk/stats_sol:919
exp97-chk/stats_sol:807
exp98-chk/stats_sol:824
exp99-chk/stats_sol:894
exp100-chk/stats_sol:888
exp101-chk/stats_sol:886
exp102-chk/stats_sol:905
exp103-chk/stats_sol:962
exp104-chk/stats_sol:997
exp105-chk/stats_sol:1009
exp106-chk/stats_sol:1004
exp107-chk/stats_sol:1046
exp108-chk/stats_sol:1092
exp109-chk/stats_sol:1124
exp110-chk/stats_sol:1163
exp111-chk/stats_sol:1170
```

### Proliferation when considering multiple uses in one program

```
exp50-chk/stats_sol:0
exp51-chk/stats_sol:0
exp52-chk/stats_sol:0
exp53-chk/stats_sol:0
exp54-chk/stats_sol:0
exp55-chk/stats_sol:0
exp56-chk/stats_sol:0
exp57-chk/stats_sol:3
exp58-chk/stats_sol:6
exp59-chk/stats_sol:17
exp60-chk/stats_sol:25
exp61-chk/stats_sol:32
exp62-chk/stats_sol:34
exp63-chk/stats_sol:37
exp64-chk/stats_sol:48
exp65-chk/stats_sol:66
exp66-chk/stats_sol:85
exp67-chk/stats_sol:104
exp68-chk/stats_sol:115
exp69-chk/stats_sol:124
exp70-chk/stats_sol:142
exp71-chk/stats_sol:175
exp72-chk/stats_sol:217
exp73-chk/stats_sol:268
exp74-chk/stats_sol:300
exp75-chk/stats_sol:302
exp76-chk/stats_sol:346
exp77-chk/stats_sol:452
exp78-chk/stats_sol:591
exp79-chk/stats_sol:747
exp80-chk/stats_sol:793
exp81-chk/stats_sol:813
exp82-chk/stats_sol:824
exp83-chk/stats_sol:825
exp84-chk/stats_sol:833
exp85-chk/stats_sol:848
exp86-chk/stats_sol:848
exp87-chk/stats_sol:863
exp88-chk/stats_sol:864
exp89-chk/stats_sol:887
exp90-chk/stats_sol:867
exp91-chk/stats_sol:895
exp92-chk/stats_sol:961
exp93-chk/stats_sol:1106
exp94-chk/stats_sol:1304
exp95-chk/stats_sol:1484
exp96-chk/stats_sol:1609
exp97-chk/stats_sol:1477
exp98-chk/stats_sol:1504
exp99-chk/stats_sol:1672
exp100-chk/stats_sol:1641
exp101-chk/stats_sol:1611
exp102-chk/stats_sol:1604
exp103-chk/stats_sol:1682
exp104-chk/stats_sol:1711
exp105-chk/stats_sol:1712
exp106-chk/stats_sol:1701
exp107-chk/stats_sol:1732
exp108-chk/stats_sol:1766
exp109-chk/stats_sol:1829
exp110-chk/stats_sol:1867
exp111-chk/stats_sol:1855
```

### E.g. here the coding is used twice (and there seem to be similar tricks there)

https://oeis.org/A108916 : 1 1 1 3 2 1 9 9 3 1 31 36 18 4 1 113 155 90 30 5 1 431 678 465 180 45 6 1 1697 3017 2373 1085 315 63 7 1 6847 13576 12068 6328 2170 504 84 8 1 28161 61623 61092 36204 14238 3906 756 108 9 1 117631 281610 308115 203640 90510 28476 6510 1080 135 10 1

size 199, time 109272: loop2 ((loop2 ((loop ((loop ((2 * ((2 * (x * y)) - x)) div (1 + y)) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) (loop2 (x * y) (y - 1) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1 (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1)) 1 y) + x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)) * ((loop2 (x * y) (1 + y) x 1 (1 + y)) div (loop (x * y) x 1))) 0 1 (0 - (loop (x - (if x <= 0 then 0 else y)) (2 + ((x div (1 + (2 + (2 + 2)))) + 2)) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)

C C K L F F K E F B L D G K L K E L A I E C K B C C D D G D K J K L F L B E A K K A B L D I E C K B C C D D G D K J E B K L K E L A I E C K B C C D D G D K J N J K L F A K K A B L D I E C K B C C D D G D K J E B J G B L J K D B L D B K D A K K F K D C G N K L F B L D K B B L D N K L F K B J G F A B A K K A L I E C K B C C C D D D G C D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N

```
def f4(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f6(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

def f7(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f5(X):
  x,y = 1, f7(X)
  for z in range (1,(0 - f6(X)) + 1):
    x,y = (x * y), (y - 1)
  return x

def f3(X):
  x = f5(X)
  for y in range (1,f4(X) + 1):
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

def f2(X,Y):
  x = Y
  for y in range (1,1 + 1):
    x = f3(x) // f8(x)
  return x

def f1(X):
  x,y = 0, ((X * X) + X) // 2
  for z in range (1,(1 + X) + 1):
    x,y = (f2(x,y) + x), (1 + y)
  return x

def f10(X,Y):
  x,y = 1, 1 + Y
  for z in range (1,X + 1):
    x,y = (x * y), (1 + y)
  return x

def f11(X):
  x = 1
  for y in range (1,X + 1):
    x = x * y
  return x

def f12(X):
  x = 1 + X
  for y in range (1,(2 + ((X // (1 + (2 + (2 + 2)))) + 2)) + 1):
    x = x - (0 if x <= 0 else y)
  return x

def f13(X):
  x = X
  for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

def f0(X):
  x,y = 0 - f12(X), f13(X)
  for z in range (1,1 + 1):
    x,y = (f1(x) * (f10(x,y) // f11(x))), 0
  return x

for x in range(32):
  print (f0(x))
```


