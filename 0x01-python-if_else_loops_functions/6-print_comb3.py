#!/usr/bin/python3
for d1 in range(0, 10):
    for d2 in range(0, 10):
        if d1 < d2 and d1 != 8:
            print("{:d}{:d}".format(d1, d2), end=", ")
        elif d1 == 8 and d2 == 9:
            print("{:d}{:d}".format(d1, d2))
