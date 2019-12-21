
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

