#request user to enter the lengths of all 3 sides of a triangle 
side1 = float(input("Please enter the length of the first side: "))
side2 = float(input("Please enter the length of the second side: "))
side3 = float(input("Please enter the length of the third side: "))
#calculate the area of the triangle 
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
print(f"The area of the triangle is {area}.")   
