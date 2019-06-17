# -*- coding: utf-8 -*-

n = int(input("enter number n:"))
s = 0
for i in range(1, n+1):
    s += int(input('enter numbers:'))
average = s / n
print(average)
