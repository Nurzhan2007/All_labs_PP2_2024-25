a , b = map(int,input().split())
a = a ** 2
b = b ** 2
s = abs(a + b)
diff = abs(a - b)
m = abs(a * b)
d = abs(a / b)
print(s, diff, m ,d)