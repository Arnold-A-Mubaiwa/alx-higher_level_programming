#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_num = str(number)[-1]
int_last = int(last_num)
if int_last > 5:
    print(f"Last digit of {number} is {int_last} and is greater than 5")
elif int_last < 6 and int_last != 0:
    print(f"Last digit of {number} is {int_last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {int_last} and is 0")
