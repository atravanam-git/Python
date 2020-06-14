# defining a function with var-args
# *n is interpreted as a tuple

print("function with var-args")


def calc(*n):
    addition = 0
    subtraction = 0

    for i in n:
        addition = addition + i
        subtraction = subtraction - i
    print("Addition: ", addition)
    print("Subtraction: ", subtraction)


# calling calc() function
print("\ncalc(10)")
calc(10)

print("\ncalc(5,10)")
calc(5, 10)

print("\ncalc(5,10,10)")
calc(5, 10, 10)