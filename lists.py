##################################################
#      Declare a list
##################################################

# Construct a basic list
mylist = [1, 2, 3, 4, 5]
print(mylist) # >> [1, 2, 3, 4, 5]

# Construct an empty list
mylist = list()
print(mylist) # >> []

# Construct a list of strings
mylist = ['the', 'lazy', 'dog']
print(mylist) # >> ['the', 'lazy', 'dog']

# Get the length of a list
print(len(mylist)) # >> 3


##################################################
#      Accessing Elements by Index
##################################################

# Access the first item of a list
print(mylist[0]) # >> 'the'

# Access the last item of a list
item = mylist[-1] # >> 'dog'
print(item)

# Sequentially print items of a list
for i in range(len(mylist)):
    print(mylist[i])

# Loop over items directly
for e in mylist:
    print(e)


##################################################
#      Adding Elements to a List
##################################################

# Add an item to the end of a list
mylist.append("jumps")

# Add a collection of items to the end of a list
mylist.extend(["over", "the", "dog"])

# Insert an item at a specific index
mylist.insert(5, "lazy")


##################################################
#      Removing Elements in a list
##################################################

# Remove the last item from a list and store it's value
last_item = mylist.pop()
print(last_item)
print(mylist)

# Remove the first instance of a value in a list
mylist.remove("dog")
print(mylist)

# Remove all indexes from a list
mylist.clear()
print(mylist)


##################################################
#      Use Loops to create a list
##################################################

# Create a list with multiple of a repeating element
list_of_zeros = [0] * 5
print(list_of_zeros)

# Use a loop and range() to create a list of even numbers
list_of_evens = []
for number in range(50):
    if not number % 2:
        list_of_evens.append(number)


##################################################
#      Accessing items by value
##################################################

my_list = [8,9,4,1,2,1,6,4,5,2,3,1,0]


value = 1
# Find the number of occurances of a value within a list
value_count = my_list.count(value)
print(f'{value_count} appears {my_list.count} times')


value = 5
# Determine if an item is in a list before calling .index()
if my_list.count(value) >= 1:
    value_index = my_list.index(value)
    print(f'{value} is in {my_list} at index {value_index}')

# Alternatively you can use the 'in' keyword
if value in my_list:
    value_index = my_list.index(value)
    print(f'{value} is in {my_list} at index {value_index}')


# Sort the items of a list in-place
mylist.sort()
print(mylist)

# Create a sorted list of elements and iterate over the result
for e in sorted(mylist):
    print e


##################################################
#      Create a new list from an existing list
##################################################

my_list = [0,1,2,3,4,5]


# Create a shallow copy of a list
new_list = mylist.copy()

# Create a new list from the partition of another
new_list = my_list[0:3]
print(new_list)

# Create a new list from every 2nd element of an existing list
new_list = my_list[::2]
print(new_list)

# Defining a partition of a list
a = my_list[1::2]
print(new_list)

# Create a reversed copy of a list
new_list = mylist[::-1]
print(new_list)


##################################################
#      Generate a list with List Comprehension
##################################################

# A Simple List Comprehension
my_list = [x for x in range(10)]
print(my_list)

# Create a list of squares with list comprehension
digits_squared = [n*n for n in my_list]
print(listofdigits)
print(digits_sq)

# Create a list of even elements with list comprehension
evens = [x*2 for x in range(50)]
print(evens)

# Use an if statement in List Comprehension to find even squares
even_squares = [n for n in digits_squared if not n % 2]
print(evens)


##################################################
# More Examples
##################################################

li = [1,2,3]; li[len(li):] = [4]       #>> 1, 2, 3, 4
li = [1,2,3]; li[len(li):] = [4, 5, 6] #>> 1, 2, 3, 4, 5, 6

li = [1,2,3]; li.insert(0, 9)    #[1,2,3]>> 9, 1, 2, 3
li = [1,2,3]; li.insert(3, 9)    #[1,2,3]>> 1, 2, 3, 9
li = [1,2,3]; li.insert(-1, 9)   #[1,2,3]>> 1, 2, 9, 3
li = [1,2,3]; li.insert(-2, 9)   #[1,2,3]>> 1, 9, 2, 3

li = [1,2,3]; li.append(9)       #[1,2,3]>> 1, 2, 3, 9

li = [1,2,3]; li.extend([4,5,6]) #[1,2,3]>> 1, 2, 3, 4, 5, 6


##################################################


##################################################
# Exersizes
##################################################

# 1. Find all words that begin with a and end with y
words = ['any', 'albany', 'apple', 'world', 'hello', '']





# 2. Categorize all the indexes in an array as Even or Odd based on their index





# 3. Create a 3 Dimensional Array with each innermost list being numbers 0, 1, 2, 3, 4, 5





# 4. Flatten a 2d matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]





# 5. Find the longest chain of repeating numbers in the given list.
numbers = [4,3,2,1,1,0,1,1,1,1,1,8,9,4,1,2,1,6,4,4,4,4,4,5,2,3,1,0]





##################################################
# Solutions
##################################################

# Find all words that begin with a and end with y
words = ['any', 'albany', 'apple', 'world', 'hello', '']
valid_strings = []
for word in words:
    if len(word) <= 1:
        continue
    if word[0] != 'a':
        continue
    if word[-1] != 'y':
        continue
    valid_strings.append(string)
print(valid_strings)

# Comparison with List Comprhension
valid_words = [word for word in words
    if len(word) >= 2
    if word.startswith('a')
    if word.endswith('y')]
print(valid_words)


# Categorize all the indexes in an array as Even or Odd based on their index
categories = []
for n in range(100):
    if n % 2 == 0:
        categories.append("Even")
    else:
        categories.append("Odd")
print(categories)

# Categorization with List Comprehension
categories = ['Even' if n % 2 == 0 else 'Odd' for n in range(10)]
print(categories)


# Create a 3 Dimensional Array
mylist = []
for _ in range(5):
    temp1 = []
    for _ in range(5):
        temp2 = []
        for num in range(5):
            temp2.append(num)
        temp1.append(temp2)
    mylist.append(temp1)

# Create a 3d array with List Comprehension
mylist = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]


# Flatten a 2d matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)
