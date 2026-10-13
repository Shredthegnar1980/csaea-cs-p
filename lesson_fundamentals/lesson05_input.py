import math
import random
#User input in python
#print("<prompt>")

#input always makes string
name =input("Enter your name:")
print(f"Hello {name}")

print(type(name))

age = input("Enter your age:")
print(f"your age is{age}")

print(type(age))

age_converted = int(age)
print(type(age_converted))

height = float(input("Enter your height:"))
print(f"you are are {height} meters tall")
print(height + 1)


#challenge 1: favorite color
color = input("Enter your favorite color: ")
print(f"your favorite color is: {color}")


#challenge 2: adding two numbers
number1 = input("first number is: ")
number2 = input("second number is: ")
answer = float(number1) + float(number2)
print(f"the sum is {answer}")

#Challenge 3: circle area from user input
diameter = float(input("Enter diameter here:"))
area = math.pi * (diameter/2)**2
print(f"area of the circle is {area}")

#challenge 4: custom die roll

sides = int(input("how many sides do you want: "))
roll = random.randint(1,sides)
print(f"you rolled a {roll}")