# declare a list
listA = [10, 20, 30, 40, 50]
listB = [10, 10.55, 20.55, "Praveen", "Naveen", 20.55]
listC = []
# Sorting the list
listA = sorted(listA, key=None, reverse=True)

# Cloning a List object by SLice Operator
listC = listA[:]
listC[2] = "new_value"
print("Cloned by : Operator - listC values are: ", listC)
print("ListA values ar not altered: ", listA)

# Cloning a list by Copy() function
listC.clear()
listC = listB.copy()
print("Cloned by copy function - listC values are: ", listC)
listC.pop()
listC.pop()
listC.pop()
print("listC values after popping are: ", listC)
print("Original listB values are still persistent: ", listB)

# Mathematical Operations *, **, +, Min, Max
minValue = min(listA)
print("Minimum value of listA: ", minValue)
maxValue = max(listA)
print("Maximum value of listA: ", maxValue)

# COncatenation operator on List objects
concatValue = []
concatValue = listA + listB
print("Concatenation of listA and listB is: ", concatValue)