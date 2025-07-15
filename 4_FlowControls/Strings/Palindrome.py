s="malayalam"
s1="malayalaM"

print(s)
print(s1)
print(s[:])       #also s[0:9]
print(s[::-1])    #also s[-1:-10:-1]

# if s[:]==s[-1:-10:-1]:
if s1[:] == s1[-1:-10:-1]:
    print("palindrome")
else:
    print("NOT palindrome")
