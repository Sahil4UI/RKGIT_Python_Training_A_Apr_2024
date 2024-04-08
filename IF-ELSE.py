#conditional Statements
x = int(input("Enter Side1:"))
y = int(input("Enter Side2:"))
z = int(input("Enter Side3:"))

if x+y>z and y+z>x and z+x>y:
    if x==y and y==z:
        print("Equilateral")
    elif x==y or y==z or z==x :
        print("Isoceles")
    else:
        print("Scalene")
else:
    print("Invalid Input")
