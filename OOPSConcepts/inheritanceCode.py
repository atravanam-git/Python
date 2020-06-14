class Emp:
    def setNo(self, empno):
        self.empno = empno

    def setName(self, eName):
        self.eName = eName

    def setRank(self, eRank):
        self.eRank = eRank

    def getNo(self):
        return self.empno

    def getName(self):
        return self.eName

    def getRank(self):
        return self.eRank


class Salary(Emp):
    def setSalary(self, basic, grade):
        self.basic = basic
        if grade == "Officer":
            sal = self.basic + 6000
            return sal
        else:
            sal = self.basic + 3000
            return sal

    def display(self):
        print("Employee No ", e.getNo())
        print("Employee Name ", e.getName())
        print("Employee Rank ", e.getRank())


e = Emp()
e.setNo(100)
e.setName("Praveen")
e.setRank("Officer")

s = Salary()
sal = s.setSalary(2500, e.getRank())
s.display()
print("Employee Salary ", sal)