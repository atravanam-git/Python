#==========================================================================# 1. Open a file in Write mode
# 2. Create a csvWriter object f
# 3. Insert rows with csvF.writerow([List]) method
#==========================================================================

import csv
with open("Actors.csv", 'w', newline='') as f:
    wObj = csv.writer(f)
    # writerow([List])
    wObj.writerow(["Roll No.", "Name", "Phone"])
    while True:
        rno = int(input("Enter roll no"))
        name = input("Enter name: ")
        ph = input("Enter phone no. ")
        # writerow([List])
        wObj.writerow([rno, name, ph])
        var = input("Do you want to enter more records (Yes/No) ").upper()

        if var == "NO":
            break
print("File Written Successfully")
"""Open a file in read mode
Create a csv.reader object
"""

with open("Actors.csv") as f:
    rObj = csv.reader(f)
    data = list(rObj)
    for row in data:
        print(row)

print("the content of the Actors.csv file is ", data)