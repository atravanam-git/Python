# input() method
S1 = input("Enter String-1")
S2 = input("Enter String-2")

# strip() method
S1 = S1.strip()
S2 = S2.strip()

# for loop with in Operator
i = 0
for x in S1:
    print("The character {} is at index {}".format(x, i))
    i = i + 1

# for loop with range method
for i in range(len(S2)):
    print("String S is ", i)

# len() & upper() methods
print("The trimmed string-1 is ", S1.upper())
print("The length of string-1 is ", len(S1))

print("The trimmed string-2 is ", S2.upper())
print("The length of string-2 is ", len(S2))

# if-elif-else Conditional Operator
if S1 == S2:
    print("String-1 & String-2 are same length")
elif S1 < S2:
    print("String-1 is less than String-2")
else:
    print("String-2 is greater than String-1")

# replace() method
S1 = S1 + " " + S2.replace(S2, "Atravanam")
print("The replaced name is ", S1)