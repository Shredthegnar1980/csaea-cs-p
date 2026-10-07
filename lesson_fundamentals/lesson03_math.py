#math operators +, -, *, /, //, %, **

add = 7+2
print("Sum:", add)

subtract = 7-4
print("difference:", subtract)

multiply= 7 *3
print("product:", multiply)

float_divide = 7/2
print("Float division:", float_divide)

integer_divide = 7//2
print("integer division:", integer_divide)

mod=7%2
print("modulus:", mod)

exponent = 7**3
print("exponents:",exponent)

#PEMDAS

result1 = (2 + 3)*4
print("result 1:", result1)

result2 = 2 **3 *4
print("result 2:", result2)

result3 = 5+2**3 *(4 - 1)
print("result 3:", result3)

#challenge 1
width = 8
height = 5
area = width * height
print("area:", area)

#challenge 2
pi = 3.14
radius = 7
circle_area = pi*radius**2
print("area of circle:", circle_area)

#challenge 3
# book = 12.99 notebook = 3.50
#3 books 4 notebooks
#book: $book 
#notebook: $notebook
#total
book = 12.99
notebook = 3.50
book_cost = 3*book
notebook_cost = 4*notebook
total_cost = book_cost + notebook_cost
print(f"books: ${book_cost} \nnotebooks: ${notebook_cost} \ntotal: ${total_cost}")

#challenge 4
#57 even or odd
#bonus: conditionals

num = 57
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")