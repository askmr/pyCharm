class Student:
    def __init__(self):
        self.name = ""
        self.rollno = ""

    def getData(self):
        self.name = input("\n Enter name: \n")
        self.rollno = input("\n Enter rollno: \n")

    def putData(self):
        print("\n Name = ", self.name)
        print("\n Roll Number = ", self.rollno)


class Marks(Student):
    def __init__(self):
        Student.__init__(self)
        self.total_marks = 0

    def getMarks(self):
        self.total_marks = int(input("\n Enter Marks: \n"))

    def putMarks(self):
        print("\n Total = ", self.total_marks)


class Grade(Marks):
    def __init__(self):
        Marks.__init__(self)
        self.grade = ""

    def calculateGrade(self):
        percentage = (self.total_marks / 500) * 100

        if percentage >= 95:
            self.grade = "A+"
        elif 90 <= percentage < 95:
            self.grade = "A"
        elif percentage >= 80:
            self.grade = "B"
        elif percentage >= 70:
            self.grade = "C"
        elif percentage >= 60:
            self.grade = "D"
        elif percentage >= 50:
            self.grade = "E"
        else:
            self.grade = "F"
            print("Candidate Failed")

    def displayGrade(self):
        print("\n Grade =", self.grade)

S1=Student()
S1.getData()
S1.putData()
M1=Marks()
M1.putMarks()
M1.getMarks()
G1=Grade()
G1.calculateGrade()
