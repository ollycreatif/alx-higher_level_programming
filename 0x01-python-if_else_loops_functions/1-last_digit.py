#!/usr/bin/python3
# import random
# number = random.randint(-10000, 10000)
number = -126

if number < 0:
    number = -1 * number

if number % 10 > 5:
    print("Last digit of {} is {} and is greater \
than 5".format(number, number % 10))
elif number % 10 == 0:
    print("Last digit of {} is {} and is 0".format(number, number % 10))
elif number != 0 and number < 6:
    print("Last digit of {} is {} and is greater \
than 5".format(number, number % 10))
