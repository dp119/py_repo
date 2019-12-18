# Given input number, print it in words
# This solution should work upto 5 digits

print("Enter a number: ")
n = int(input())
#n = 780

one_digits = ["", "one", "two", "three",
                 "four", "five", "six", "seven", "eight", "nine"]


# it is to make array indexing simple
two_digits = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

# The first two string are not used,
# they are to make array indexing simple
tens_multiple = ["", "", "twenty", "thirty", "forty",
                 "fifty", "sixty", "seventy", "eighty", "ninety"]


# number = list(map(int, str(n)))

# convert given number to list. 
# NOTE: Below method stores the number to list in reverse order
number = [0, 0, 0, 0, 0]
i = 0
while n > 0:
    number[i] = n % 10
    n = n // 10
    i += 1

# print(number)
InWords = ""

if len(number) > 5:
    print("Given number is more than 5 digits. Please enter a 5 digit number")


# NOTE: Below list has given number in reverse order. Hence traversing the list from right to left
# this is to decide the thousands place

if number[4] != 0:
    if number[4] == 1:
        InWords += two_digits[number[3]] + " thousand "
    else:
        InWords += tens_multiple[number[4]] + " " + one_digits[number[3]] + " thousand "
else:
    if number[3] != 0:
        InWords += one_digits[number[3]] + " thousand "

# this is to decide the hundredth place
if number[2] != 0:
    InWords += one_digits[number[2]]  + " hundred "


# this is to decide the tenth and units place
if number[1] != 0:
    if number[1] == 1:
        InWords += two_digits[number[1]] 
    else:
        InWords += tens_multiple[number[1]] + " " + one_digits[number[0]]
else:
    if number[0] != 0:
        InWords += one_digits[number[0]] 

print(InWords)