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
