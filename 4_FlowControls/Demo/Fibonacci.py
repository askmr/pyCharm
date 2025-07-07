n = int(input("Enter range: \n"))

a = 0
b = 1
for i in range(1, n + 1):  # Fibonacci
    print(a, end=" ")
    a, b = b, a + b

##WHILE LOOP


# i=0
# a=0
# b=1
# while i < 10:
#     print(a, end=" ")
#     a, b = b, a+b     #Fibonacci
#     i+=1

# i=0
# a=0 #sum
# b=1
# n = int(input("Enter number: \n"))  #Fibonacci value < 10
#
# while i < n:
#     if a < 10:
#         print(a, end=" ")
#         a, b = b, a+b
#     i+=1

# n = int(input("Enter number: \n"))  #Fibonacci value < n
# i = 0
# a = 0  # sum
# b = 1
#
# while a < n:
#
#     print(a, end=" ")
#     a, b = b, a + b
#     i += 1