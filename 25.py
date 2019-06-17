# -*- coding: utf-8 -*-

n = int(input("enter number n:"))
x = 0
while n > 0:
    x = (10 * x) + (n % 10)
    n = (n - (n % 10)) / 10
print(x)
