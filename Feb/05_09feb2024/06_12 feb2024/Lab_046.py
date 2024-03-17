# Triangle program
# side1 == side2 == side3  --> equality triangle eq
# side1 == side2 or side2 == side3 or side1 == side3  ->>> isosellis trianle iso
# else -- scalene

side1 = float(input("enter the side 1\n"))
side2 = float(input("enter the side 2\n"))
side3 = float(input("enter the side 3\n"))

if side1 == side2 == side3:
    print("triangle is EQ")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("triangle is ISO")
else:
    print("It is a scalene")
