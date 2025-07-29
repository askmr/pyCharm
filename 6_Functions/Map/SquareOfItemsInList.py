lst = ['1', '2', '3', '4', '5']
lst2 = list(map(int, lst))
print(lst2)


def square(n):  #Using user def function
    return n * n

sqr= lambda n: n*n  #Using lambda function

lst3 = list(map(square, lst2))
print(lst3)

lst4 = list(map(sqr , lst2))
print(lst4)
