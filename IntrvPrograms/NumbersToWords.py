# Given input number, print it in words
# This solution should work upto 5 digits

# print("Enter a number: ")
# n = input()
n = 2345

one_digits = ["zero", "one", "two", "three",
                 "four", "five", "six", "seven", "eight", "nine"]

# The first string is not used,
# it is to make array indexing simple
two_digits = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

# The first two string are not used,
# they are to make array indexing simple
tens_multiple = ["", "", "twenty", "thirty", "forty",
                 "fifty", "sixty", "seventy", "eighty", "ninety"]


# number = list(map(int, str(n)))

number = [0, 0, 0, 0, 0]
i = 0
while n > 0:
    number[i] = n % 10
    n = n // 10
    i += 1

print(number)
InWords = ""

if len(number) > 5:
    print("Given number is more than 5 digits. Please enter a 5 digit number")


if number[0] != 0:
    if number[0] == 1:
        InWords += two_digits[number[1]]
    else:
        InWords += one_digits[number[1]]

print(InWords)