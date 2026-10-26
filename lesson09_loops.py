import time
#loops in python
#repeat a block of code 

# animals = ["horse, dog, cow, dog, pig, chicken"]

# print("\n Our animals", animals)

# for a in animals:
#     print("Im petting a", a)
#     time.sleep(0.5)

# for i in range(5):
#     print("counting", i)
# #range (start,stop,step)

for num in range(23,383,100):
    print("numbers", num)

# strings are iterable

fav_word = "cheese"
print(fav_word)
letter_list = []

for letter in fav_word:
    print(letter)
    letter_list.append(letter + "!")

print(letter_list)

print()
#challenge 1: sum calculator
total =0
for num in range(1,11):
    total += num
print(total)

# while loop: repeates while a condition is true

count = 0

while count< 5:
    print(f" on loop index #{count}")
    count += 1
    # time.sleep(0.5)

# example w/ user input
# user_input =""
# while user_input != "exit":
#     user_input = input("type exit to stop ")

#loop control statements

for i in range(1,11):

    if i == 3:
        print("skipping 3")
        continue # skips iteration
    if i == 6:
        print("breaking at 6")
        break # stops loop entirely
    if i == 9:
        pass #place holder. code in future
    print("number", i)


# challenge 2: guess till correct
# correct = 7
userinput =""
while userinput != 7:
    userinput = int(input("type number"))
