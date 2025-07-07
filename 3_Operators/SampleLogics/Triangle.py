import math

Angle1 = int(input("Enter Angle1 of the triangle(should be 90 if right angled): \n"))
Angle2 = int(input("Enter Angle2 of the triangle: \n"))
Angle3 = int(input("Enter Angle3 of the triangle: \n"))

if Angle1 + Angle2 + Angle3 == 180:
    largest_angle = max(Angle1, Angle2, Angle3)
    print("The largest angle is: \n", largest_angle)

    print("\n If the triangle has 2 equal sides, enter in Base1 and Base2 \n")

    Base1 = int(input("Enter Base of the triangle: \n"))
    Base2 = int(input("Enter Height of the triangle: \n"))
    Base3 = int(input("Enter Hypotenuse of the triangle: \n"))

    if Base1 == Base2 == Base3:
        print("The triangle is an equilateral triangle")
    elif Base1 == Base2 and Angle1 == 90:
        Angle1_rad = math.radians(largest_angle)
        Base3 = math.sqrt(Base1 ** 2 + Base2 ** 2 - 2 * Base1 * Base2 * math.cos(Angle1_rad))
        print("The Hypotenuse = \n", Base3)
        print("The triangle is a ISOSCELES right triangle")

    elif Base1 != Base2 and Angle1 == 90:
        Angle1_rad = math.radians(largest_angle)
        Base3 = math.sqrt(Base1 ** 2 + Base2 ** 2 - 2 * Base1 * Base2 * math.cos(Angle1_rad))
        print("The Hypotenuse = \n", Base3)
        print("The triangle is a right angled triangle")

    elif Base1 != Base2 != Base3 and Angle1 != 90:
        print("The triangle is a scalene triangle")
        Angle1_rad = math.radians(largest_angle)
        Base3 = math.sqrt(Base1 ** 2 + Base2 ** 2 - 2 * Base1 * Base2 * math.cos(Angle1_rad))
        print("The Hypotenuse = \n", Base3)
    else:
        print("Invalid Triangle")
else:
    print("Angle sum is NOT = 180")
