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


# conditionals

# if elif else

t = True
f = False

if f:
    print("reached the first condition")
elif t:
    print("reached second condition")
else:
    print("Reached else")

if 2 > 1 and 2 == 1 :
    print("reached the first condition")
elif 6 == 7 or 2 == 3:
    print("reached second condition")
elif 9 != 10:
    print("reached third condition")
else:
    print("Reached else")


# lists
# a list can hold any type, and can grow or shrink at any time

#index: 0  1   2   3   4
nums =[34, 52, 3, 64, 32]

print(nums)
print(nums[3]) #predict
print(nums[0])
print(nums[-1])
print(nums[-3])
print(nums[0] + nums[2])

nums[0] = 64
print(nums)

# list methods
# special built-in methods
words =[]

words.append("Word 1")
words.append("Word 2")
words.append("Word 3")
print(words)

words.remove("Word 1")
words.insert(0, "Word 4")
words[1] = "Word 5"
length = len(words)
print(words)
print(length)