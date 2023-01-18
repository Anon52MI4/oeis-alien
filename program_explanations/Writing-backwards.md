### OEIS writing backwards 
In the iteration done on <2022-10-19> this was exploited in several new programs:

https://oeis.org/A71587
https://oeis.org/A071586
https://oeis.org/A004165

Code for the last one: L B C C C C D F D I K F L C C C C D F D H D L C G B C C D D G B K D A K K F K F B B K D J N

The python code for the last one:
```
def f1(X):
  x = 1 + X
  for y in range (1,1 + 1):
    x = (x * x) * x
  return x

def f0(X):
  x,y = 0, f1(X)
  for z in range (1,(1 + X) + 1):
    x,y = (((1 if y <= 0 else (2 + (2 * (2 + 2)))) * x) + (y % (2 + (2 * (2 + 2))))), ((y // 2) // (1 + (2 + 2)))
  return x

for x in range(32):
  print (f0(x))
```
