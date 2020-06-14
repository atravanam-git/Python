'''
This is called doc string
Created on May 23, 2020
@author: Admin_2
'''
#=========================================================================
# There are 3 types of methods in python
# 1. instance method - are object related methods
# 2. static method - are general utility methods
# 3. class method - are class related methods
#=========================================================================

class Student:
    # cname is a class Variable
    cname = "Python Class"

#   Constructor Method
    def __init__(self, rno, name):
        # self is an instance variable
        self.rno = rno
        self.name = name

# Instance method uses instance variable
    def display(self):
        print("*" * 25)
        print("Roll no. is ", self.rno)
        print("Student Name is ", self.name)

    @classmethod
    def getClassName(self):
        print("Class Name is ", self.cname)

    @staticmethod
    def avgMarks(marks1, marks2):
        avg = (marks1 + marks2) / 2
        print("Average Score is ", avg)


# calling the Student class methods
s = Student(10, "Durga")
s.display()
s.getClassName()
s.avgMarks(56, 87)


# Other ways of calling Student method
s = Student(11, "Praveen")
s.display()
Student.getClassName()
Student.avgMarks(85, 75)