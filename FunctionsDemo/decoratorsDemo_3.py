#==========================================================================# In Python, functions are first-class objects.
# This means that functions can be passed around and used as arguments,
# just like any other object (string, int, float, list, and so on).
#==========================================================================

# printing employee Department Details

def empDeptDisplay(func):
    dept_no = input("Enter Department_no")
    dept_name = input("Enter Department Name")

    def wrapper_function(*args, **kwargs):
        func(*args, **kwargs)
        print("Department Number: ", dept_no)
        print("Department Name: ", dept_name)
    return wrapper_function

# printing employee address and phone no.
def empDetails(func):
    city_branch = input("Enter Branch City")
    offcPh = input("Enter Contact Phone")

    def wrapper_function(*args, **kwargs):
        func(*args, **kwargs)
        print("Branch Office City", city_branch)
        print("Contact Phone No. ", offcPh)
    return wrapper_function

# Extend the functionality of the original employee directory
@empDetails
@empDeptDisplay
def empDirectory(**kwargs):
    print("\n")
    for k, v in kwargs.items():
        print(k, "\t", v)


empDirectory(Employee_no=24, Employee_Name="Praveen", Contractor="Yes")
empDirectory(Employee_no=25, Employee_Name="Naveen Reddy", Contractor="No")
empDirectory(Employee_no=34, Employee_Name="Gaurav", Contractor="Yes")
