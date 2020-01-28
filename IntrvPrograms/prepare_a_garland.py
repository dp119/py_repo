# Mary does not want 2 flowers of the same colour together in the while preparing the garland.
# If one of the boxes becomes empty, she would add the remaining flowers from the other box to the end of the garland.
# Help Mary prepare the garland.


# print("Enter the string variety for box a")
# a = input()

# print("Enter the string variety for box b")
# b = input()

a = "abcdef"
b = "wxyzpqrst"

a_len = len(a)
b_len = len(b)


l_a = list(a)
l_b = list(b)

if a_len > b_len:
    diff = a_len - b_len
    while diff >= 1:
        # print("a")
        l_b.append("")
        diff = diff - 1

    out_string = ""

    for i in range(len(l_a)):
        out_string = out_string + l_a[i] + l_b[i]


else:
    diff = b_len - a_len
    while diff >= 1:
        # print("a")
        l_a.append("")
        diff = diff - 1

    out_string = ""

    for i in range(len(l_a)):
        out_string = out_string + l_a[i] + l_b[i]

print(out_string)
