# #Armstrong number
# lst = [153, 1634, 1234, 45678, 876]
# for n in lst:
#     m = n  # to compare sum with n value, but since n is updated in line 13, m is temp of n
#     s = 0  # to reset sum value for next loop
#     x = 1  # reset x
#     # print(m)
#     num = str(n)
#     mul = len(num)
#     while n > 0:
#         mod = n % 10
#         # print(x, "Mod is: ", mod)
#         s += mod ** mul
#         # print(x, "Sum is: ", s)
#         n = n // 10
#         x += 1
#     # print("Sum is: ", s)
#     if s == m:
#         print(m, "is Armstrong")
#
