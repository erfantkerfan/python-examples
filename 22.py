# -*- coding: utf-8 -*-

n = int(input("enter number n:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("* ", end="")
    print()
