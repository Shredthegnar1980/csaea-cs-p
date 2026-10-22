#conditionals in python
#comparison operators: ==, !=,<, >, <=, >=
#logical operators: and, or, not
#control flow: if, elif, else

#Boolean refresher:
# always True or False
print(3==2)
print("Hello" == "Hi there")
print(7 != 4)
print(4 > 5)

# if
num = 12
if num == 10:
    print("your num is equal to ten")
    print(10 + num)

# if else

num = 5
if num <= 12:
    print("num is lesse than or equal to 12")
else:
    print("num is greater than 12")

# if elif else

temperature = 72
if temperature > 95:
    print(" its hot")
elif temperature >= 60:
    print("its nice")
else:
    print("its cold")


print()

x = 2
y =20

if x == y:
    print(" they are equal")
elif x >= y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("error")

# logical operators: and
age = 16
has_permission = True

if age >= 16 and has_permission:
    print("you can drive")
else:
    print("you can't drive")

# logical operators: 'or' and 'not'

day ="Sunday"

if day == "saturday" or day == "Sunday":
    print("its the weekend")
else:
    print("its a weekday")

print("--- Using 'is' and 'not' ---")

if day is not "Monday":
    print("its not monday")
else:
    print("its monday")




# challenge 1: Movie admission
age = 45
if age < 13:
    print("can watch PG and G rated movies")
elif age >= 13 and age <= 17:
    print(" can watch PG-13 rated movies")
else:
    print("can watch all rated movies")

# challenge 2: leap year
year = 2020
if year % 4 == 0 and year % 100 is not 0 or year % 400 == 0: 
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")