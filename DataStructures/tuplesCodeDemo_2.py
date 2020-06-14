# tuple is read only version of a List object
tupleA = (2, 63, 43, 54, 22, 2)
tupleB = ('A', 'B', 'C', 'D', 'E')
tupleC = ()

# Cloning the tuple with Slice operator
# Copy function is not available for cloning
tupleC = tupleA[:]
print("tupleA copied to tupleC: ", tupleC)
print("type(tupleC) ", type(tupleC))
print("Id of tupleC: ", id(tupleC))

# Cloning the same reference variable changes the id value
tupleC = tupleB[:]
print("tupleA copied to tupleC: ", tupleC)
print("type(tupleC) ", type(tupleC))
print("Id of tupleC: ", id(tupleC))