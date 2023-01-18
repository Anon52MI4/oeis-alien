### Number of pairs of functions (f,g) from a set of n elements into itself satisfying f(x) = f(g(f(x))).

https://oeis.org/A239768 : 1 1 10 195 6808 362745 26848656 2621263519 324981308800 49669569764433 9146879704748800 1993011341241988551 506190915590699695104 148000190814308473203433 49289886405448749446514688 18529196186934893511062427375 7800708229072237749055062900736 3652486190893312491910941333813537

size 200, time 406817: loop2 ((loop ((((loop2 ((loop2 (x * y) y x 1 (y - 1)) * ((loop2 (x * y) (1 + y) x 1 y) div (loop (x * y) x 1))) 0 1 (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) (1 - (loop (x - (if x <= 0 then 0 else y)) (1 + (2 + (x div (1 + (2 + 2))))) (1 + x)))) * (loop2 (x * y) y (loop (x - (if (y - x) <= 0 then y else 0)) (2 + (x div (1 + (2 + 2)))) x) 1 ((loop2 ((if y <= 0 then 0 else 1) + x) (y - x) (2 + (x div (1 + (2 + 2)))) 2 x) - 2))) * (loop2 (x * y) (1 + y) (0 - (loop (x - (if x <= 0 then 0 else (1 + y))) (2 + (x div (1 + (2 + 2)))) x)) 1 (loop (loop y (x - y) x) x (1 + x)))) div (loop (x * y) (0 - (loop (x - (if x <= 0 then 0 else x)) 1 x)) 1)) 1 y) + x) (1 + y) (1 + x) 0 (((x * x) + x) div 2)

K L F L K B L B E N K L F B L D K B L N K L F K B J G F A B K L K E L A I E C K B C C D D G D K J B K K A L I E B C K B C C D D G D D B K D J E N K L F L K L K E L A I E C K B C C D D G D K J B L A B I K D L K E C K B C C D D G D C K N C E N F K L F B L D A K K A B L D I E C K B C C D D G D K J E B L K L E K J K B K D J N F K L F A K K A K I E B K J E B J G B L J K D B L D B K D A K K F K D C G N

#### Explanation of the Python code

```
""" product of all the numbers of a given iterator
"""
def product(xs):
    res = 1
    for x in xs:
        res *= x
    return res

def factorial(n):
    return product(range(1, n+1))

def binom(n,k):
    return product(range(n-k+1,n+1)) // factorial(k)

def catalan(n):
    return binom(2*n,n) // (n+1)

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

def f3(X,Y):
    x,y = 1, Y - 1
    for z in range (1,X + 1):
        x,y = (x * y), y
    return x

def f3a(X,Y):
    return (Y-1)**X

for x in range(32):
    for y in range(32):
        assert f3(x,y) == f3a(x,y)

def f4(X,Y):
    x,y = 1, Y
    for z in range (1,X + 1):
        x,y = (x * y), (1 + y)
    return x

def f4a(X,Y):
    return product(range(Y, Y+X))

for x in range(32):
    for y in range(32):
        assert f4(x,y) == f4a(x,y)

def f5(X):
    x = 1
    for y in range (1,X + 1):
        x = x * y
    return x

f5a = factorial

for x in range(32):
    assert f5(x) == f5a(x)

def f6(X):
    x = X
    for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
        x = x - (y if (y - x) <= 0 else 0)
    return x

def f6a(X):
    a,b = triangle_index(X)
    return b

for x in range(1000):
    assert f6(x) == f6a(x)

def f7(X):
    x = 1 + X
    for y in range (1,(1 + (2 + (X // (1 + (2 + 2))))) + 1):
        x = x - (0 if x <= 0 else y)
    return x

def f7a(X):
    a,b = triangle_index(X)
    return b-a

for x in range(1000):
    assert f7(x) == f7a(x)

def f2(X):
    x,y = f6(X), 1 - f7(X)
    for z in range (1,1 + 1):
        x,y = (f3(x,y) * (f4(x,y) // f5(x))), 0
    return x

def f2a(X):
    a,b = triangle_index(X)
    return (a-b)**b * binom(a,b)

for x in range(32):
    assert f2(x) == f2a(x)

def f9(X):
    x = X
    for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
        x = x - (y if (y - x) <= 0 else 0)
    return x

f9a = f6a

for x in range(1000):
    assert f9(x) == f9a(x)

def f10(X):
    x,y = 2, X
    for z in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
        x,y = ((0 if y <= 0 else 1) + x), (y - x)
    return x

def f10a(X):
    a,b = triangle_index(X)
    return a+2

for x in range(1000):
    assert f10(x) == f10a(x)

def f8(X):
    x,y = 1, f10(X) - 2
    for z in range (1,f9(X) + 1):
        x,y = (x * y), y
    return x

def f8a(X):
    a,b = triangle_index(X)
    return a**b

for x in range(32):
    assert f8(x) == f8a(x)

def f12(X):
    x = X
    for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
        x = x - (0 if x <= 0 else (1 + y))
    return x

def f12a(X):
    a,b = triangle_index(X)
    return b-a

for x in range(1000):
    assert f12(x) == f12a(x)

def f14(X,Y):
    x = X
    for y in range (1,(X - Y) + 1):
        x = y
    return x

def f14a(X,Y):
    if X <= Y: return X
    else: return X - Y

for x in range(32):
    for y in range(32):
        assert f14(x,y) == f14a(x,y)

def f13(X):
    x = 1 + X
    for y in range (1,X + 1):
        x = f14(x,y)
    return x

def f13a(X):
    a,b = triangle_index(X)
    return b+1

for x in range(100):
    assert f13(x) == f13a(x)

def f11(X):
    x,y = 1, f13(X)
    for z in range (1,(0 - f12(X)) + 1):
        x,y = (x * y), (1 + y)
    return x

def f11a(X):
    a,b = triangle_index(X)
    return product(range(b+1, a+1))

for x in range(32):
    assert f11(x) == f11a(x)

def f16(X):
    x = X
    for y in range (1,1 + 1):
        x = x - (0 if x <= 0 else x)
    return x

def f16a(X):
    return min(X,0)

for x in range(-100,100):
    assert f16(x) == f16a(x)

def f15(X):
    x = 1
    for y in range (1,(0 - f16(X)) + 1):
        x = x * y
    return x

def f15a(X):
    x = 1
    return factorial(-X)

for x in range(-32, 32):
    assert f15(x) == f15a(x)

def f1(X,Y):
    x = Y
    for y in range (1,1 + 1):
        x = ((f2(x) * f8(x)) * f11(x)) // f15(x)
    return x

def f1a(X):
    a,b = triangle_index(X)
    # X is non-negative numbers
    assert factorial(-X) == 1
    return (a-b)**b * binom(a,b) * a**b * product(range(b+1, a+1)) // factorial(-X)

for x in range(32):
    assert f1(0,x) == f1a(x)

def f0(X):
    x,y = 0, ((X * X) + X) // 2
    for z in range (1,(1 + X) + 1):
        x,y = (f1(x,y) + x), (1 + y)
    return x

def f0a(X):
    return sum(
        (X-b)**b * binom(X,b) * X**b * product(range(b+1, X+1))
        for b in range(0,X+1)
    )

for x in range(32):
    print (f0(x))
    assert f0(x) == f0a(x)
```
