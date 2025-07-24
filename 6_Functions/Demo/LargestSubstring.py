# def dictOfString(str):            #USING DICTIONARY
#     dct1={}
#     for i in str:
#         length= len(i)
#         dct1[i]=length
#     print(dct1)

def largString(str):  # USING LIST
    lar = len(str[0])
    for i in str:
        if len(i) > lar:
            lar = len(i)
    print(i, lar)


lst1 = input("Enter the words: \n").split()
largString(lst1)
