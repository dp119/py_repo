# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


########### ###########
########### Tuples ###########
########### ###########


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# print(thistuple[2:5])
# # ('cherry', 'orange', 'kiwi')

# print(thistuple[-4:-1])
# # ('orange', 'kiwi', 'melon')

# print(thistuple[-1:-1])
# # ()

# print(thistuple[-1])
# # mango


# # <h6> Change Tuple Values
# #Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# #But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# # <h6> Add/Remove Tuple Values
# #Same answer as above

# # <h6> Create Tuple with Single Value
# #NOTE : To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.

# mytuple = ("apple",)
# print(mytuple)
# print(type(mytuple))


# # <h6> Convert tuple into list

# x = ("apple", "banana", "cherry")
# y = list(x)

# print(y)

# # <h6> Convert list into tuple


# l = ['apple', 'banana', 'cherry']
# t = tuple(l)

# print(t)

# # <h6> Loop Through a Tuple

# for i in t:
#     print(i)

# # <h6> Check if Item Exists

# t = ('apple', 'banana', 'cherry')
# if "apple" in t:
#     print("YES")


# # <h6> Tuple Length
#     print(len(t))

# # <h6> Join 2 tuples

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# # ('a', 'b', 'c', 1, 2, 3)

# # <h6> count() on a tuple
# # Returns the number of times a value appears in the tuple

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.count(5)

# print(x)
# #returns 2

# # <h6> index() method on a tuple
# #Returns position of first occurence of a value in a tuple

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.index(5)

# print(x)
# #returns 5


########### ###########
########### Lists ###########
########### ###########


# #Lists are similar to Tuples, except that Lists are editable/mutable

# #Additionaly, lists have below methods
# # append()	    Adds an element at the end of the list
# # clear()	    Removes all the elements from the list
# # copy()	    Returns a copy of the list
# # count()	    Returns the number of elements with the specified value
# # extend()	    Add the elements of a list (or any iterable), to the end of the current list
# # index()	    Returns the index of the first element with the specified value
# # insert()	    Adds an element at the specified position
# # pop()	        Removes the element at the specified position
# # remove()	    Removes the item with the specified value
# # reverse()	    Reverses the order of the list
# # sort()	    Sorts the list

# #The del keyword removes the specified index:

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# #More on sort() function

# #list.sort(reverse=True|False, key=myFunc)

# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort()
# print(cars)
# #['BMW', 'Ford', 'Volvo']

# cars.sort(reverse=True)
# print(cars)
# #['Volvo', 'Ford', 'BMW']



# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

# #Below length function is passed as a parameter  to sort function and it sorts based on len of string
# def myFunc(e):
#   return len(e)

# cars.sort(key=myFunc)
# print(cars)
# #ascending output
# #['VW', 'BMW', 'Ford', 'Mitsubishi']

# cars.sort(reverse=True, key=myFunc)
# print(cars)
# #descending output
# #['Mitsubishi', 'Ford', 'BMW', 'VW']



########### ###########
########### Dictionary ###########
########### ###########


#A dictionary is a collection which is unordered, changeable and indexed. 
#In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)
#same result as above

#Change the "year" to 2018:
thisdict["year"] = 2018
print(thisdict)

print(len(thisdict))

# <h4>Looping through a dictionary
#Print all key names in the dictionary, one by one
for x in thisdict:
    print(x)

#Print all values  in the dictionary, one by one
#NOTE: this loops through the keys
for x in thisdict:
    print(thisdict[x])

#You can also use the values() function to return values of a dictionary:
#NOTE: this loops through the values
for x in thisdict.values():
  print(x)

#Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
    print(x, y)

# <h4> Check if key exists

#Check if "model" is present in the dictionary
if "model" in thisdict:
    print("Yes")

#Check if value exists
if "Mustang" in thisdict.values():
    print("Yes")

#Adding Items

thisdict["color"] = "red"
print(thisdict)

#NOTE: remove() function exists for list and not for a dictionary
thisdict.pop("color")

print(thisdict)

#popitem() method removes the last inserted item
#NOTE: In versions older than 3.7, some random item is removed instead of last item


#It is also possible to use the dict() constructor to make a new dictionary:

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict) 


#A dictionary can also contain many dictionaries, this is called nested dictionaries.