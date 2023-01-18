### Convolution of primes with themselves.

https://oeis.org/A14342 : 4 12 29 58 111 188 305 462 679 968 1337 1806 2391 3104 3953 4978 6175 7568 9185 11030 13143 15516 18177 21150 24471 28152 32197 36678 41543 46828 52621 58874 65659 73000 80949 89462 98631 108396 118869 130102 142071

size 127, time 3130033: loop2 ((loop (loop2 ((1 + (compr (x - (loop2 (loop (if (x mod (2 + y)) <= 0 then 0 else x) (y div (2 * (2 + 2))) (1 + y)) 0 (1 - (x mod 2)) 1 x)) (1 + x))) * (compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) y)) 0 1 (0 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (2 + (x div (1 + (2 * (2 + 2))))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (2 + (x div (1 + (2 * (2 + 2)))))) x)) 1 y) + x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

B K K C L D H A K I L C C C D F G B L D J A B K C H E B K N E B K D M D C K B L D H A K I K C E K J E L M F A B A K K A L I E B C C K B C C C D F D G D D D B K D J E K L K E L A I E C C K B C C C D F D G D D K J N B L J K D B L D B K D A K K F K D C G N

size 125, time 3536319: loop2 ((loop (loop2 ((1 + (compr (x - (loop2 (loop (if (x mod (2 + y)) <= 0 then 2 else x) (2 + (y div (2 * (2 + (2 + (2 + 2)))))) (1 + y)) 0 (1 - (x mod 2)) 1 x)) (1 + x))) * (compr (2 - (loop (if (x mod (1 + y)) <= 0 then 0 else x) (x - 2) x)) y)) 0 1 (0 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (x div (1 + (2 + 2))))) (1 + x))) (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x)) 1 y) + x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

B K K C L D H C K I C L C C C C C D D D F G D B L D J A B K C H E B K N E B K D M D C K B L D H A K I K C E K J E L M F A B A K K A L I E B C K B C C D D G D D B K D J E K L K E L A I E C K B C C D D G D K J N B L J K D B L D B K D A K K F K D C G N

```
from itertools import islice

""" product of all the numbers of a given iterator
"""
def product(xs):
    res = 1
    for x in xs:
        res *= x
    return res

def factorial(n):
    return product(range(1,n+1))

def binom(n,k):
    return product(range(n-k+1,n+1)) // factorial(k)

def catalan(n):
    return binom(2*n,n) // (n+1)

""" prime factorizartion
"""
def factorize(x):
    res = []
    p = 2
    while p*p <= x:        
        exp = 0
        while x % p == 0:
            x //= p
            exp += 1
        if exp: res.append((p,exp))
        p += 1
    if x != 1:
        res.append((x,1))
    return res

def is_prime(x):
    fac = factorize(x)
    return len(fac) == 1 and fac[0][1] == 1

def primes():
    yield 2
    yield 3
    x = 6
    while True:
        if is_prime(x-1): yield x-1
        if is_prime(x+1): yield x+1
        x += 6

def nth_prime(n):
    return next(islice(primes(), n, n+1))

""" enumerates numbers as
  (0,0)
  (1,0), (1,1)
  (2,0), (2,1), (2,2)
  ...
"""
def triangle_index(x):
    y = 0
    while x > y:
        y += 1
        x -= y
    return y,x
def from_triangle_index(y,x):
    return x + y*(y+1)//2

for x in range(32):
    assert from_triangle_index(*triangle_index(x)) == x

#### Matching with the generated code

def f5(X,Y):
    x = 1 + Y
    for y in range (1,(Y // (2 * (2 + 2))) + 1):
        x = 0 if (x % (2 + y)) <= 0 else x
    return x

def f5a(X):
    fac = factorize(X+1)
    if len(fac) > 2: return 0
    elif len(fac) == 2:
        if fac[0] != (2,1) or fac[1][1] != 1: return 0
    elif len(fac) == 1:
        if fac[0][0] == 2:
            if fac[0][1] > 4: return 0
        else:
            if fac[0][1] > 1: return 0
    return X+1

for x in range(1000):
    assert f5(0,x) == f5a(x)

def f4(X):
    x,y = 1, X
    for z in range (1,(1 - (X % 2)) + 1):
        x,y = f5(x,y), 0
    return x

def f4a(X):
    fac = factorize(X+1)
    if len(fac) > 0 and fac[0][0] == 2: return 1
    elif len(fac) > 1 or (len(fac) == 1 and fac[0][1] > 1): return 0
    else: return X+1

for x in range(1000):
    assert f4(x) == f4a(x)

def f3(X):
    x,i = 0,0
    while i <= 1 + X:
        if (x - f4(x)) <= 0:
            i = i + 1
        x = x + 1
    return x - 1

def f3a(X):
    return nth_prime(X)-1

for x in range(50):
    assert f3(x) == f3a(x)

def f7(X):
    x = X
    for y in range (1,(X - 2) + 1):
        x = 0 if (x % (1 + y)) <= 0 else x
    return x

def f7a(X):
    if X == 1 or is_prime(X): return X
    else: return 0

for x in range(1000):
    assert f7(x) == f7a(x)

def f6(X,Y):
    x,i = 0,0
    while i <= Y:
        if (2 - f7(x)) <= 0:
            i = i + 1
        x = x + 1
    return x - 1

def f6a(X):
    return nth_prime(X)

for x in range(50):
    assert f6(0,x) == f6a(x)

def f8(X):
    x = 1 + X
    for y in range (1,(1 + (2 + (2 + (X // (1 + (2 * (2 + 2))))))) + 1):
        x = x - (0 if x <= 0 else y)
    return x

def f8a(X):
    a,b = triangle_index(X)
    return b-a

for x in range(1000):
    assert f8(x) == f8a(x)

def f9(X):
    x = X
    for y in range (1,(2 + (2 + (X // (1 + (2 * (2 + 2)))))) + 1):
        x = x - (y if (y - x) <= 0 else 0)
    return x

def f9a(X):
    a,b = triangle_index(X)
    return b

for x in range(1000):
    assert f9(x) == f9a(x)

def f2(X):
    x,y = 0 - f8(X), f9(X)
    for z in range (1,1 + 1):
        x,y = ((1 + f3(x)) * f6(x,y)), 0
    return x

def f2a(X):
    a,b = triangle_index(X)
    return nth_prime(a-b) * nth_prime(b)

for x in range(100):
    assert f2(x) == f2a(x)

def f1(X,Y):
    x = Y
    for y in range (1,1 + 1):
        x = f2(x)
    return x

f1a = f2a

for x in range(100):
    assert f1(0,x) == f1a(x)

def f0(X):
    x,y = 0, ((X * X) + X) // 2
    for z in range (1,(1 + X) + 1):
        x,y = (f1(x,y) + x), (1 + y)
    return x

def f0a(X):
    return sum(
        f1a(x)
        for x in range(from_triangle_index(X,0), from_triangle_index(X,X)+1)
    )

for x in range(32):
    print( f0(x) )
    assert f0(x) == f0a(x)

```    
