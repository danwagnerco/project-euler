"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
__author__ = "Dan Wagner"

from math import factorial

def evenly_divisible_by_one_through_twenty(num):
    checker = True
    for idx in range(11, 20):
        if not num % idx == 0:
            checker = False
            break
    return checker

maximum = factorial(20)
for n in range(20, maximum, 20):
    if evenly_divisible_by_one_through_twenty(n):
        print("Yay, {0} is dvisible by 1 through 20".format(n))
        break

