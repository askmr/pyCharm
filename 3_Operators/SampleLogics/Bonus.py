Salary = int(input("Enter Salary: \n"))

Service = int(input("Enter the years of service: \n"))
if Service > 10:
    Bonus = Salary * 10 / 100
    print("new Salary=", Salary + Bonus)
elif 6<= Service <= 10:
    Bonus = Salary * 8 / 100
    print("new Salary=", Salary + Bonus)
elif Service < 6:
    Bonus = Salary * 5 / 100
    print("new Salary=", Salary + Bonus)
else:
    print("Service Invalid")
