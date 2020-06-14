"""
#==========================================================================
Syntax for the following functions
# 1. Lambda input arguments: expression
# 2. filter(function, Sequence) -
#    2.1 Sequence can be list,set, tuples etc.
#    2.2 function always checks for boolean (True/False)
#    2.3 Filter() always returns filter object
# 3. map(function, sequence)
#    3.1 Sequence can be list,set, tuples etc.
#    3.2 function always does some operation
# 4. map(function, sequence)
#    4.1 reduce() function present in functools module and we should import statement.
#    4.2 Sequence can be list,set, tuples etc.
#    4.3 function always does some operation
#=========================================================================="""

# declaring an empty list
from _functools import reduce
listF = list()
listA = list()

listA = list(range(2, 10, 1))
print("ListA: ", listA)

# declaring a Lambda function 3x+1
lambda x: x * 2

# usage of lambda functions in filter()
print("return type of filter() is ", type(filter(lambda x: x % 2 != 0, listA)))
listF = list(filter(lambda x: x % 2 != 0, listA))
print("List of odd numbers listF: ", listF)

# usage of lambda functions in map()
print("return type of map() is: ", type(map(lambda x: x * 2, listA)))
listF = list(map(lambda x: x * 2, listA))
print("ListF with double of original listA : ", listF)

# usage of lambda functions in reduce()
val = reduce((lambda x, y: x * y), listA)
print("reduced() value: ", val)