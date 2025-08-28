a=int(input("Enter No1: \n"))
b=int(input("Enter No2: \n"))

try:
    div=a/b
    print(div)
except ZeroDivisionError:
    print("Do not enter Zero")
except ValueError:
    print("Enter integers only")
except:
    print("Error")
