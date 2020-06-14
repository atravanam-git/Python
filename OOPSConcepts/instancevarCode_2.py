#==========================================================================# How to delete instance variable:
# ---------------------------------
# 1. Within the class - del self.variable name
# 2. Outside the class - del Objectreference.variable name
#
# How to access instance variable:
# ---------------------------------
# 1. Inside class using self keyword
# 2. Outside class using Object reference
#==========================================================================


class xyz:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def deleteVar(self):
        del self.a
        del self.c


s = xyz()
s.e = 50
print("No of instance variables before delete is ", s.__dict__)
s.deleteVar()
del s.e
print("No of instance variables after delete is\n ", s.__dict__)

s1 = xyz()
print("No of instance variables for s1 is\n ", s1.__dict__)

print("accessing instance variable by using object reference ", s.d)
print("accessing instance variable by using object reference ",
      s1.a, s1.b, s1.c, s1.d)