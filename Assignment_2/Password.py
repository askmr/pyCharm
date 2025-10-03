class Password:
    def __init__(self):
        self.passcode = input("Enter the password: \n")

    def validator(self):
        lstU = []
        lstL = []
        lstD = []
        lstS = []
        if len(self.passcode) >= 8:
            for i in self.passcode:
                if i.isupper():
                    lstU.append(i)
                elif i.islower():
                    lstL.append(i)
                elif i.isdigit():
                    lstD.append(i)
                else:
                    lstS.append(i)
        else:
            print("Password length not enough")

        if len(lstU) == 0 or len(lstL) == 0 or len(lstD) == 0 or len(lstS) > 0:
            print("Invalid password \n",
                  lstU, "\n",
                  lstL, "\n",
                  lstD, "\n",
                  lstS)
        else:
            print("Valid Password")


P1 = Password()
P1.validator()
