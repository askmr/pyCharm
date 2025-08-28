# Act of representing essential features without including background details
# using private and public access modifiers

from EmployeeDetails import Employee

class Child:

    def accessModifiers(self):
        emp=Employee()
        emp.getData()
        emp.putData()

        print("Parent class")

# if __name__=="__main__":
#     app = Child()
#     app.accessModifiers()