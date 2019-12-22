
# using the sort() function with reverse flag. It reverses the list permanently
thislist = [1, 2, 3, 4, 5]
thislist.sort(reverse=True)
print(thislist)         # [5, 4, 3, 2, 1]

# Using the slicing technique
# returns [1, 2, 3, 4, 5], NOTE: list was already reversed in above step
print(thislist[::-1])


# reverse() function does in-place operations. It reverses the list permanently (i.e. change the list)
thislist1 = [1, 2, 3, 4, 5]
thislist1.reverse()
print(thislist1)


# reversed() function is often used to iterate the list in reverse. It does not make changes to the list.
thislist2 = [1, 2, 3, 4, 5]
newlist = []
for i in reversed(thislist2):
    print(i)  # prints list in reverse order

print(thislist2)  # still returns [1, 2, 3, 4, 5]
