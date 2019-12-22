###############
<h1> Print string in reverse
###############

# With String Slicing
txt = "Hello World"[::-1]
print(txt)


# With For loop
txt = "Hello World"
revStr = ""
for i in txt:
    revStr = i + revStr

print(revStr)


# with reverse() function
txt = "Hello World"
revStr1 = reversed(txt)
print(''.join(revStr1))

###############
<h1> Print List in reverse
###############


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


###############
<h1> find factorial
###############

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



###############
#python program to find simple interest
###############

print("Enter the principal amount:")
p = int(input())

print("Enter the tenure:")
t = int(input())

print("Enter the rate of interest:")
r = int(input())

SI = int((p * t * r) / 100)

print("Simple Interest is {}".format(SI))


#python program to find compound interest

def compound_interest(principle, rate, time):

    CI = principle * (pow((1 + rate / 100), time))
    print("Compound interest is", CI)


compound_interest(10000, 10.25, 5)

