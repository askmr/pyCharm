# files with built-in operations
# like sqrt, math, pi
# unlike functions which only assist in operations

# import math #1
# from math import factorial  #2
# from math import *    #3 imports all files

import math as m  # 4
from math import sqrt as s  # 5

# print(math.factorial(6))    #1
# print(factorial(5)) #2 #3
print(m.factorial(4))  # 4
print(s(4))  # 5
