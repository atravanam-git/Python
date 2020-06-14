myStr = "Hello World"
myStr1 = "hello universe"

slicedStr = myStr[:8]
print("SLiced String is ", slicedStr)

newslicedStr = myStr1[0:8:2]
print("New Sliced String is ", newslicedStr)

cptlize = myStr1.capitalize()
print("Capitalized String is ", cptlize)

cntVar = myStr.count('o')
print("Count of letter 'O' is ", cntVar)

newStr = myStr.replace("Hello", "Hi")
print("New String is ", newStr)

newStr = myStr + '\t' + myStr1
print("Concatenated String is ", newStr)