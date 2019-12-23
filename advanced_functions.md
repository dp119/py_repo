

# <h2> Python Advanced functions examples

# <h4> lambda function


#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

#lambda arguments : expression

#Use lambda functions when an anonymous function is required for a short period of time.

#General way of defining a function
	def square(x):
	    return x * x
	print(square(4))


#Lambda way of defining function
	sqr = lambda x: x * x
	print(sqr(8))       #prints 64


	ab = lambda a, b : a * b
	print(ab(5, 6))      #prints 30

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

#map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.
#Syntax - map(fun, iter)

	n = 12345

	list1 = list(map(int, str(n)))
	print(list1)



#Double all numbers using map and lambda 

	numbers = (1, 2, 3, 4)

	x = map(lambda x: x * 2, numbers)

	print(list(x))		#[2, 4, 6, 8]

#Add two lists using map and lambda 

	x = [1, 2, 3, 4]
	y = [4, 5, 6, 7]

	z = list(map(lambda x, y: x + y, x, y))    
	print(z)		#[5, 7, 9, 11]


#with map() listify the list of strings individually

	l = ['sat', 'bat', 'cat', 'mat']
	z = list(map(list, l))

	print(z)            #listify the list of strings individually



# <h4> Filter function

#filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not

#filter(function, iterable)

	Filter the array, and return a new array with only the values equal to or above 18:

	ages = [5, 12, 17, 18, 24, 32]

	def myFunc(x):
	  if x < 18:
	    return False
	  else:
	    return True

	adults = list(filter(myFunc, ages))
	print(adults)


#function that filters vowels 

	sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 

	def vowels(x):
	    if x in "aeiou":
	        return True
	    else:
	        return False


	v = list(filter(vowels, sequence))
	print(v)



#a list contains both even and odd numbers
#result contains odd numbers of the list
#result contains even numbers of the list

	seq = [0, 1, 2, 3, 5, 8, 13]

	odd = list(filter(lambda x: x % 2, seq))
	print(odd)

	even = list(filter(lambda x: x % 2 == 0, seq))
	print(even)



# <h4> Reduce function


#reduce() function returns an iterator were the items are filtered through a function to test if the item is accepted or not

#reduce is part of functools module
#filter(function, iterable)

	import functools

	lis = [1, 3, 5, 6, 2, ]

	#using reduce to compute sum of list

	print(functools.reduce(lambda a, b: a+b, lis))


	#using reduce to compute maximum element from list 

	print(functools.reduce(lambda a, b: a if a > b else b, lis))



#reduce() can also be combined with operator functions to achieve the similar functionality as with lambda functions and makes the code more readable

	import operator

	lis = [1, 3, 4, 10, 4]

	print(functools.reduce(operator.add, lis))


	print(functools.reduce(operator.mul, lis))


#reduce() vs accumulate()

#Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. But there are differences in the implementation aspects in both of these.

#reduce() is defined in “functools” module, accumulate() in “itertools” module.
#reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a list containing the intermediate results. The last number of the list returned is summation value of the list.
#reduce(fun,seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.

	print(functools.reduce(operator.add, lis))  #prints 22


	import itertools 
	print(list(itertools.accumulate(lis,lambda x,y : x+y)))    #prints [1, 4, 8, 18, 22]