#string manipulation
# built-in methods: len(), upper(), lower(), capitalize()
#string indexing

#string formatting, string concatination

greeting = "hello"
first_name = "Ada"
last_name = "Lovelace"
print("hello" , first_name, last_name,"!")
#concatination
print("hello"+" " + first_name + " " + last_name + "!")
print(f"hello {first_name} {last_name}!")

# 0 1 2 3 4
# h e l l o

second_letter = greeting[1]
print(second_letter)

#string slicing
word= "super-cali-fragil-istic-expi-ali-docious"

print("\n the word is:", word)
print("first letter is:",word[0])
print("last letter is: ",word[-1])
print("range of letters(non-inclusive):",word[3:7])
print("first five letters:",word[:5])
print("everything after first five letters:",word[5:])
print("last seven letters",word[-7:])
print("step through every second character",word[::2])#hidden zeroes inbetween colons
print("string in reverse:",word[::-1])
last_name = "   Lovelace" #takes in account of spaces too
length = len(last_name)
print("\nlength of string:", length)

#challenge 1: favortie quote
# quote = input("Enter favorite quote:")
# print("length of quote is",len(quote),"characters long")

#challenge 2: certain letter of word
#2nd through 6th characters, 7 letter or more word
# word1 = input("type a seven letter word: ")
# print("the 2nd through 6th letters of the word are", word1[2:7])

#challenge 3: name formatter
# firstname= input("first name is: ")
# lastname= input("last name is: ")
# print(f"the last name is {lastname}, and the first name is {firstname}")

character = "DarTh vAdeR"
print("\nLowercase:", character.lower())
print("uppercase:", character.upper())
print("capitalize first letter:", character.capitalize())
print("title format:", character.title())

print()

#find and replace text
sentence = "turtles are so cool"
new_sentence = sentence.replace("are", "were")
print(sentence)
print(new_sentence)

#join and split
groceries = "milk,eggs,bread,butter,peanuts"
print("\noriginal string", groceries)

#split string into python list, based on a delimiter
items = groceries.split(",")
print(items)

#join a python list back together to a string
joined = " and ".join(items)
print(joined)
print(type(items))
print(type(joined))

#challenge 4: word mutation
#print a word backwards, in uppercase, and lowercase

challenge_word = "Potato"
print("lowercase:", challenge_word.lower())
print("uppercase:", challenge_word.upper())
print("word reversed:", challenge_word[::-1])