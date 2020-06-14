# opening a file in write mode and write onto it
from _io import open
with open("Abc.txt", 'w') as f:
    f.write("Hello World, this is my first python file")
    print("if file is closed? ", f.closed)
    print("if file is readable? ", f.readable())
    print("if file is writable? ", f.writable())
print("if file is closed? ", f.closed)

# Open a file in read mode and print
with open("Abc.txt", "r") as f1:
    print("Mode of file: ", f1.mode)
    strg = f1.readlines()
print("File Abc.txt contents are: ", strg)


# Write a List into the file and then read it (w+) mode
listA = ["Praveen", "Durga", "Python"]
stringS = "I will succeed"
with open("Kyc.txt", 'w+') as f2:
    if(f2.writable()):
        f2.write(stringS)
        f2.writelines(listA)
        data = f2.readlines()
        print("Data: ", data)
    else:
        print("File not writable")

# read a file and then write (r+) mode
with open("Abc.txt", 'r+') as f4:
    strg = f4.read()
    print("Contents of Abc.txt file is: ", strg)
    f4.write("ANonymous names into this world")

f4 = open("Abc.txt")
strg = f4.read()
print("New contents of Abc.txt file is: ", strg)
