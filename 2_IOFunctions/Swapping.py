#1
x, y, z = 3, 6, 2
print(x, y, " :Before Swapping")

x = y + 0
y = x + 0
print(x, y)  # Output ended up being x = y, because value of x got updated before it was swapped to y.

#2
x, y, z = 3, 6, 2  # To reset x, y, z values that changed due to above operation

temp = x + 0
x = y + 0
y = temp + 0

print(x, y,
      " :After Swapping, using temp variable")  # Output ended up swapping of x , y because intermediate variable temp stored value of x which was used to update y

#3
x, y, z = 3, 6, 2  # To reset x, y, z values that changed due to above operation

x, y = y, x
print(x, y, " :After Swapping using assignment")  # Output ended up swapping of x , y without temp variable

#4
x, y, z = 3, 6, 2  # To reset x, y, z values that changed due to above operation

x = x + y
print(x)
y = x - y
print(y)
x = x - y
print(x)
print(x, y, " :After Swapping using Add, Sub")  # Output ended up swapping of x , y without temp variable

#5
x, y, z = 3, 6, 2  # To reset x, y, z values that changed due to above operation

x = x * y
y = x / y
x = x / y
print(x, y, " :After Swapping using Mul, Div")  # Output ended up swapping of x , y without temp variable
