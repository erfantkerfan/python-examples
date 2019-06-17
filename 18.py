# -*- coding: utf-8 -*-

string = input("enter a string with . in it:")
x = string.index(".")
print(x)

x = string.split(".")
x = len(x[0])
print(x)
