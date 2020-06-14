#==========================================================================
# Unlike in Java in Python we can define
#  1. Define a function within a function
#  2. Function can be a parameter like in filter(),map(), reduce()
#  3. FUnction can return a function as value
#==========================================================================
# define an outer function

def outerFunction():
    print("I am in Outer function")
    # define an inner function within an outer function

    def innerFunction():
        print("I am in Inner function")
    print("Return a function as return value")
    return innerFunction


# Outer function is called which will return an inner function
# f1 will now contain the inner function
f1 = outerFunction()

# Calling an inner function outside the outer function is not possible
# but in this approach we are calling inner function from outside outer function
# you an call f1() any number of times
f1()
f1()