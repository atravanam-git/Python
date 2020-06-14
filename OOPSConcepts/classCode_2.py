"""#==========================================================================
Types of methods:
------------------
1. instance method -
    we are using at least one instance variable as argument.
     a. first arg as self.
     b. self refers to current object
     b. example is setter() and getter() methods
2. class method -
   we are using ONLY static variable and NOT instance variable.
     a. we are using decorator @classmethod
     b. first arg is always cls, cls refers to current class object.
3. static method -
   we are NOT using any instance OR static var, only local var
=========================================================================="""
import sys

class MyBank:
    bankName = "Canara Bank"
    prevBalance = 5000
#     setter() methods instead of constructors

    def setAcctNo(self, cAcct):
        self.cAcct = cAcct

    def setcustName(self, cName):
        self.cName = cName

    def setBranch(self, branch):
        self.branch = branch


#     getter() methods instead of printing with reference object
    def getAcctNo(self):
        return self.cAcct

    def getcustName(self):
        return self.cName

    def getBranch(self):
        return self.branch

    @classmethod
    def depositFunc(cls, depAmt):
        cls.depAmt = depAmt
        netBalance = float(cls.prevBalance + cls.depAmt)

        if netBalance >= 0:
            return (True, netBalance)

        else:
            return (False, netBalance)

    @classmethod
    def withdrawalFunc(cls, wthAmt):
        cls.wthAmt = wthAmt
        if cls.wthAmt < cls.prevBalance:
            netBalance = float(cls.prevBalance - cls.wthAmt)
            return (True, netBalance)
        else:
            # to avoid 'bool' is not iterable error return False,False
            return False, False

    @staticmethod
    def Display(getBranch, getAcctNo, getcustName, ttype, amt, bal):
        print("\n")
        print("*" * 25)
        print("Welcome to ", MyBank.bankName)
        print("Your Branch Name is ", getBranch)
        print("Your Account No. is ", getAcctNo)
        print("Your Name is ", getcustName)
        print("Your Previous Balance is ", MyBank.prevBalance)
#         check deposit or withdrawal
        if ttype == 'd' or ttype == 'D':
            print("{} Amount is {}".format("Deposited", amt))
            print("Your Net Balance is ", bal)
        else:
            print("{} Amount is {}".format("Withdrawn", amt))
            print("Your Net Balance is ", bal)



# create object reference variable
obj = MyBank()

# enter customer inputs
branch = input("Enter Branch Name")
obj.setBranch(branch)

cAcct = int(input("Enter Account No"))
obj.setAcctNo(cAcct)

name = input("Enter Full Name")
obj.setcustName(name)

# Enter your choice
print("Enter D/d for Deposit ")
print("Enter W/w for Withdrawal ")
t_Type = input("Enter your choice: ")

# check for Transaction type
if t_Type == 'D' or t_Type == 'd':
    depAmt = float(input("Enter the deposit amount "))
    bln, bal = obj.depositFunc(depAmt)
    if bln:
        obj.Display(obj.getBranch(), obj.getAcctNo(),
                    obj.getcustName(), t_Type, depAmt, bal)
    else:
        print("Transaction Failed")
elif t_Type == 'W' or t_Type == 'w':
    wthAmt = float(input("Enter the Withdrawal amount "))
    bln, bal = obj.withdrawalFunc(wthAmt)
    if bln:
        obj.Display(obj.getBranch(), obj.getAcctNo(),
                    obj.getcustName(), t_Type, wthAmt, bal)
    else:
        print("Insufficient Balance - Transaction Failed", bal)
else:
    print("Invalid Entry")
    sys.exit()