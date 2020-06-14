"""tuples have the same properties like list:
#==========================================================================
# 1. They allow duplicate values
# 2. They allow heterogeneous values
# 3. They preserve insertion order
# 4. But they are IMMUTABLE
# 5. tuple objects can be used as keys in Dictionaries
#==========================================================================
"""
# Declaring empty tuples
tupleA = ()
tupleB = tuple()

# initializing the values using tuple()
tupleA = tuple(range(1, 10, 2))
tupleB = tuple(range(2, 8))

# printing complete tuple data set
print("tupleA values: ", tupleA)
print("tupleB values: ", tupleB)

# tuple' object does not support item assignment
"""tupleA[0] = 'AddnewValue'
tupleB[1] = 2"""

# Mathematical Operator * and + for tuple
tupleA = tupleA + tupleB
tupleB = 3 * tupleB

print("Concatenation Operator - tupleA + tupleB: ", tupleA)
print("Repetition Operator - tupleB * 3: ", tupleB)

# Sorting a tuple
tupleA = sorted(tupleA, key=None, reverse=False)
print("Sorted tupleA: ", tupleA)
tupleA = sorted(tupleA, key=None, reverse=True)
print("Reverse Sorted tupleA: ", tupleA)