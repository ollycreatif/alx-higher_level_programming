#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    sum = 0
    n = len(argv)
    for i in range(n - 1):
        sum += int(argv[i + 1])
    print("{:d}".format(sum))
