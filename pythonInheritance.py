class Student:
    def __init__(self, receivedName, receivedAge, receivedMajor, receivedId):
        self.name  = receivedName
        self._age   = receivedAge
        self.major = receivedMajor
        self._id    = receivedId
        
    def setName(self, nameParam):
        self.name  = nameParam
    
    def setAge(self, ageParam):
        self._age  = ageParam
    
    def setMajor(self, majorParam):
        self.major  = majorParam
        
    def setId(self, idParam):
        self._id  = idParam
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self._age
    
    def getMajor(self):
        return self.major
        
    def getId(self):
        return self._id
        
class EmployeeStatus(Student):
    def __init__(self, receivedName, receivedAge, receivedMajor, receivedId, currentSalary, years):
        super().__init__(receivedName, receivedAge, receivedMajor, receivedId)
        self.salary = currentSalary
        self.workingYears = years
    
    def setSalary(self, moneyAsSalary):
        self.salary = moneyAsSalary
    
    def setWorkingYears(self, years):
        self.workingYears = years
        
    def getSalary(self):
        return self.salary
        
    def getWorkingYears(self):
        return self.workingYears
    
def main():
    objectOne = EmployeeStatus("Seeam", 23, "Computer Science", 11771075, "100K", 3)
    print(objectOne.getName())
    print(objectOne.getAge())
    print(objectOne.getMajor())
    print(objectOne.getId())
    print(objectOne.getSalary())
    print(objectOne.getWorkingYears())
    
    objectOne.setAge(30)
    objectOne.setSalary("300K")
    objectOne.setWorkingYears(5)
    print()
    
    print(objectOne.getName())
    print(objectOne.getAge())
    print(objectOne.getMajor())
    print(objectOne.getId())
    print(objectOne.getSalary())
    print(objectOne.getWorkingYears())
    
if __name__ == "__main__":
    main()
    
"""
Seeam
23
Computer Science
11771075
100K
3

Seeam
30
Computer Science
11771075
300K
5
"""
