

# <h2> Python Advanced functions examples

# <h4> lambda function


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# lambda arguments : expression

# Use lambda functions when an anonymous function is required for a short period of time.

#General way of defining a function
def square(x):
    return x * x
print(square(4))


#Lambda way of defining function
sqr = lambda x: x * x
print(sqr(8))       # prints 64


ab = lambda a, b : a * b
print(ab(5, 6))      # prints 30

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))       #prints sum of all 3



#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n


mydoubler = myfunc(2)
print(mydoubler(11))

mytripler = myfunc(3)
print(mytripler(11))




# <h4> Map function

# map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.
#Syntax - map(fun, iter)

n = 12345

list1 = list(map(int, str(n)))
print(list1)



# Double all numbers using map and lambda 

numbers = (1, 2, 3, 4)

x = map(lambda x: x * 2, numbers)

print(list(x))		#[2, 4, 6, 8]

# Add two lists using map and lambda 

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]

z = list(map(lambda x, y: x + y, x, y))    
print(z)		# [5, 7, 9, 11]


# with map() listify the list of strings individually

l = ['sat', 'bat', 'cat', 'mat']
z = list(map(list, l))

print(z)            #listify the list of strings individually



# <h4> Filter function

# filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not

# filter(function, iterable)

Filter the array, and return a new array with only the values equal to or above 18:

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = list(filter(myFunc, ages))
print(adults)


# function that filters vowels 

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 

def vowels(x):
    if x in "aeiou":
        return True
    else:
        return False


v = list(filter(vowels, sequence))
print(v)

