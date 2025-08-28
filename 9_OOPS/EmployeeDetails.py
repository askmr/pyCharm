#using get data and put data, runtime, and dynamic (commented)

class Employee:
    def __init__(self):
        self.empName = None
        self.empID = None

    # def getData(self):
    def getData(self, eID, eName):

        # self.empID=input("\n Enter employee ID: \n")
        # self.empName=input("\n Enter employee name: \n")
        self.empID=eID
        self.empName=eName
    def putData(self):
        print("\n EmpID= ", self.empID)
        print("\n EmpName= ", self.empName)

Emp1=Employee()
# Emp1.getData()
Emp1.getData(47, 'Athul')
Emp1.putData()

#using parametrized constructor

class Employee:
    def __init__(self, eID, eName):
        self.empID=eID
        self.empName=eName

    def putData(self):
        print("\n EmpID= ", self.empID)
        print("\n EmpName= ", self.empName)

Emp2=Employee(23, 'Raj')
Emp2.putData()
