# -*- coding: utf-8 -*-

a = int(input("enter number 1:"))
b = int(input("enter number 2:"))

x = a
if x > b:
    x = b
#
if a < b:
    x = a
elif b < a:
    x = b
#
if a < b:
    x = a
else:
    x = b

print(x)
