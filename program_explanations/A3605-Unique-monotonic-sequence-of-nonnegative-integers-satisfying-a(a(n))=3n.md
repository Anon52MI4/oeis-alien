### Unique monotonic sequence of nonnegative integers satisfying a(a(n)) = 3n.

"a subject of the 5th problem of the 27th British Mathematical Olympiad in 1992" described in A. Gardiner, The Mathematical Olympiad Handbook: An Introduction to Problem Solving" (the problem was to find f(1992) ). 

https://oeis.org/A3605 : 0 2 3 6 7 8 9 12 15 18 19 20 21 22 23 24 25 26 27 30 33 36 39 42 45 48 51 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 84 87 90 93 96 99 102 105 108 111 114 117 120

size 31, time 121597: (x + x) - (loop ((loop (0 - 1) ((loop (loop y (x div (1 + 2)) x) (1 + 2) y) - 1) 1) + x) (x - 1) 0)

K K D A B E L K B C D G K J B C D L J B E B J K D K B E A J E

The invented program is wrong. Here is the explanation:

My Python program gives a different answer: 3789 . The "mistake" that the program generator did was introducing the constant 3 in f3 in the python code. In the right way, it should be an infinite loop. f3 is supposed to find the first digit of a given number Y written in ternary. But currently, it performs at most 3 divisions, so it fails to calculate correctly f3(X,81) -- it is supposed to be 1, but
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
