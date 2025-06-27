#1 Membership [ in, not in ]

Value='Python'

print ('P' in Value)
print ('x' in Value)
print ('A' not in Value)

#Only for string, cannot check if Value = integer

#2 Identity [ is, is not ]

a, b, c = 10, 10, 20

print ( a is b)
print ( c is b)
print ( a is not b)
print ( c is not b)

#3 Bitwise [ & , | ]

a, b = 4, 7
print ( a & b )
print ( a | b)