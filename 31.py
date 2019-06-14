n = int(input("enter number n:"))
m = int(input("enter number m:"))
for i in range(1, min(n, m)+1):
    if (n % i == 0) and (m % i == 0):
        print(i)
