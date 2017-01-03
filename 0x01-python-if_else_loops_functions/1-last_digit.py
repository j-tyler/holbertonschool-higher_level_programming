#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 == 0:
    print("Last digit of {} is 0 and is 0".format(number))
elif number < 0:
    print("Last digit of {} is {}".format(number, (10 - number % 10) * -1),
          "and is less than 6 and not 0")
elif number % 10 < 6:
    print("Last digit of {} is {}".format(number, number % 10),
          "and is less than 6 and not 0")
else:
    print("Last digit of {} is {}".format(number, number % 10),
          "and is greater than 5")
