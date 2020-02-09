

# <h1> Basic Programs

# <h2> List of python of libraries used

	os random re sys smtplib  logging csv ssl datetime
	math (round, abs), functools (reduce), operator(add, mul), itertools (accumulate), flask, json
	
	
# <h2> List of functions in the python Re module 

	import re
	txt = "The rain in Spain"
	x = re.findall("Portugal", txt)
	print(x)


	re.match(pattern, string, flags=0)

	
	re.search(pattern, string, flags=0)
	search() function searches the string for a match, and returns a Match object if there is a match
	
	NOTE: if you need to match at the beginning of the string, or to match the entire string use match. It is faster. Otherwise use search
	
	
	re.findall("ai", txt)
	findall() function returns a list containing all matches.
	
	split() function returns a list where the string has been split at each match
	x = re.split("\s", txt)		#returns a list of words which are seperated by space
	
	
	The sub() function replaces the matches with the text of your choice
	
	Replace every white-space character with the number 9:
	import re

	txt = "The rain in Spain"
	x = re.sub("\s", "9", txt)
	print(x)
	

A Match Object is an object containing information about the search and the result.	
Note: If there is no match, the value None will be returned, instead of the Match Object
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match


# <h2> List of functions in the python smtplib module 

	import smtplib

	smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
	
host − This is the host running your SMTP server. You can specify IP address of the host or a domain name like tutorialspoint.com. This is optional argument.

port − If you are providing host argument, then you need to specify a port, where SMTP server is listening. Usually this port would be 25.

local_hostname − If your SMTP server is running on your local machine, then you can specify just localhost as of this option.


	smtpObj.sendmail(sender, receivers, message)
	
	sender = 'from@fromdomain.com'
	
	receivers = ['to@todomain.com']
	
	message = """
	Subject: SMTP e-mail test
	This is a test e-mail message.
	"""


# <h2> List of functions in the python logging module 



With the logging module imported, you can use something called a “logger” to log messages that you want to see. By default, there are 5 standard levels indicating the severity of events. Each has a corresponding method that can be used to log events at that level of severity. The defined levels, in order of increasing severity, are the following:
	DEBUG
	INFO
	WARNING
	ERROR
	CRITICAL


	import logging

	logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
	logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


	logging.debug('This is a debug message')
	logging.info('This is an info message')
	logging.warning('This is a warning message')
	logging.error('This is an error message')
	logging.critical('This is a critical message')


You can customize the root logger even further by using more parameters for basicConfig()
The functions debug(), info(), warning(), error() and critical() will call basicConfig() automatically if no handlers are defined for the root logger.


# <h2> List of functions in the python os module 


	os.name 			#returns OS name
	os.chdir(
	os.listdir
	os.getcwd()			#
	os.error
	os.open()
	os.close()
	os.rename(


# <h2> List of functions in the python date module
	date.today().strftime
	datetime.date.today()
	datetime.timedelta(days=1)


# <h2> List of functions in the python filehandling module 


# <h2> List of functions in the python csv module


# <h2> What is PEP 8
PEP 8, sometimes spelled PEP8 or PEP-8, is a document that provides guidelines and best practices on how to write Python code

# <h2> What is keyword argument

# <h2> list vs tuple vs set

	

# <h2> Print String in reverse

# <h5> With String Slicing
	txt = "Hello World"[::-1]
	print(txt)


# <h5> With For loop
	txt = "Hello World"
	revStr = ""
	for i in txt:
		revStr = i + revStr

	print(revStr)


# <h5> With reverse() function
	txt = "Hello World"
	revStr1 = reversed(txt)
	print(''.join(revStr1))


# <h2> Print List in reverse

# <h5>  using the sort() function with reverse flag. It reverses the list permanently
	thislist = [1, 2, 3, 4, 5]
	thislist.sort(reverse=True)
	print(thislist)         # [5, 4, 3, 2, 1]

# <h5> Using the slicing technique

	print(thislist[::-1]) # returns [1, 2, 3, 4, 5], NOTE: list was already reversed in above step


# <h5> reverse() function does in-place operations. It reverses the list permanently (i.e. change the list)
	thislist1 = [1, 2, 3, 4, 5]
	thislist1.reverse()
	print(thislist1)


# <h5> reversed() function is often used to iterate the list in reverse. It does not make changes to the list.
	thislist2 = [1, 2, 3, 4, 5]
	newlist = []
	for i in reversed(thislist2):
		print(i)  # prints list in reverse order

	print(thislist2)  # still returns [1, 2, 3, 4, 5]


# <h2> Given list, list1 = [(1, 2), (3, 3), (1, 1)]. Sort it according to second element

	list1 = [(1, 2), (3, 3), (1, 1)]

	def sortSecond(val):
		return val[1]

	list1.sort(key=sortSecond) 
	#list.sort(reverse=True, key=sortSecond) for descending order

	print(list1)


# <h2> Remove duplicates from a list

# <h5> sol1
    test_list = [2, 4, 10, 20, 5, 2, 20, 4]


    def Remove(test_list):
        final_test_list = []
        for num in test_list:
            if num not in final_test_list:
                final_test_list.append(num)
        return final_test_list


    print(Remove(test_list))


# <h5> sol2 - converting into set


    test_list = [2, 4, 10, 20, 5, 2, 20, 4]

    A = list(set(test_list))
    print(A)



# <h5> sol3 - converting into dictionary

    mylist = ["a", "b", "a", "c", "c"]
    mylist = list( dict.fromkeys(mylist) )      #using list elements as keys for dictionary
    print(mylist)



# <h2> find factorial of a number



    print("Enter a number:")

    num = int(input())

    f = 1

    if f < 0:
        print("Factorial does'nt exist for negative number.")
    elif f == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1, 1 + num):
            # print(i)
            f = f * i
        print("Factorial of {} is {}".format(num, f))


# <h2> python program for simple interest



    #python program to find simple interest

    print("Enter the principal amount:")
    p = int(input())

    print("Enter the tenure:")
    t = int(input())

    print("Enter the rate of interest:")
    r = int(input())

    SI = int((p * t * r) / 100)

    print("Simple Interest is {}".format(SI))

# <h2> python program for compound interest


	def compound_interest(principle, rate, time):

		CI = principle * (pow((1 + rate / 100), time))
		print("Compound interest is", CI)


	compound_interest(10000, 10.25, 5)


# <h2> PYTHON Quiz  											        




Question 1:													
What is a correct syntax to output "Hello World" in Python?

	print("Hello World")    Your answer  
	p("Hello World")
	echo("Hello World");
	echo "Hello World"


Question 2:
How do you insert COMMENTS in Python code?

	#This is a comment    Your answer  
	/*This is a comment*/
	//This is a comment

Question 3:
Which one is NOT a legal variable name?

	_myvar    Your answer  
	Myvar
	my-var    Correct answer  
	my_var

Question 4:
How do you create a variable with the numeric value 5?

	Both the other answers are correct    Your answer  
	x = int(5)
	x = 5

Question 5:
What is the correct file extension for Python files?

	.py    Your answer  
	.pyth
	.pt
	.pyt

Question 6:
How do you create a variable with the floating number 2.8?

	Both the other answers are correct    Your answer  
	x = 2.8
	x = float(2.8)

Question 7:
What is the correct syntax to output the type of a variable or object in Python?

	print(type(x))    Your answer  
	print(typeof(x))
	print(typeOf(x))
	print(typeof x)

Question 8:
What is the correct way to create a function in Python?

	def myFunction():    Your answer  
	create myFunction():
	function myfunction():

Question 9:
In Python, 'Hello', is the same as "Hello"

	True    Your answer  
	False

Question 10:
What is a correct syntax to return the first character in a string?

	x = sub("Hello", 0, 1)    Your answer  
	x = "Hello".sub(0, 1)
	x = "Hello"[0]    Correct answer  

Question 11:
Which method can be used to remove any whitespace from both the beginning and the end of a string?

	trim()    Your answer  
	strip()    Correct answer  
	ptrim()
	len()

Question 12:
Which method can be used to return a string in upper case letters?

	upper()    Your answer  
	toUpperCase()
	uppercase()
	upperCase()

Question 13:
Which method can be used to replace parts of a string?

	replace()    Your answer  
	repl()
	switch()
	replaceString()

Question 14:
Which operator is used to multiply numbers?

	*    Your answer  
	#
	x
	%

Question 15:
Which operator can be used to compare two values?

	==    Your answer  
	><
	=
	<>

Question 16:
Which of these collections defines a LIST?

	["apple", "banana", "cherry"]    Your answer  
	("apple", "banana", "cherry")
	{"apple", "banana", "cherry"}
	{"name": "apple", "color": "green"}

Question 17:
Which of these collections defines a TUPLE?

	("apple", "banana", "cherry")    Your answer  
	{"name": "apple", "color": "green"}
	{"apple", "banana", "cherry"}
	["apple", "banana", "cherry"]

Question 18:
Which of these collections defines a SET?

	{"apple", "banana", "cherry"}    Your answer  
	["apple", "banana", "cherry"]
	("apple", "banana", "cherry")
	{"name": "apple", "color": "green"}

Question 19:
Which of these collections defines a DICTIONARY?

	{"name": "apple", "color": "green"}    Your answer  
	["apple", "banana", "cherry"]
	{"apple", "banana", "cherry"}
	("apple", "banana", "cherry")

Question 20:
Which collection is ordered, changeable, and allows duplicate members?

	LIST    Your answer  
	SET
	DICTIONARY
	TUPLE

Question 21:
Which collection does not allow duplicate members?

	SET    Your answer  
	LIST
	TUPLE

Question 22:
How do you start writing an if statement in Python?

	if x > y:    Your answer  
	if x > y then:
	if (x > y)

Question 23:
How do you start writing a while loop in Python?

	while x > y:    Your answer  
	x > y while {
	while (x > y)
	while x > y {

Question 24:
How do you start writing a for loop in Python?

	for x in y:    Your answer  
	for each x in y:
	for x > y:

Question 25:
Which statement is used to stop a loop?

	break    Your answer  
	return
	exit
	stop

