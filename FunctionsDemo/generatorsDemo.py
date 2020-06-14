"""Generator function is responsible for:
1. A sequence of values.
2. Yield will return the iterator
3. always use next() function"""

def genDemo():
    no = int(input("How many numbers you want to enter "))
    i = 1
    while i <= no:
        if (i % 2) == 0:
            yield i
        i = i + 1

val = genDemo()
print("Return value type of gen function is ", type(val))


# Using for loop
for i in val:
    print("Yield values using for loop are ", i)