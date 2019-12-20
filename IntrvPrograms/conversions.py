# # <h2> Type Conversions (explicit)

# # h<4> String to Int

#     s = "1001"

#     i = int(s)

#     print(type(i))


# # h<4> Int to String

#     i = 1001
#     s = str(i)
#     print(type(s))

# # h<4> String to List

#     s = "youtube"
#     l = list(s)
#     print(l)


# # h<4> Integer to List

#     n = 12345

#     #l = list(i)
#     # Above step can be done for a string, but it does not work for integer. It returns error - INT object not iterable

#     # method 1 using for loop
#     l1 = []
#     for i in str(n):
#         l1.append(int(i))

#     print(l1)

#     # method 2 using map

#     l2 = list(map(int, str(n)))
#     print(l2)


# # List to Set

# l = [1, 2, 3, 4, 5]
# s = set(l)
# print(s)


# # Set to List

# s = {1, 2, 3, 4, 5}
# l = list(s)
# print(l)


# List to Dictionary


# Dictionary Key to List

# Dictionary Value to List

# Dictionary


# Tuples

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[2:5])
# ('cherry', 'orange', 'kiwi')

print(thistuple[-4:-1])
# ('orange', 'kiwi', 'melon')

print(thistuple[-1:-1])
# ()

print(thistuple[-1])
# mango




# <h6> Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# <h6> Add/Remove Tuple Values
#Same answer as above

# <h6> Create Tuple with Single Value
#NOTE : To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.

mytuple = ("apple",)
print(mytuple)
print(type(mytuple))


# <h6> Convert tuple into list

x = ("apple", "banana", "cherry")
y = list(x)

print(y)

# <h6> Convert list into tuple


l = ['apple', 'banana', 'cherry']
t = tuple(l)

print(t)

# <h6> Loop Through a Tuple

for i in t:
    print(i)

# <h6> Check if Item Exists

t = ('apple', 'banana', 'cherry')
if "apple" in t:
    print("YES")


# <h6> Tuple Length
    print(len(t))

# <h6> Join 2 tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# ('a', 'b', 'c', 1, 2, 3)

# <h6> count() on a tuple
# Returns the number of times a value appears in the tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
#returns 2

# <h6> index() method on a tuple
#Returns position of first occurence of a value in a tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(5)

print(x)
#returns 5

