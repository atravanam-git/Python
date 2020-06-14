import os
fname = input("Enter file name ")
if os.path.isfile(fname):
    print("File exists ", fname)
    f = open(fname, 'r')
    print("Contents of file {} is: ".format(fname), f.read())
else:
    print("File does not exists")