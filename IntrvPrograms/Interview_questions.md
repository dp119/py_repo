

# <h1> Basic Programs

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




| PYTHON Quiz  											        |
| Score: 22 of 25												|
| ------------------------------------------------------------- |



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

