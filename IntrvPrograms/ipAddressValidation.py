# n = int(input())
# l1 = []

# for i in range(n):

#     e = str(input())
#     l1.append(e)


# print(l1)

import re
n = 2
l1 = ['1050:1000:1000:a000:5:600:300c:326b', '22.231.113.64']

regex4 = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

regex6 = '''^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$'''


def check(IP):

    for i in range(len(l1)):
        Ip = l1[i]
    # pass the regular expression
    # and the string in search() method
        if(re.search(regex4, Ip)):
            print("IPv4")
        elif(re.search(regex6, Ip)):
            print("IPv6")
        else:
            print("Invalid Ip address")


check(l1)
