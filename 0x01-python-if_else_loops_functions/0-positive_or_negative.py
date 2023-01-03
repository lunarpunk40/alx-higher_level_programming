#!/usr/bin/python3

import random
number = random.randint(-10, 10)
print("{} is positive".format(number) if number> 0 else "{} is zero".format(number) if number == 0 else "{} is negative".format(number))


