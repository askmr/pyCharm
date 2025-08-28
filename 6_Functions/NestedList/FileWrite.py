f1 = open('File1', 'r')
lst = f1.read()  # to copy as is
lst1 = f1.read(0).split()  # to copy without spaces, like to get count of words, occurrences etc
f3 = open('File3', 'w')  # because it is write ONLY, cannot read
f3.write("Atul")  # to add one argument as a word or a sentence
f3.writelines(["College", "\n", "School\n"])  # to add multiple words, sentences in a list format
f3.writelines(lst)  # fetch data as a list from other file
f1.close()
f3.close()

f3 = open('File3', 'r+')  # Read and Write operation
data = f3.read()
print(data)


# r - to read only
# r+- to read and write, with selective overwriting based on char position
# rb- to read in binary
# w - to write only, overwrites entirely by default
# w+- to read and write, overwrites entirely. only difference, can do read operation
# wb- to write in binary format
# a - to append data
# a+- to read and append
