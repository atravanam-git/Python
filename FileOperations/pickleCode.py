# Pickle and Unpickle Concept: (same like Serialization and De-serialization)
# 1.Import pickle module
# 2.Use dump() method to write object to dat file
# 3.Use load() method to read object from the dat file

import pickle
import emp
f = open("emp.dat", 'wb')
num = int(input("Enter how many records of employees? "))
for i in range(num):
    rno = input("Id No ")
    name = input("Name is ")
    sal = int(input("Salary "))
    addr = input("Address is ")
    e = emp.Employee(rno, name, sal, addr)
    pickle.dump(e, f)
print("Pickle operation success")
f.close

