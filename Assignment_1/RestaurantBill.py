Name = input("Enter your name: \n")
Food = input("Enter food item: \n")
Price = int(input("Enter Price: \n"))
Quantity = int(input("Enter Quantity: \n"))

Bill = Price * Quantity
print("Customer:", Name, "\n"
                         "Item:", Food, "\n"
                                        "Quantity:", Quantity, "\n"
                                                               "Total Bill:", Bill)
