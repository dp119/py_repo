
# Jumping on the Clouds

# Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus or . She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.


# Function Description

# Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

# jumpingOnClouds has the following parameter(s):

# c: an array of binary integers


# Input Format

# The first line contains an integer n, the total number of clouds. The second line contains n space-separated binary integers describing clouds c[i] where 0 <= i < n.


# Sample Input 0

# 7
# 0 0 1 0 0 1 0

# Sample Output 0
# 4

# Explanation 0:
# Emma must avoid c[2] and c[5]. She can win the game with a minimum of 4 jumps


# Sample Input 1

# 6
# 0 0 0 0 1 0

# Sample Output 1

# 3

# Explanation 1:
# The only thundercloud to avoid is c[4]. Emma can win the game in 3 jumps


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.

n = 7
c = [0, 0, 1, 0, 0, 1, 0]



def jumpingOnClouds(c):
    counter = 0
    x = 0
    for i in c:
        if x >= n-2:
            counter = counter + 1
            break
        elif c[x+2] == 0:
            counter = counter + 1
            x = x + 2
            if x == n-1:
                break
        else:
            x = x + 1
            counter = counter + 1
        #print(x)

    return counter


print(jumpingOnClouds(c))
