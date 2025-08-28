s = 'pineapple'
lst8 = [i for i in s if i in ('aeiou')]
print("vowels in word:", lst8)

lst9 = ['mango', 'strawberry', 'kiwi', 'guava', 'pineapple', 'mandarine orange']
nlst9 = [i.upper() for i in lst9]
print("Upper Case list:", nlst9)

nlst10 = [i.title() for i in lst9]
print("Capital named list:", nlst10)

nlst11 = [i for i in lst9 if len([c for c in i if c in ('aeiou')]) > 2]
print("Words with vowels>2:", nlst11)
nlst15 = [i for i in lst9 if len([c for c in i if c in ('aeiou')]) == 2]
print("Words with vowels=2:", nlst15)
nlst12 = [i for i in lst9 if len(i) > 5]
print("words with len>5", nlst12)
nlst13 = [i for i in lst9 if len(i) == 5]
print("words with len>5", nlst13)
nlst14 = [len(i) for i in lst9]
print("Length of word:", nlst14)
