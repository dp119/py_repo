n = 6
numbers = [1, 1, 2, 2, 2, 3, 4, 4]


def countNonUnique(numbers):
    set1 = set(numbers)
    counter = 0
    for i in set1:
        if numbers.count(i) > 1:
            counter = counter + 1
    return counter


print(countNonUnique(numbers))
