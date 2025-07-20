lst = input("Enter the number: \n").split()
nlst1 = []
for i in lst:
    i = int(i)
    nlst1.append(i)
print(nlst1)

for i in nlst1:
    s = 0
    for j in range(1, i + 1):
        if i % j == 0:
            s += 1
    if s == 2:
        print(i)
