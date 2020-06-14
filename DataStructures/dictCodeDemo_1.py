"""Dictionary data type has the following features
#===============================================================================
# 1. Dict objects are key value pairs
# 2. Keys has to be always unique
# 3. Tuples can be as keys
# 4. Allows heterogeneous values
# 5. Allows duplicates in values
#==============================================================================="""
# Declare an empty dictionary object
dictStudents = dict()

# initialize dictionary values using dict[Key]=values
n = int(input("Enter how many students you want to enroll: "))
i = 1
while i <= n:
    rollNo = input("Enter Student Roll no.")
    stName = input("Enter student name")
    dictStudents[rollNo] = stName
    i = i + 1

# Printing students register by traversing the dictionary collection object
print("\nPrinting students register")
print("Roll No.\tName")
for i in dictStudents:
    print(i + "\t\t" + dictStudents[i])

# Printing the items of the dictionary as a Set data type
printSet = {}  # declaring an empty set
printSet = dictStudents.items()
print("items in dictionary are :", printSet)