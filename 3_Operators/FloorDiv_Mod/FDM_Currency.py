#Currency
#amount split into notes of 500, 200, 100, 50, 20, 10, 5, 2, 1 denominations

Amount = int(input("The amount (in rupees) is : \n")) #5858
D500 = Amount // 500
D1 = Amount % 500

D200 = D1 // 200
D1 = D1 % 200

D100 = D1 // 100
D1 = D1 % 100

D50 = D1 // 50
D1 = D1 % 50

D20 = D1 // 20
D1 = D1 % 20

D10=D1//10
D1=D1%10

D5=D1//5
D1=D1%5

D2=D1//2
D1=D1%2

print("The total amount for each denomination is: \n",
      "500=",D500,
      "\n200=", D200,
      "\n100=", D100,
      "\n50=", D50,
      "\n20=", D20,
      "\n10=", D10,
      "\n5=", D5,
      "\n2=", D2,
      "\n1=", D1,
      )