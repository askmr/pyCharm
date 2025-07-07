gender = input("Gender (M/F): \n")
age = float(input("Enter the age: \n"))
workdays = float(input("Enter the number of days worked: \n"))

if gender in "Mm":
    if 18 <= age < 30:
        wage = 700 * workdays
        print("The wage is: \n", wage)

    elif 30 <= age <= 40:

        wage = 800 * workdays
        print("The wage is: \n", wage)
    else:
        print("\n The age is not in limits, no wages \n")

elif gender in "Ff":
    if 18 <= age < 30:
        wage = 750 * workdays
        print("The wage is: \n", wage)

    elif 30 <= age <= 40:

        wage = 850 * workdays
        print("The wage is: \n", wage)
    else:
        print("\n The age is not in limits, no wages \n")

else:
    print("\n The Gender is not valid, no wages \n")
