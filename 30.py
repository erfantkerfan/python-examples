# -*- coding: utf-8 -*-

n = int(input("enter number n:"))
for i in range(1, n+1):
    if n % i == 0:
        print(i)
