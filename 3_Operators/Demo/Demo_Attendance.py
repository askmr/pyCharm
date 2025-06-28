WorkingDays = int(input("Enter the number1: \n"))
AbsentFor = int(input("Enter the number2: \n"))
PresentFor = WorkingDays - AbsentFor
Attendance = (PresentFor / WorkingDays ) * 100

print("The Attendance % is \n", round(Attendance, 2))

if Attendance >= 75:
    print("Eligible to attend the exam")
else:
    print("NOT Eligible to attend the exam")
