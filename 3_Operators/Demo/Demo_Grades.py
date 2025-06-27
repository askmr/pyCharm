Marks = int(input("Enter the marks: \n"))
if Marks >= 80:
    print("The Grade is A")
elif 70 <= Marks < 80:
    print("The Grade is B")
elif 60 <= Marks < 70:
    print("The Grade is C")
elif 50 <= Marks < 60:
    print("The Grade is D")
elif Marks < 50:
    print("FAILED")
else:
    print("Invalid entry")
