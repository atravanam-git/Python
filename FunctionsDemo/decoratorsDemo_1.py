#==========================================================================
# input Function ==> Decorator Function ==> output function with extended functionality
# Without modifying an existing function but enhancing or extending the functionality
# Decorator helps in reducing code
#==========================================================================

def decor(greet):
    #     print("decorGreet()")
    def inner(name):
        #         print("inner()")
        if name != "Sidumungi":
            greet(name)
        else:
            print("Get Lost!!! {}".format(name))
    return inner


#=========================================================================
# @ is an Decorator Annotation used for calling the decor() function defined above
# greet() is passed as an argument to the decor() which will extend its functionality
#========================================================================="
@decor
def greet(name):
    print("Greetings!{} Good Day".format(name))


# # call greet() function which is the original function

greet("Praveen")
greet("Prashant")
greet("Sidumungi")