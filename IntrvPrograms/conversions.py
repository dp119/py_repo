# <h2> Type Conversions (explicit)

# h<4> String to Int

    s = "1001"

    i = int(s)

    print(type(i))


# h<4> Int to String

    i = 1001
    s = str(i)
    print(type(s))

# h<4> String to List

    s = "youtube"
    l = list(s)
    print(l)


# h<4> Integer to List

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
