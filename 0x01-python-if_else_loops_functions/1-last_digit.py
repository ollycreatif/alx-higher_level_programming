#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastdgt = number % 10
else:
    lastdgt = number % -10
if (lastdgt > 5):
    print("Last digit of {:d} is {:d} and is greater \
than 5".format(number, lastdgt))
elif (lastdgt == 0):
    print("Last digit of {:d} is {:d} and is 0".format(number, lastdgt))
elif (lastdgt < 6 and lastdgt != 0):
    print("Last digit of {:d} is {:d} and is less than 6 and \
not 0".format(number, lastdgt))
