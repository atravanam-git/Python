#==========================================================================
# This code will demonstrate the following:
# 1. Adding of values to list
# 2. Removing and Popping of values from the list
# 3. Sorting of the list in ascending and descending
# 4. Merging of two lists
#==========================================================================

# Declaring an empty list
listA = []
listB = list()

# Adding values to the List using list()
listA = list(range(25, 35, 2))
listB = list(range(1, 5))

# Printing the list data set
print("Original ListA values ", listA)
print("Original ListB values ", listB)
print("\n")

# Adding values to the List using append()
listA.append(5)
listA.append("IT")
listA.append("Praveen")
listA.append(10000)
listA.append("Employee")
listA.append("Grade A")
listB.append("Naveen")
listB.append("Raju")
listA.insert(0, 155.55)


# Removing values from list
listA.pop(2)
listA.pop
listB.pop(4)
listB.remove("Raju")
listB.pop(2)

# traversing the list with while loop and in operator
length = 0
while length < len(listA):
    print("Values of listA ", listA[length])
    length = length + 1
print("\n")
# traversing the list with for loop and range method
i = 0
x = len(listB)
for i in range(x):
    print("Values of ListB ", listB[i])

# extend() to merge listB into listA
listA.extend(listB)
print("Mergged list values are: ", listA)