#Problem 1: Calculate Power of a Numbers

a = float(input("Enter the base (a): "))
b = float(input("Enter the exponent (b): "))
result = a ** b

print("Result:", result)

#Problem 2: Calculate Average of 3 Numbers and 2 numbers

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
average = (x + y + z) / 3

print("Average:", average)

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
average = (x + y ) / 2

print("Average:", average)

#Problem 3: Find the Modulus

a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
remainder = a % b

print("Remainder:", remainder)

#Problem 4: Calculate Natural Logarithm

import math

x = float(input("Enter a positive number: "))
log_value = math.log(x)  # natural log

print("Natural Logarithm (ln):", log_value)
