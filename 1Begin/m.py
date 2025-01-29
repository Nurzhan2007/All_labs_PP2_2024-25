import math
x1, y1, x2, y2, x3, y3 = map(int,input().split())
AB = math.sqrt((x2-x1)**2 + (y2-y1)**2)
BC = math.sqrt((x3-x1)**2 + (y3-y1)**2)
AC = math.sqrt((x3-x2)**2 + (y3-y2)**2)
pzh = (AB + AC + BC)/2
S = math.sqrt(pzh*(pzh-AB)*(pzh-BC)*(pzh-AC))
print(S)