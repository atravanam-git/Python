# defining a function with multiple retun values
def calci(a, b):
    adds = a + b
    product = a * b
    diff = a - b
    divs = a % b
    return adds, product, diff, divs


# calling the calci() function with positional args in return type
print("calling the calci() function with positional args in return type")
a, b, c, d = calci(20, 10)
print("Addition: ", a)
print("Multiplication: ", b)
print("SUbstraction: ", c)
print("Division: ", d)

# Calling the calci() function with tuple
print("Calling the calci() function with tuple")
t = tuple()
t = calci(20, 10)
for x in t:
    if t.index(x) == 0:
        print("Addition:\t", x)
    elif t.index(x) == 1:
        print("Multiplication:\t", x)
    elif t.index(x) == 2:
        print("Subtraction:\t", x)
    else:
        print("Division:\t", x)