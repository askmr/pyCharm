
# i = 0
# j = 0
# n = ord('A')
#
# for i in range(1, 5):
#     for j in range(i):
#         m = chr(n)  # to store ord(n) , else ord(n) numerical value will be printed
#         print(m, end=" ")  # print m =A, BC, DEF, GHIJ,  print n = 65, 66 67, 68 69 70, 71 72 73 74,
#         n += 1
#     print()
# print("*", end=" ")

# i = 0
# j = 0
# for i in range(1, 5):
#     n = ord('A')            #This makes the alphabet reset in new line
#     for j in range(i):
#         if j <= i:
#             print(chr(n), end=" ")  # A, AB, ABC, ABCD
#             n += 1
#     print()
# print("*", end=" ")

# i = 0
# j = 0
# n = ord('c')
#
# for i in range(1, 5):
#     for j in range(i):
#         m = chr(n)  # to store ord(n) , else ord(n) numerical value will be printed
#         print(m, end=" ")  # c, de, fgh, ijkl
#         n += 1
#     print()
# print("*", end=" ")

# i = 0
# j = 0
# n = int(input("Enter range: \n"))
# for i in range(0, n+1, 1):
#     # for j in range(1, n+1): #(0,i) #*, **, *** ...
#     for j in range(i):              # j= i when u need triangle pattern, adjust range as per requirement of ASC(0,n,1) and DEC(n,0,-1)
#         if j<= n:
#             print("*", end=" ")       # * in ascending order
#     print()

# i = 1
# j = 1
# n = int(input("Enter range: \n"))     # 1 2 3 4, 1 2 3, 1 2, 1
# for i in range(n+1, 1, -1):             # same above program, but swapped range in i, changed range of j, then print j
#     for j in range(1, i):
#         if j<= n:
#             print(j, end=" ")
#     print()

# i = 1
# j = 1
# n = int(input("Enter range: \n"))       # 4 4 4 4, 3 3 3, 2 2, 1
# for i in range(n-1, 0, -1):             # same above program, but changed range in i, changed range of j, then print i
#     for j in range(0, i):
#         if j< n:
#             print(i, end=" ")
#     print()

# n = int(input("Enter range: \n"))  # star with space
# # for i in range(1, n + 1):
# #     print(" " * (n - i) + "* " * i)
#
# for i in range(0,n):
#     for k in range(0, n-i):
#         print(end=" ")
#     for j in range(0, i+1):
#         print("*", end=" ")
#     print()
