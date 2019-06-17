# -*- coding: utf-8 -*-

x = int(input("enter a number:"))
# x = 35
y = x % 10
x = (x - y)/10
y = 10 * y + x
print(y)
