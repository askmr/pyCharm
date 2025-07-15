s=input("Enter the word: \n")

# to find the length of data
# n= len(s)
# print(n)

#to find count of digits in an alphanumeric data
# d=0
# for i in s:
#     if i.isdigit():
#         d+=1
# print(d)
#

#to find number of uppercase and lowercase letters
#
# u=0
# l=0
#
# for i in s:
#     if i.isupper():
#         u+=1
#     elif i.islower():
#         l+=1
#     else:
#         print(i, "is skipped")
# print(u,l)

#count of charecters, skip spaces

# c=0
# for i in s:
#     if i.isalpha():
#         c+=1
# print(c)

char= input("Enter char: \n")
c=0
for i in s:
    if i==char:
        c+=1
print(c)