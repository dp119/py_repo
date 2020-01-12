

# Seek() Change the current file position to 4, and return the rest of the line
# The seek() method sets the current file position in a file stream.
# The seek() method also returns the new postion.

import os
f = open("file.txt", "r")
f.seek(4)
print(f.readline())

f = open("file.txt", "r")
print(f.seek(4))


# Check if File exist
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("The file does not exist")


# Delete Folder
os.rmdir("myfolder")
