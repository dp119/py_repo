# n = 6
# numbers = [1, 1, 2, 2, 2, 3]

# set1 = set(numbers)

import os



def countNonUnique(numbers):
    counter = 0
    for i in set1:
        if numbers.count(i) > 1:
            counter = counter + 1
    return counter


#print(countNonUnique(numbers))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = countNonUnique(numbers)

    fptr.write(str(result) + '\n')

    fptr.close()
