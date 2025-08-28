lst = [1, 2, 3, 4, 5]

# Create identical list
lst1 = [i for i in lst]
print(lst1)

# Create list from range with step of 130
lst2 = [i for i in range(1200, 2000, 130)]
print(lst2)

# List with square value greater than 8
lst3 = [i ** 2 for i in lst if i ** 2 > 8]
print(lst3)

# Get numbers from a sentence
# lst4 = input("Enter the sentence: \n").split()
# print(lst4)
# lst5 = [int(i) for i in lst4 if i.isdigit()]
# print(lst5)

# New list with numbers divisible by 2 and 5 in range
lst6 = [i for i in range(1, 100) if i % 2 == 0 and i % 5 == 0]
print(lst6)

# new list with double of even numbers in range
lst7=[i*2 for i in range(1,100) if i%2==0]
print(lst7)




