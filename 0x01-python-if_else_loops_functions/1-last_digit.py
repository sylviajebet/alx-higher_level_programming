#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# find last digit for ngatives and positives
if number < 0:
    lastDgt = -((-1*number) % 10)
else:
    lastDgt = number % 10

# output the last digit of the number
if lastDgt == 0:
    print(f"Last digit of {number:d} is {lastDgt:d} and is 0")
elif lastDgt > 5:
    print(f"Last digit of {number:d} is {lastDgt:d} and is greater\
 than 5")
elif lastDgt < 6 and lastDgt != 0:
    print(f"Last digit of {number:d} is {lastDgt:d} and is\
 less than 6 and not 0")
