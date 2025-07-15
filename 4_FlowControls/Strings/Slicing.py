s="slicing"
print(s)
print(s[2:4]) #forwarding slicing, (excluding 4)
print(s[2:5:2]) #forwarding slicing with steps
print(s[-6:-3]) #backward slicing
print(s[-6:-3:2]) #backward slicing with steps

print(s[2:])    #to remove frontend
print(s[:2])    #to remove backend
print(s[:])     #no change
print(s[::-1])  #full reverse
print(s[::2])   #every odd string
print(s[1::2])  #every even string
print(s[-1:])   #print last letter using back slice
print(s[6:7])   #print last letter using front slice
print(s[-6:-3:1])#print by backslice
print(s[-3:-6:1]) #no result. for reverse slice, use negative steps like below example
print(s[-3:-6:-1])

a="luminar technolab"
total=len(a)
print(total)
print(a[2:5])       #to print min using forward slice
print(a[-15:-12])   #to print min using backward slice
print(a[14:17])     #to print lab using forward slice
print(a[-3:])       #to print lab using backward slice
print(a[8:12])      #to print tech using forward slice
print(a[-9:-5])     #to print tech using backward slice
print(a[:-4:-1])     #to print bal using reverse slice
print(a[-11:-14:-1])     #to print bal using reverse slice

