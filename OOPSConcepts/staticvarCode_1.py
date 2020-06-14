#==========================================================================# What is Static variable:
# ---------------------------
# 1. If a value of variable is NOT changing from object to object then its a #    static variable.
# 2. For all objects a single copy will be maintained at class level.
# Where to declare:
# -----------------
# 1. Directly within the class but outside the method
# 2. Inside the constructor, Instance Method by using class name
# 3. Inside the @ClassMethod by using cls variable or class name
# 4. Inside the @staticmethod by using class name
# 5. From outside the Class by using Class name
#==========================================================================


class Employee():
    # inside the class but outside method
    employerName = "Durgasoft Solution"

    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal
#     inside constructor
        Employee.batch = "Engineering"

    def display(self):
        print("#" * 25)
        print("Employer name ", self.employerName)
        print("Employee no ", self.eno)
        print("Employee name ", self.ename)
        print("Employee no ", self.esal)
        print("Batch is ", self.batch)


e1 = Employee(100, "Durga", 5000)
e1.display()

e2 = Employee(200, "Praveen", 5500)
Employee.batch = "HR"
e2.employerName = "HP India"
e2.display()

# out side of the class declaring static variable
Employee.branch = "SR Nagar"
print("Static variable are ", Employee.__dict__)