# Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

# For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.

# Function Description

# Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

# countingValleys has the following parameter(s):

# n: the number of steps Gary takes
# s: a string describing his path

# Sample Input
# 8
# UDDDUDUU

# Sample Output
# 1

#!/bin/python3

import math
import os
import random
import re
import sys


s = "UDDDUDUU"
n = 8
# Complete the countingValleys function below.

sea_level = 0
U = 1
D = -1
list1 = []
x = 0
counter = 0


def countingValleys(n, s):
    x = 0
    counter = 0
    for i in range(len(s)):
        if s[i] == "U":
            list1.append(1)
        else:
            list1.append(-1)

    for i in range(len(s)):
        x = x + int(list1[i])
        y = x - int(list1[i])
        if x - int(list1[i]) < 0 and x == 0:
            counter = counter + 1
    return counter


print(countingValleys(n, s))
