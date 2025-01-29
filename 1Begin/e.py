import math
a , b = map(int, input().split())
c = math.sqrt(a**2 + b**2)
peri = a + b + c
print(c)
print(peri)