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