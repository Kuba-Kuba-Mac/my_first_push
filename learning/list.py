languages = ['Python', 'Swift', 'C++']

# access the first element
print('languages[0] =', languages[0])

# access the third element
print('languages[2] =', languages[2])
# output from this code
# languages[0] = Python
# languages[2] = C++

# In Python, lists are:
#
# Ordered - They maintain the order of elements.
# Mutable - Items can be changed after creation.
# Allow duplicates - They can contain duplicate values.


# Python List Methods
# Python has many useful list methods that make it really easy to work with lists.
#
# Method	Description
# append()	Adds an item to the end of the list
# extend()	Adds items of lists and other iterables to the end of the list
# insert()	Inserts an item at the specified index
# remove()	Removes the specified value from the list
# pop()	Returns and removes item present at the given index
# clear()	Removes all items from the list
# index()	Returns the index of the first matched item
# count()	Returns the count of the specified item in the list
# sort()	Sorts the list in ascending/descending order
# reverse()	Reverses the item of the list
# copy()	Returns the shallow copy of the list


# task for undestable
def find_max(number):
    print(max(number))

number = [23,54,23,65,43,65]
find_max((number))


numbers = [2,4,7,9]
numbers.remove(4)
print(numbers)


cars = ['BMW', 'Mercedes', 'Tesla']
print('Total Elements:', len(cars))


fruits = ['apple', 'banana', 'orange']

# iterate through the list
for fruit in fruits:
    print(fruit)