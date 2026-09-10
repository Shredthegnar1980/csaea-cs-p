import math

#comment

# here
# is 
# a
# comment

print("hello world!")

#Variable declerations and data types:

a = 4 #integer
b = 5.5  #float
c = "CSAEA"  #string
d = False   #boolean

print(a, b, c, d)

# OPERATORS
# + - / *  % ** //
# += -= /=

e = 7 + 2
print(e)
e += 7
print(e)

# f-string, formatted strings

print(f"e is equal to {e}")

e -= 2
e+= 7

print(f"e is NOW equal to {e}")

#comparisons (booleans, which always return True or False)

# < > <= >= == !=

print(4 < 5)
print(7 == 4)
print(1 != 2)

isEqual = "yes" == "yes"
print(isEqual)

#logical operators
# in order of precedence: not and or

f = False
t = True
#predict not run
print(not f) #true
print(f and t) #false
print(f or t) #true
print(f or t and not f) #true

# Casting ()

g = int(5.5)
print(g,)

#strings

s1 = "goodnight"
s2 = " and "
s3 = "goodbye"
end = s1 + s2 + s3 # concatenation with +
end += ", cowboy."

print(end + "\n") # \n is new line

# math library


print(math.sqrt(14))
print(math.ceil(3.65))
print(math.floor(8.94))
print(math.pow(2, 4))