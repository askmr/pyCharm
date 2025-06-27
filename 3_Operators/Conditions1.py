age =int(input("Enter the number: \n"))

#1 Positive or negative
if age > 0:
    print("The number is positive")
else:
    print("The number is negative")

#2 Voter eligibility
if age >= 18:
    print("The person is eligible for voting")
else:
    print("The person is NOT eligible for voting")

#3 Odd or Even
if age % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#4 Divisible by 7
if age % 7 == 0:
    print("The number is divisible by 7")
else:
    print("The number is NOT divisible by 7")

#5 Multiple of both 3, 7

if age % 3== 0 and age % 7== 0 :
    print("The number is a multiple of 3 and 7")
else:
    print("The number is NOT a multiple of 3 and 7")

# #6 Factor of 120
# if 120 % age == 0:
#     print("The number is a factor of 120")
# else:
#     print("The number is a NOT factor of 120")

#7 Positive , negative or Zero
if age > 0:
    print("The number is positive")
elif age < 0:
    print("The number is negative")
else:
    print("The number is ZERO")




