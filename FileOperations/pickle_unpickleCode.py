#=========================================================================
# from test.test_decimal import file
# Pickle and Unpickle Concept: (same like Serialization and De-serialization)
# 1.Import pickle module
# 2.Use dump() method to write object to dat file
# 3.Use load() method to read object from the dat file
#========================================================================="""
# define an employee class
import pickle


class Employee:
    def __init__(self, eno, name, sal, addr):
        self.eno = eno
        self.name = name
        self.sal = sal
        self.addr = addr

    def display(self):
        print(" Employee no ", self.eno)
        print("Employee name ", self.name)
        print("Salary ", self.sal)
        print("Address ", self.addr)


# Pickling - Create a emp data file to dump the object
f = open("emp.dat", 'wb')
e1 = Employee(100, "Praveen", 10000, "Hyd")
pickle._dump(e1, f)
print("Pickling of employee object done successfully")
f.close()

# Unpickling - Read the data file using load()
f = open("emp.dat", 'rb')
obj = pickle._load(f)
print("Employee Object Contents ")
print(obj.display())