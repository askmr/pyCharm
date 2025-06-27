# Convert data in millimeters to meter and centimeters

Distance1 = 5678

meter1 = Distance1 // 1000  # because 1 meter is 1000 mm, for conversion because data is in mm
mm1 = Distance1 % 1000
cm1 = mm1 // 10
mm1 = mm1 % 10

print("The distance is: \n", meter1, "m:", cm1, "cm:", mm1, "mm")

# Here the data is taken in run-time (dynamically)

Distance2 = int(input("Enter the distance(in mm): \n"))  # 11542

meter2 = Distance2 // 1000  # because 1 meter is 1000 mm, for conversion because data is in mm
mm2 = Distance2 % 1000
cm2 = mm2 // 10
mm2 = mm2 % 10

print("The distance is: \n", meter2, "m:", cm2, "cm:", mm2, "mm")
