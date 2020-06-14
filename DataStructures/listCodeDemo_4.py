from emp import Employee
# declare an empty list

empList = list()

# append instances of class to the empList
empList.append(Employee(100, "Praveen",  4500, "Bangalore"))
empList.append(Employee(200, "Vydehi", 5000, "Hyd"))
empList.append(Employee(300, "Naveen", 5500, "Chennai"))

# print employee list using membership operator 'in'
for i in empList:
    print("List values are ", i.eno, i.ename,  i.esal, i.eAddr)

print("*" * 25)

# print employee list using instance attributes
for i in range(len(empList)):
    print(empList[i].eno, empList[i].ename,  empList[i].esal, empList[i].eAddr)
    i = i + 1