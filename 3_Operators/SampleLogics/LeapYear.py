Number = input("Print a 4 digit number: \n")

if len(Number) == 4 and Number.isdigit():
    Year = int(Number)
    if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
        print("The year is a leap year")
    else:
        print("The year is NOT a leap year")
else:
    print("Invalid entry")
