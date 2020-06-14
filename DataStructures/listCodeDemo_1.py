#=========================================================================
# List have the following properties:
# 1. Lists are mutable
# 2. Lists can have duplicate values
# 3. Lists can have heterogeneous values
# 4. Lists will preserve order of insertion
#=========================================================================


# Declaring an empty list array
list1 = []
list2 = list()

# initializing lists with range() method
list1 = range(1, 15, 2)
list2 = [2, 5, 8, 10, "Praveen", 8, 2.56]

# Print the length of list1 and list2
print("Length of List1 is ", len(list1))
print("Length of List2 is ", len(list2))

# if-elif-else Condition
if len(list1) == len(list2):
    print("List1 is equal to List2")
elif len(list1) > len(list2):
    print("List1 is bigger than List2")
else:
    print("List2 is bigger than List1")

# printing the list1 with while loop
print("\n printing the list1 with while loop")
i = 0
while i < len(list1):
    print("index {} and value is {} ".format(i, list1[i]))
    i = i + 1

# printing the list2 with for loop
print("\n printing the list2 with for loop")
i = 0
x = len(list2)
for i in range(x):
    print("index {} and value is {} ".format(i, list2[i]))