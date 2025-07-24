# Normal: int, float, complex, boolean, string
# Collections: List, tuple, set, dictionary

# List is a collection of heterogeneous elements-different datatypes
list1 = [1, 2, 3, 4, 5, "hai", 8.6, True]
str= len(list1)
print(str)
print(list1)

#forward indexing
print(list1[5])

#reverse indexing
print(list1[-3])

print(list1[0:3])   #to print 1,3,2
print(list1[-6:-3]) #to print 3,4,5
print(list1[5:])    #to print last 3
print(list1[::-1])  #to reverse

list1[2]=100
print(list1)        #List is mutable, can be changed/updated. Tuple is immutable.
