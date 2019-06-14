x = 352
i = x
for f in range(0, 501):
    for e in range(0, 251):
        for d in range(0, 101):
            for c in range(0, 51):
                for b in range(0, 6):
                    for a in range(0, 3):
                        if ((250*a) + (100*b) + (10*c) + (5*d) + (2*e) + (1*f)) == x:
                            if a + b + c + d + e + f < i:
                                x = "250*" + str(a) + "+ 100*" + str(b) + "+ 10*" + str(c) + "+ 5*" + str(d) + "+ 2*" \
                                    + str(e) + "+ 1*" + str(f)
print(x)
