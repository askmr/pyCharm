# Fibonacci using functions

def fibo(n):
    a = 0
    b = 1
    lst1 = []
    for i in range(1, n + 1):
        print(a, end=" ")
        lst1.append(a)  # append before re-assign
        a, b = b, a + b  # re-assign
    return lst1


lst = fibo(7)  # because return value is list of fibo series
print()
lst.sort(reverse=True)  # descending order
print(lst)
