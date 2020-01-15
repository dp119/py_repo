#!/bin/python3

import math
import os
import random
import re
import sys

ip_array = ["This line has junk text", "121.18.19.20"]

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''


def checkIPs(ip_array):
    # Write your code here
    for i in range(len(ip_array)):
        # print(ip_array[i])
        #str = ip_array[i]
        if re.search(regex, ip_array[i]):
            print("IPv4")
        else:
            print("Neither")


checkIPs(ip_array)
