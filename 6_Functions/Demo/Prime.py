def prime(n):
    f = 0
    for i in range(1, n + 1):
        if n % i == 0:
            f += 1
    print("No. of factors= \n", f)

    if f == 2:
        print("The given number", n, "is a prime number")


num = int(input("Enter the number: \n"))
print(prime(num))
