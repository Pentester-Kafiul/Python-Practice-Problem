#Problem 1: Area of a Rectangle

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width

print("Area of rectangle:", area)

#Problem 2: Area of a Triangle 

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height

print("Area of triangle:", area)

#Problem 3: Area and Circumference of a Circle 

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("Area of circle:", round(area, 2))
print("Circumference of circle:", round(circumference, 2))

# Problem 4: Perimeter of a Square 

side = float(input("Enter the side length of the square: "))
perimeter = 4 * side

print("Perimeter of square:", perimeter)
