#count of odd numbers in range

#method 1
lst5=[i for i in range(1,100) if i%2==1]
# print(lst5)
count1 = len(lst5)
# print(count)

#method 2
count2=len([i for i in range(1,100) if i%2==1])
# print(count)

#multiples of 7 in range
lst1=len([i for i in range (100, 200) if i%7==0])
print(lst1)

lst2=[i for i in range(1, 300) if i%3==0 and i%11==0]
print(len(lst2))



