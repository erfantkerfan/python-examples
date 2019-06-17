# -*- coding: utf-8 -*-

n = int(input('enter n:'))
x = 0
for i in range(1, n+1):
    f = 1
    for j in range(1, i+1):
        f *= j
    x += 1/f
print(x)
