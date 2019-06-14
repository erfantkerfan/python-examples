x = 352
for f in range(0, 501):
    for e in range(0, 251):
        for d in range(0, 101):
            for c in range(0, 51):
                for b in range(0, 6):
                    for a in range(0, 3):
                        if ((250*a) + (100*b) + (10*c) + (5*d) + (2*e) + (1*f)) == x:
                            print("250*", a, "+ 100*", b, "+ 10*", c, "+ 5*", d, "+ 2*", e, "+ 1*", f)
