# -*- coding: utf-8 -*-

n = int(input("enter number n:"))
x = 0
for i in range(1, n+1):
    if n % i == 0:
        x += 1
if x == 2:
    print('PRIME')
else:
    print("NOT PRIME")
