def starPattern(x):
    if x == 0:
        return []
    star = starPattern(x - 1)
    star.append("*" * x)
    return star


rows = int(input("Enter rows: \n"))
for i in starPattern(rows):
    print(i)
