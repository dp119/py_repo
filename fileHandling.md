# <h5> <h2> fileHandling

# <h5> file.txt contains below content
"Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!"


# <h5> <h4> four different methods (modes) for opening a file

	"r" - Read - Default value. Opens a file for reading, error if the file does not exist

	"a" - Append - Opens a file for appending, creates the file if it does not exist

	"w" - Write - Opens a file for writing, creates the file if it does not exist

	"x" - Create - Creates the specified file, returns an error if the file exists


# <h5> <h4> addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


# <h5> r and t modes are default, so below two declarations are same

f = open("file.txt") 
f = open("file.txt", rt)


# <h5> open() function returns a file object

f = open("file.txt")
print(f.read())
f.close()

# <h5> read method can also be used to read only part of the file

f = open("file.txt")
print(f.read(5))
f.close()
#prints "Hello"


# <h5> to read the file line by line

f = open("file.txt")
for i in f:
	print(i, end="")		#end flag to skip printing the new line
f.close()

# <h5> readline() method to read the line. It reads single line. 

f = open("file.txt")
print(f.readline())
# <h5> Prints only first line in the file


# <h5> readlines() function to print lines to a list

f = open("file.txt")
print(f.readlines())
f.close()

# <h5> ['Hello! Welcome to demofile.txt\n', 'This file is for testing purposes.\n', 'Good Luck!']





# <h5> Write to an Existing File
NOTE: write flag overwrites the file if it already exists.

f = open("file1.txt", "w")
f.write("Harry bhai is awesome")
f.close()

append to an existing file

f = open("file1.txt", "a")
f.write("Harry bhai is also short \n")
f.close()


# <h5> Create a New File. Empty file

import os
f = open("myfile.txt", "x")


# <h5> Delete a File

os.remove("myfile.txt")


# <h5> Tell() for Position of File Handle, Returns an integer

with open("myfile.txt", "r") as f:
    print(f.tell())


# <h5> Seek() Change the current file position to 4, and return the rest of the line
# <h5> The seek() method sets the current file position in a file stream.
# <h5> The seek() method also returns the new postion.

f = open("file1.txt", "r")
f.seek(4)
print(f.readline())

f = open("file1.txt", "r")
print(f.seek(4))


# <h5> Check if File exist
import os
if os.path.exists("file1.txt"):
    os.remove("file1.txt")
else:
    print("The file does not exist")


# <h5> Delete Folder
os.rmdir("myfolder")
