# for i in range(0, 250):
#     fc=0
#     for j in range(1, i+1):
#         if i%j==0:
#             fc=fc+1
#     if fc==2:
#         print(i, end=" ")

s = 0
for i in range(5, 51):  # perfect number
    fs = 0
    for j in range(1, i):
        if i % j == 0:
            fs = fs + j
    if fs == i:
        print(i, "is a perfect number")
    # else:
    #     print(i, "is NOT a perfect number")

