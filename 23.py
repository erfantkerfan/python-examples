# -*- coding: utf-8 -*-

n = int(input("enter number n:"))
for i in range(n+1, 1, -1):
    for j in range(i, 1, -1):
        print("* ", end="")
    print()
