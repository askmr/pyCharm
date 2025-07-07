import datetime

Number = int(input("Enter the number1: \n"))

if Number <= 365:

    if Number % 7 == 1 or Number == 1:
        print("Sunday")
    elif Number % 7 == 2 or Number == 2:
        print("Monday")
    elif Number % 7 == 3 or Number == 3:
        print("Tuesday")
    elif Number % 7 == 4 or Number == 4:
        print("Wednesday")
    elif Number % 7 == 5 or Number == 5:
        print("Thursday")
    elif Number % 7 == 6 or Number == 6:
        print("Friday")
    elif Number % 7 == 0 or Number == 0:
        print("Saturday")

else:
    print("INVALID")

# if 1 < Number <= 365:
#         start_date = datetime.date(2025, 1, 1)
#         result_date = start_date + datetime.timedelta(Number - 1)
#         week_number = result_date.isocalendar()[1]
#
#         print(f"Date: {result_date.strftime('%B %d, %Y')}")
#         print(f"Week Number: {week_number}")
#
# else:
#         print("\n Please enter a number between 1 and 365 \n")
