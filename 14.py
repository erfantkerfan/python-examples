a = int(input('enter starting number:'))
b = int(input('enter ending number:'))
sum = 0
for i in range(a, b+1):
    sum += 1/i
print(sum)
