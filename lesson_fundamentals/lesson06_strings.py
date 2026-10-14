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
firstname= input("first name is: ")
lastname= input("last name is: ")
print(f"last name is {lastname}, and first name is {firstname}")