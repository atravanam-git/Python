# Copying one file to another file
import os
f1 = open("Abc.txt", 'r')
print("File Abc.txt contents ", f1.read())
f2 = open("xyz.txt", 'r+')
f2.write(f1.read())
f1.close()
f2.close()
if os.path.isfile("Xyz.txt"):
    f = open("xyz.txt")
    print("File xyz.txt exists")
    print("File xyz.txt contents ", f.read())