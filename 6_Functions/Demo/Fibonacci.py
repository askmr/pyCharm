def Fibo():
    n = int(input("Enter range: \n"))
    a = 0
    b = 1
    for i in range(1, n + 1):  # Fibonacci
        print(a, end=" ")
        a, b = b, a + b
Fibo()