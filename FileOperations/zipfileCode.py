#==========================================================================# 1. zipfile module is used for zipping and unzipping files
# 2. ZipFile is a class available in zipfile module
#==========================================================================

# Importing  a zipfile module and all its classess
from zipfile import*

# Create a zipfile
fW = ZipFile("Example.zip", 'w', ZIP_DEFLATED)
fW.write("abc.txt")
fW.write("Kyc.txt")
fW.write("xyz.txt")

"""
1. ZIP_STORED represents unzip operation. This is default value and optional to specify.
2. Get all file names from zip file by using namelist() method.
"""
# check if the filetype is zipfile
bln = is_zipfile("Example.zip")
if(bln):
    print("Zipfile created successfully")
else:
    print("Bad Zip FIle")
    exit

# Unzipping azip file and reading its file contents
fR = ZipFile("Example.zip", 'r')
filenames = fR.namelist()
print(filenames)
for names in filenames:
    print("File name is ", names)
    f = open(names, 'r')
    print(f.read())
    print("*", 10)