"""
#==========================================================================
# 1. global vs local variables in functions
# 2. returning multiple values
# 3. positional args vs keyword args
# 4. var-args, variable length arguments
# 5. kwargs - keyword arguments
#==========================================================================
 """
# any variable defined outside the function is global
a = 10
print("Demo on global vs. Local variables")

# this function has local variable hence local values is taken


def f1():
    a = 20
    print("Prints local variable  ", a)

# this function has No local variable hence global values is taken


def f2():
    print("Prints global variable ", a)

# this function has global keyword explicitly mentioned and its value modified


def f3():
    global a
    a = 100
    print("prints modified global value ", a)


# calling functions
f1()
f2()
f3()
f2()