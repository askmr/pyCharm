# SUM OF ODD and EVEN NUMBERS

# for i in range(1, n+1, 1): #Sum of natural numbers
#     s +=i
# print(s)

# s = 0  # sum of odd numbers
# for i in range(1, n + 1):  # +1 to include n when n= odd number
#     if i % 2 == 1:
#         print(i)
#         s += i
# print("Sum is", s)

###WHILE LOOP

# i = 1
# s = 0
# while i <= 50:
#     if i % 2 == 1:     #Logic 1
#         print(i, end=" ")
#         s += i
#     i += 1
# print("\n Sum is:", s)

# i = 1
# s = 0
# while i <= 50:
#     print(i, end=" ")
#     s += i
#     i += 2              #Logic 2
# print("\n Sum is:", s)

# i = 1
# n = int(input("Enter number: \n"))  # even numbers
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1

i = 1
esum = 0
osum = 0
n = int(input("Enter number: \n"))  # Sum of Even and Odd numbers under 50
while i < n:
    if i % 2 == 0:
        # print("Even", i)
        esum += i
    else:
        # print("Odd", i)
        osum += i
    i += 1

print("Sum of even=", esum, "\nSum of odd=", osum)