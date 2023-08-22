# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

# Accessing an element
item = mylist[1]
print(item)

# Slicing a list(reversing the order)
slice_list = mylist[::-1]
print(slice_list)

# iterating over a list
for fruit in mylist:
    print(fruit)

# checking if an item is in the list
if "banana" in mylist:
    print("yes")
else:
    print("no")

# length of list
length = len(mylist)
print(length)

# appending to a list(the end of the list)
mylist.append("orange")
print(mylist)

# appending to a list at a certain index
mylist.insert(1, "raspberry")
print(mylist)

# removing items(returns last item and removes)
item = mylist.pop()
print("my item is ", item)
print(mylist)

# removing a specific element(does not store)
mylist.remove("raspberry")
print(mylist)

# clearing a list
mylist2 = [1, 2, 3]
mylist2.clear()
print(mylist2)

# reversing a list
mylist.reverse()
print(mylist)

# sorting a list
mylist3 = [4, 6, 2, 8, 23, 90, -23, -3]

mylist3.sort()
print(mylist3)

# creating and sorting a new list (does not alter original list)
mylist4 = [4, 2, -1, 5]

new_list = sorted(mylist4)
print(mylist4)
print(new_list)

# create a new list with the same element multiple times
mylist5 = [0] * 5
print(mylist5)

# combining lists
big_list = mylist3 + mylist + mylist5
print(big_list)

# slicing a list
mylist = [1, 2, 3, 4, 5, 6]
a = mylist[3:6]
print(a)

# copying lists
fruits = ["banana", "cherry", "apple"]

fruits_cpy = fruits.copy()
# fruits_cpy = list(fruits)
# fruits_cpy = fruits[:]
fruits_cpy.append("Orange")

print(fruits_cpy)
print(fruits)

# list comprehension (making a new list from existing in one line)
numbers = [1, 2, 3, 4, 5, 6]

squared = [i*i for i in numbers]

print(numbers)
print(squared)
