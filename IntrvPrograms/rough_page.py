

# Write to an Existing File
NOTE: write flag overwrites the file if it already exists.

f = open("file1.txt", "w")
f.write("Harry bhai is awesome")
f.close()

append to an existing file

f = open("file1.txt", "a")
f.write("Harry bhai is also short \n")
f.close()


# Create a New File. Empty file

import os
f = open("myfile.txt", "x")


# Delete a File

os.remove("myfile.txt")


# Tell() for Position of File Handle, Returns an integer

with open("myfile.txt", "r") as f:
    print(f.tell())


# Seek() Change the current file position to 4, and return the rest of the line
# The seek() method sets the current file position in a file stream.
# The seek() method also returns the new postion.

f = open("file1.txt", "r")
f.seek(4)
print(f.readline())

f = open("file1.txt", "r")
print(f.seek(4))


# Check if File exist
import os
if os.path.exists("file1.txt"):
    os.remove("file1.txt")
else:
    print("The file does not exist")


# Delete Folder
os.rmdir("myfolder")
