#lists in python
#lists store multiple values in one variable
#they are ordered, mutable(changeable), and allow dupilcation

empt_list =[]

# create lists
animals = ["dog", "cat", "turtle"]
numbers = [2,3,4,5,6]
mixed =["hello", 34, True, 9.45]

print("animals:", animals)
print("numbers:", numbers)
print("mixed:",mixed)

#print 3rd in animals, last in numbers, 1st in mixed
print(animals[2])
print(numbers[-1])
print(mixed[0])



animals[-1] = "fish"
print(animals)

# add element to end of list
animals.append("frog")

print(animals)

# insert element at specific index
animals.insert(2,"bird")
print(animals)
animals.insert(1, "camel")
print(animals)

#remove elements
animals.remove("frog")
print(animals)

# remove (pop off) last element and save it
last_animal = animals.pop()
print(last_animal)
print(animals)
print()

#challenge 1:number swap
# numbs = [1,2,3,4,5,6]
# new_num = input("new number is: ")
# numsb2 =[1,2,new_num,4,5,6]
# print(numsb2)

#challenge 2: shopping list manager
shopping =[]
shopping.append("milk")
shopping.append("eggs")
shopping.append("turkey")
shopping.insert(1,"chicken")
shopping.remove("milk")
print(shopping)

nums = [3,7,1,9,4,2,5,8,6,0]
print("numbers: ", nums)

print("length:", len(nums))
print("Min: ",min(nums))
print("max: ",max(nums))
print("sum: ",sum(nums))

nums.sort()
print(nums)

animals.sort()
print(animals)

nums.reverse()
print(nums)

if "cat" in animals:
    print("cat is in the list")
else:
    print("cat is not in the list")

#challenge 3: number stats
measurements = [1.0,1.5,2.0,2.5,3.0]
print(len(measurements))
print(min(measurements))
print(max(measurements))
print(sum(measurements))