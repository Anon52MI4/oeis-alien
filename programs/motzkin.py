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

def f3(X):
    x = X
    for y in range (1,(2 + (X // 5)) + 1):
        x = x - (y if (y - x) <= 0 else 0)
    return x

def f3a(x):
    return triangle_index(x)[1]
for x in range(32):
    assert f3(x) == f3a(x)

def f5(X):
    x = X
    for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
        x = x - (0 if x <= 0 else (1 + y))
    return x

def f5a(X):
    a,b = triangle_index(X)
    return b-a
for x in range(32):
    assert f5(x) == f5a(x)

def f6(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (y if (y - x) <= 0 else 0)
  return x

f6a = f3a  # again the same definition
for x in range(32):
    assert f6(x) == f3a(x)

def f4(X):
    x,y = 1, 1 + f6(X)
    for z in range (1,(0 - f5(X)) + 1):
        x,y = (x * y), (1 + y)
    return x

def f4a(X):
    a,b = triangle_index(X)
    return product(range(1+b, 1+a))

for x in range(32):
    assert f4(x) == f4a(x)

def f2(X):
    x = f4(X)
    for y in range (1,f3(X) + 1):
        x = (((1 + 2) * (x * y)) // (2 + y)) + x
    return x

def f2a(X):
    a,b = triangle_index(X)    
    return product(range(1+b, 1+a)) * catalan(b+1)

for x in range(32):
    assert f2(x) == f2a(x)

def f8(X):
  x = X
  for y in range (1,(2 + (X // (1 + (2 + 2)))) + 1):
    x = x - (0 if x <= 0 else (1 + y))
  return x

f8a = f5a  # again the same definition

for x in range(32):
    assert f8(x) == f8a(x)

def f7(X):
    x = 1
    for y in range (1,(0 - f8(X)) + 1):
        x = x * y
    return x

def f7a(X):
    a,b = triangle_index(X)
    return factorial(a-b)

for x in range(32):
    assert f7(x) == f7a(x)

def f1(X,Y):
    x = Y
    for y in range (1,1 + 1):
        x = f2(x) // f7(x)
    return x

def f1a(X,Y):
    a,b = triangle_index(Y)
    return binom(a,b) * catalan(b+1)

for x in range(32):
    for y in range(32):
        assert f1(x,y) == f1a(x,y)

def f0(X):
    x,y = 1, 1 + (((X * X) + X) // 2)
    for z in range (1,X + 1):
        x,y = (f1(x,y) - x), (1 + y)
    return x

def f0a(X):
    return sum(
        binom(X,b) * catalan(b+1) * (-1)**(X-b)
        for b in range (0, X+1)
    )

for x in range(32):
    assert f0(x) == f0a(x)
    print (f0(x))
