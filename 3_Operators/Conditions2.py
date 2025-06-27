number =int(input("Enter the number: \n"))
print("The number is=", number)

#1 Multiple of both 3, 5

if number % 3== 0 and number % 5== 0 :
    print("The number is a multiple of 3 and 5")
elif number % 3== 0 and number % 5!= 0 :
    print("The number is a multiple of 3 and NOT 5")
elif number % 5 == 0 and number % 3 != 0:
    print("The number is a multiple of 5 and NOT 3")
else:
    print("The number is NOT a multiple of 3 and 5")



