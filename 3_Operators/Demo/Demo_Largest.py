N1 = int(input("Enter the number1: \n"))
N2 = int(input("Enter the number2: \n"))
N3 = int(input("Enter the number3: \n"))

# 1 If-Else for largest

# if N1 >= N2 and N1 >= N3:
#     print("The number1 is Largest")
# elif N2 >= N1 and N2 >= N3:
#     print("The number2 is Largest")
# else:
#     print("The number3 is Largest")

# 2 If-Else for smallest

# if N1 <= N2 and N1 <= N3:
#     print("The number1 is Smallest")
# elif N2 <= N1 and N2 <= N3:
#     print("The number2 is Smallest")
# else:
#     print("The number3 is Smallest")

# Nested IF
# if N1>= N2:
#     if N1>=N3:
#         print("N1 is largest")
#     else:
#         print("N3 is largest")
# else:
#     if N2>=N3:
#         print("N2 is largest")
#     else:
#         print("N3 is largest")

if N1 > N2 and N1 > N3:
    if N2 > N3:
        print("N2 is Second largest")
    else:
        print("N3 is Second largest")
elif N1 < N2 and N1 < N3:
    if N2 < N3:
        print("N2 is Second largest")
    else:
        print("N3 is Second largest")
else:
    print("N1 is second largest")
