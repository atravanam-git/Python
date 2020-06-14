# declaring a dictionary object
dictA = dict()

# initialize dictionary values
dictA[100] = "Durga"
dictA[200] = "Praveen"
dictA[300] = "Reddy"
dictA[400] = "Govind"
dictA[500] = "Naveen"


print("Key\t" + "Values")
for k, v in dictA.items():
    print(k, "\t", v)