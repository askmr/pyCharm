def fun(*tup):
    s = 0
    for i in tup:  # Here 'tup' behaves like a tuple
        s += 1
    print(s)


fun(1, 2, 3)
fun(1, 2, 3, 4, 5)
