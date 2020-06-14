# declaring an empty dictionary object
dictA = dict()
cloneA = dict()
# dict can take heterogenous & duplicate values
dictA[100] = "Durga"
dictA[200] = "Durga Prasad"
dictA[300] = "Naveen"
dictA[400] = "Durga"


# Manipulating dict values with get()
val = dictA.get(400)
if val == "Durga":
    dictA[400] = "Praveen"

# Manipulating dict values with setdefault()
dictA.setdefault(500, "Sachin")

# CLoning dict values with copy()
cloneA = dictA.copy()

# removing dict values with remove()
val = dictA.get(200)
if val != 0:
    dictA.pop(200)


# print cloned dictionary object
print(" printing cloned dictionary object")
for i in cloneA:
    print("Key is: {} and value is: {} ".format(i, cloneA[i]))

# print actual dictionary object
print(" printing cloned dictionary object")
for i in dictA:
    print("Key is: {} and value is: {} ".format(i, dictA[i]))

# Empty the cloned dictionary object
cloneA.clear()
print("CLoned dict object values are: ", cloneA)