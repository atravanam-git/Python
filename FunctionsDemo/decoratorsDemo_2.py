#==========================================================================
# The main objective of decorator functions is
#  1. extend the functionality of existing functions and
#  2. retaining the original code of function.
# In python we have:
# 1. Function decorators
# 2. Class decorators
# define a Student function with inner function to define grades of the students
#=========================================================================

def student(funct):
    def studentGrade(rno, name, marks):
        if marks > 90:
            funct(rno, name, marks)
            print("Student grade is A+ ")
        elif marks > 70:
            funct(rno, name, marks)
            print("Student grade is A- ")
        elif marks > 60:
            funct(rno, name, marks)
            print("Student grade is B")
        else:
            funct(rno, name, marks)
            print("Student grade is Fail")
    return studentGrade


# this function displays details of student and marks

@student
def displayStudent(rno, name, marks):
    print("Roll No.is", rno)
    print("Name is ", name)
    print("Marks Scored is ", marks)


# calling the original function - dsiplayStudent
displayStudent(10, "Praveen", 75)
displayStudent(10, "Praveen", 75)
displayStudent(10, "Praveen", 75)
displayStudent(10, "Praveen", 75)