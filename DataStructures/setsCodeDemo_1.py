"""
#==========================================================================
# 1. Set has unique values, no duplicates
# 2. Set allows heterogeneous values
# 3. Set objects are mutable
# 4. Insertion order is not preserved
# 5. Slicing and Indexing are not applicable
# 6. Set can be sorted and performed mathematical operations
#==========================================================================
"""
# Declaring an empty set in this way is treated as Dictionary object
setA = {}
setB = set()

print("type(setA) is ", type(setA))
print("type(setB) is ", type(setB))

# initializing set values with set() function
setB = set(range(1, 10, 2))
print("SetB values: ", setB)

# set are mutable and heterogeneous
setB.add("Praveen")

# adding duplicate values to set will store only unique values
setB.add(9)
setB.add("Praveen")
length = len(setB)
print("SetB values: {} and length of setB is {} ".format(setB, length))

# Cloning set object using copy() function OR slice operator
setA = set()
setA = setB.copy()
print(" Cloned setA: ", setA)

# Mathematical Operations
setB.remove("Praveen")
minValue = min(setB)
maxValue = max(setB)
sortedSet = sorted(setB, key=None, reverse=False)

print("Minimum Value is {} and Maximum Value is {}".format(minValue, maxValue))
print("Sorted Set values: ", sortedSet)