# Square
#1
# Here we enter data.
Length = 5
Perimeter = 4 * Length
print("The perimeter of the square is: \n", Perimeter)

#2
# Here we ask user to enter data.
# Then we add datatype specifically to recognize int, because user data entry by default is a String datatype
# In the below scenario, user is asked to enter data twice, one after the other. Enter 55 4 times to see the result.
Side1 = input("Please enter the measurement of one side of the square: \n")
Perimeter1 = 4 * Side1
print("The perimeter of the square is: \n", Perimeter1)
print(type(Side1))

Side2 = int(input("\n Please enter the measurement of one side of the square: \n"))
Perimeter2 = 4 * Side2
print("The perimeter of the square is: \n", Perimeter2)

Side3 = float(input("\n Please enter the measurement of one side of the square: \n"))
Perimeter3 = 4 * Side3
print("The perimeter of the square is: \n", Perimeter3)

Side4 = complex(input("\n Please enter the measurement of one side of the square: \n"))
Perimeter4 = 4 * Side4
print("The perimeter of the square is: \n", Perimeter4)
