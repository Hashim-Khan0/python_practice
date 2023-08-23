# Tuple: ordered, immutable, allows duplicates


# creating a tuple (does not require parenthesis)
mytuple = ("Max", 28, "Boston")
print(mytuple)

# creating a tuple with one element requires (x, )
test = ("max")
print(type(test))

test = ("Max",)
print(type(test))

# using the built-in tuple to create a tuple from an iterable
mylist = ["Max", 28, "Boston"]
mytuple = tuple(mylist)
print(mytuple)

# accessing elements (0 indexed)
item = mytuple[2]
print(item)

# iterating over a tuple
for i in mytuple:
    print(i)

# checking if an element is in a tuple
if "Boston" in mytuple:
    print("yes")
else:
    print("no")

# finding length of tuple
mytuple = ('a', 'b', 'c', 'l', 'z', 'a')
print(len(mytuple))

# counting the elements
print(mytuple.count('a'))

# finding the index of an element(stops at first hit)
print(mytuple.index('a'))

# convert a tuple to a list and backwards
mylist = list(mytuple)
print(mylist)

mytuple2 = tuple(mylist)
print(mytuple2)

# slicing a tuple[start:stop:step]
mytuple = (1, 2, 3, 4, 5, 6, 7, 9, 10, 23, -90)
a = mytuple[2:8:2]
print(a)

# unpacking a tuple (elements on left side should match the tuple)
mytuple = "Max", 28, "Boston"

name, age, city = mytuple
print(name)
print(age)
print(city)

# unpacking multiple elements(the *y creates a list between [x,z], inclusive)
mytuple = (0, 1, 2, 3, 4)

x, *y, z = mytuple
print(x)
print(z)
print(y)
