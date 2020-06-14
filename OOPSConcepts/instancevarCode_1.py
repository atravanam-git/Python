#==========================================================================# What is instance variable:
# ---------------------------------
# 1. Instance variable are object related variable
# 2. Separate copies will be created for each instance variables
#
# Where to use instance variable:
# ---------------------------------
# 1. Inside constructor __init()__
# 2. Inside instance method
# 3. From outside class using object reference variable
#==========================================================================

class Students:
    def __init__(self, rno, name):
        self.rno = rno
        self.name = name

    def info(self):
        self.course = "Python"


s = Students(100, "Praveen")
s.info()
s.marks = 85
print("No of instance variables for S is\n ", s.__dict__)

s1 = Students(200, "Durga")
s1.grade = "A+"
print("No of instance variables for S1 is\n ", s1.__dict__)
