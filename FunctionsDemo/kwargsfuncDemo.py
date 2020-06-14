
# defining a function
# ** is interpreted as dictionary object"""

def display(**kwargs):
    print("** keyword arguments function")
    for k, v in kwargs.items():
        print(k, "\t", v)


# Calling display() function
display(name="Praveen", age=25, dept="IT")