# <h2> Type Conversions (explicit)

# String to Int

# s = "1001"

# i = int(s)

# print(type(i))


# Int to String

# i = 1001
# s = str(i)
# print(type(s))

# String to List

# s = "youtube"
# l = list(s)
# print(l)


# Integer to List

n = 12345

#l = list(i)
# Above step can be done for a string, but it does not work for integer. It returns error - INT object not iterable


l = []
for i in str(n):
    l.append(int(i))

print(l)


