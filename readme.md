
# <h1> Python Topics

# <h6> Python Language and Python Implementations


# <h6> Python Compiler and Portability


# <h5> Dynamic Language (like Javascript and Ruby)

	* Variable Declaration

To print the type of variable of an object in python
	
	x = 1
	print(type(x))
	
	print(type(1))
	print(type("a"))
	print(type(1.1))

Take Away : Python is a dynamic language which means the type of the variable is determined at run_time as opposed to compile time


	
# <h2> Type Annotation or Type Hinting



# <h2> Mutable and Immutable variables

	* Int is Immutable
	
	x = 1		#x points to memory address 2336032
	x = x + 1	#x points to memory address 2336045
	
Changes are applied on different memory location
This means the variable x is allocated to a new value in memory
	
	
	
	
	* Lists are mutable
	
	x = [1, 2, 3]
	print(id(x)) #2336078
	
	x.append(4)		
	print(id(4))
	
The changes are applied on the same memory location.
This means the variable name is allocated to same memory
	
	



	
# <h2> String Operations

	
	course = "Python Programming"

	print(len(course)) 			#prints lenght of string

	print(course[0:3])			#returns "Pyt"

	print(course[:3])			#returns "Pyt"

	print(course[0:])			#returns "Python Programming"

	print(course[:])			#returns "Python Programming"

	print(course[-1]) 			#returns "g"

	
# <h2> Escape Sequences

Escape character in python treats the next character as a string

	message = "Python \"Programming\" "

	message = "Python\'s Programming"

	message = "Python \\Programming"

	message = "Python \nProgramming"


# <h2> Formatted Strings

	first = "Deepak"
	last = "Prasad"
	full = f"{first} {last}"
	print(full)
	

	
	
# <h2> Print Variables and String in same line

	x = 1
	y = 2

	
	
	
# <h4> Using **,** to separate strings and variables while printing: 
(this automatically separtes the items by a single space)

	print("My kid is",x,"year old")

	
	

# <h4> Using concatenate **+** to separate strings and variables while printing: 
(this does not automatically separtes the items by a single space)
Also we need to convert any integer to string explicitly

	print("My kid is " + str(x) + " year old")
	

	
	
# <h4> Using format strings: 

	print("My kid is {} year old".format(x))
	
	Another example
	print("My kid is {} year old. She will be {} next year".format(x, y))


	

# <h2> Useful String Methods

	
	course = " Python Programming"
	
	print(course.upper())
	
	print(course.lower())
	
	print(course.title())
	
	print(course.strip())
	
	print(course.find("Pro"))		#find index of the character
									#string comparison's are case sensitive
									
	print(course.replace("P", "-"))
	
	print("Programming" in course)	#returns boolean True
	
	print("Programming" not in course)	#returns boolean False

	print(course.replace("Python", "Java"))
	
	print(course.startswith("Py")) 		#Returns Boolean True
	
	print(course.endswith("n"))			#Returns Boolean False
	
	print(course.count("o"))			#Returns number of times the character appears in the string
	
	
	
# <h2> Numbers

Binary representation of the numbers
	
	
	x = 10
	print(bin(x))		#prints binary representation of number 10
	
	x = 0x12c
	print(x)			#prints number decimal representation of the hexadecimal value
	
	print(hex(x))		#prints hexadecimal representation of given number
	
	

Arithmetic Operations
	
	
	x = 10 + 3
	x = 10 - 3
	x = 10 * 3
	x = 10 / 3		#returns float
	x = 10 // 3		#returns integer
	x = 10 % 3		#modulus returns remainder
	x = 10 ** 3		#power 
	

Augmented assignment operator	
	
	
	x = x + 1
	x += 1
	
	

There are no incremental operators unlike Java (x++ or x--)
	
	
# <h2> Working with Numbers

	*
	import math
	PI = 3.14		#by convention upper case variables are used for constants. Although this value can be changed, it's just a convention. Because there are no constants in python
	print(round(PI))
	print(abs(PI))
	
:exclamation: *Complete list of python built in functions available [here](https://docs.python.org/3/library/functions.html/)* 

	
:exclamation: *Complete list of methods in math module available [here](https://docs.python.org/3/library/math.html/)*

	
# <h2> Type Conversion

	
	input("x: ")
	y = x + 1 		#Returns type conversion error
	
Python is strongly typed language. It does not perform explicit type conversion
Javascript is weakly typed language. It does perform implicit type conversions
	
	
	
	print(int(x))		# 1
	print(float(x))		# 1.0
	print(bool(x))		# True
	print(str(x))		# 1
	
	
Truthy and Falsy Boolean Values.
Any of the below values, if we try to convert to boolean, the result will be false. Everything else is true

	
	bool(0)				# returns false
	bool("")			# returns false
	bool([])			# returns false
	bool(None)			# returns false
	bool("false")		# returns true
	
	
# <h2> Conditional Statements


		age = 22
		if age >= 18:
		  print("Adult")
		elif age >= 13:
		  print("Teenager")
		else:
		  print("child")
		  
		print("All done")
		


		if x > 1:
			pass	#use pass keyword to have an empty block
		else:
			pass
			
			
# <h2> Logical Operators


Eg for "not" operator: To find if given string is empty. If uses the concept of Falsy boolean

	name = " "
		
	if not name.strip():        #use strip to remove empty spaces
		print("Name is empty")
	else:
		print("Name is not empty")

Eg for "and" operator

	age = 22
	if age >= 18 and age <= 65:
		print("Eligible")

We could re-write above like below as well and eliminate "and"

	if 18 <= age < 65:
		print("Eligible")
		
# <h2> Ternary Operators

	message = "Eligible" if age >= 18 else "Not Eligible"
	
# <h2> Loops

For Loops
	for x in "Python":
		print(x)
		
	for x in ['a','b','c']:
		print(x)
		
	for x in range(5):
		print(x)
		
	for x in range(0, 10, 2):
		print(x)				#prints 0 2 4 6 8
		
		
Difference between list and range objects @1:14:00
	
# <h2> For..Else


	names = ["John", "Mary"]
	for name in names:
		if name.startswith("J"):
			print("Found")
			break
	else:
		print("Not found")	
	

# <h2> While Loops

	guess = 0
	answer = 5

	while answer =! guess:
		guess = int(input("Guess: "))
	else:
		pass



# <h2> Tuples (All about tuples)


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



# <h2> Functions



#Function returns single value

	def increment(number, by):
		return number + by


	print(increment(2, 3))

#Function returns multiple value

	def incrementby(number, by):
		return (number, number + by)  # returns a tuple (which is read only unlike lists)


	print(incrementby(2, 3))


#keyword argument

	print(increment(2, by=3))


#function with default value

	def increment(number, by=1):
		return (number, number + by)

	print(increment(2))


#Type hinting / type annotation in functions

	def increment(number: int, by: int =1) -> tuple:
		return (number, number + by)


# <h6> *args

#Function to multiply 2 arguments

	def multiplya(a, b):
		return a * b

	print(multiplya(2, 3))

#Function to multiply a variable number of arguments
#In this example we are passing 4 numbers, which are (2, 3, 4, 5). 
#The ones within small brackets is a tuple in python. To pass tuple in function definition, use (*list)

	def multiplyb(*list):
		print(list)

		total = 1
		for number in list:
			total *= number
		return total        


	print(multiplyb(2, 3, 4, 5))
	



# <h6> **args

#Function to take dictionary (key value pair) as arguments

	def save_user(**user):
		print(user)

		print(user["id"])
		print(user["name"])

	save_user(id=1, name="admin")


# <h2> Local variable and Global variable

#Local variable limited to a function

#Global variable is for the whole file

	message = "a"

	def greet():
		essage ="b"

	greet()
	print(message) # prints a

#To override we can use global keyword inside a function. But it's not recommended practice

	message = "a"

	def greet():
		global message
		message ="b"

	greet()
	print(message) # prints b
	

# <h2> Map, Filter and Reduce Functions in Python
	
# <h2> Explicit Type Conversions (datastructures)

# <h4> String to Int

    s = "1001"

    i = int(s)

    print(type(i))


# <h4> Int to String

    i = 1001
    s = str(i)
    print(type(s))

# <h4> String to List

    s = "youtube"
    l = list(s)
    print(l)


# <h4> Integer to List

    n = 12345

    #l = list(i)
# Above step can be done for a string, but it does not work for integer. It returns error - INT object not iterable

# method 1 using for loop
    l1 = []
    for i in str(n):
        l1.append(int(i))

    print(l1)

# method 2 using map

    l2 = list(map(int, str(n)))
    print(l2)



# List to Set

	l = [1, 2, 3, 4, 5]
	s = set(l)
	print(s)


# Set to List

	s = {1, 2, 3, 4, 5}
	l = list(s)
	print(l)


#List to Dictionary

#Dictionary Key to List

#Dictionary Value to List

#Dictionary 

#HashMap

#Lambda function

#Zip Function

#Komposite, Kafka, Airflow

#All the python libraries used

Difference between lists and tuple

What is PEP 8
PEP 8, sometimes spelled PEP8 or PEP-8, is a document that provides guidelines and best practices on how to write Python code

What is keyword argument

# <h2> Debugging in VS Code discussed at 1:33

# <h2> VS Code tricks at 1:36

Shortcuts

To comment multiple, select all the line and 

	ctrl + /
	
To run code

	Alt + Ctrl + N
	
To move the line up, () select the line 
	
	ALT + UP arrow
	

open command pallete by ctrl + shift + p

Installing VS Code Extensions

****LINTER****
select and install linter



****FORMAT****
select format document
In settings choose the option - Format on Save 


****CODE RUNNER****


# <h5> *Learn more about markdown [here](https://guides.github.com/features/mastering-markdown/)*