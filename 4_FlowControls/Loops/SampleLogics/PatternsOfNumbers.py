
# i=0
# j=0
# for i in range(1,5): # 1234 , 4 times in new line.
#     for j in range(1,5):
#         print(j, end=" ")
#     print("*", end=" ")
#     print()

# i = 0
# j = 0
# for i in range(1, 5):  # 1111. 2222, 3333, 4444 in new line.
#     for j in range(1, 5):
#         print(i, end=" ") #change j to i, because j is incrementing when i is still 1 so, use i.s
#     print("*", end=" ")
#     print()

# i = 0
# j = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         if j <= i:
#             print(j, end=" ") #1, 12, 123, 1234
#     print("*", end=" ")
#     print()

# i = 0
# j = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         if j <= i:
#             print(i, end=" ")  # 1, 22, 333, 4444
#     print("*", end=" ")
#     print()

# i = 0
# j = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         if i <= j:
#             print(i, end=" ")  # 1111, 222, 33, 4
#     print("*", end=" ")
#     print()

# i = 0
# j = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         if i <= j:
#             print(j, end=" ")  # 1234, 234, 34, 4
#     print("*", end=" ")
#     print()

# i = 0
# j = 0
# for i in range(4, 0, -1):
#     for j in range(1, i+1):
#         # if i >= j:
#         print(j, end=" ")  # 1234, 123, 12, 1
#     print("*", end=" ")
#     print()

# i = 0
# j = 0
# n = 1
# for i in range(i+1):
#     for j in range(1, 5):
#         print(n, end=" ")  #1 1 1 1,
#         j += 1
#     print()
# print("*", end=" ")

# i = 0
# j = 0
# n = 1
# for i in range(i+1):
#     for j in range(1, 5):
#         print(n, end=" ")  #1 2 3 4
#         n += 1
#     print()
# print("*", end=" ")


# i = 0
# j = 0
# n = 1
# for i in range(1, 5):
#     for j in range(1, 5):
#         print(n, end=" ")  #1234, 5678, 9 10 11 12, 13 14 15 16,
#         n += 1
#     print()
# print("*", end=" ")

# i = 0
# j = 0
# n = 1
# for i in range(1, 5):
#     for j in range(i):
#         print(n, end=" ")  #1 23 456 789 10
#         n += 1
#     print()
# print("*", end=" ")


# i = 0
# j = 0
# n = 1
# for i in range(1, 5):
#     for j in range(i+1):
#         print(n, end=" ")  #1 2 , 3 4 5, 6 7 8 9, 10 11 12 13 14
#         n += 1
#     print()
# print("*", end=" ")