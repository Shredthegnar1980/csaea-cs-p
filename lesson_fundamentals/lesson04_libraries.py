import math




sqrt= math.sqrt(25)
print("square root:", sqrt)

round_up = math.ceil(4.5)
print("Round up:", round_up)

round_down = math.floor(4.8)
print(f"round down: {round_down}")

exponent = math.pow(2,5)
print("exponent: ", exponent)

#constant: variable that never changes, All caps always

PI = math.pi
print(PI)

#challenge 1
diameter = 14
radius = diameter / 2
area = PI*math.pow(radius,2)
print("the area is:", area)



# PYTHON RANDOM LIBRARY



#Pyhton's library is a Psuedorandom Number Generator
#challenge 2: make psuedorandom number generator

seed = 8374.6
seed_2 = math.sqrt(seed)
seed_3 = seed_2 * 53.18
seed_4 = seed_3 % 10
seed_5 = math.ceil(seed_4)
print("seed is now:", seed_5)

#Pythons random library

import random

random_integer = random.randint(1,100)
print(random_integer)

random_float = random.random()
print(random_float)

my_list = ["taco", "burger", "pizza", "cake"]

random_selection = random.choice(my_list)
print(random_selection)

random.shuffle(my_list)
print(my_list)


#challenge 2: simulation of die rolling

die_roll_outcomes= [1,2,3,4,5,6]
die_roll = random.choice(die_roll_outcomes)
print(f"the outcome of the roll is {die_roll}")

#challenge 3: random square root
number = random.randint(1,75)
square_root = math.sqrt(number)
rounded_integer = math.ceil(square_root)
print(f" the integer is {rounded_integer}")

# challenge 4: power roll
base = [1,2,3,4,5,6]
exponent = [1,2,3,4,5,6]
base2 = random.choice(base)
exponent2 = random.choice(exponent)
answer = math.pow(base2,exponent2)
answer2 = int(answer)
print(f"the base is {base2}\nthe power is {exponent2}\nthe answer is {answer2}")