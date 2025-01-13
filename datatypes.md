# Fundamental Types

**int(), float(), str(), bool()**


# Lists

list()

lists are declared using []

an empty list can be made with var = []

A single list can contain multiple data types, ints, floats, or even other lists [at once]

```python
 = ["banana", "cherry", "apple"]      # >> Declares a list of strings
 = list()                             # >> Declares an empty list
 = [1, 2, True, "string1", [1, 2, 3]] # >> Lists can contain multiple data types
 = ['a', 'b', 'c', 'd', 'e']
len(li)      # Number of elements in li ( last index + 1 )
```

# Tuples

tuple()

Tuples can also be accessed by index

Usually declared with () but it is the comma in the declaration that makes it a tuple [important note]

```python
mytuple = (1, True, 'string')       # >> Creates a tuple
mytuple = tuple(1, True, 'string')  # >> Also Creates a tuple
mytuple[0] == 1 # >> True
len(mytuple)
```

## Dictionaries and Sets

dict(), set(), frozenset()


```python
`mydict = {"name": "Max", "age": 28, "city": "Charlotte"}`
`value = mydict["name"]`

pairs = [('a', 1), ('b', 2), ('c', 3)]

my_dict = {k: v for k, v in pairs}
print(my_dict)


nums = [1, 2, 3, 4, 5, 6, 9, 9, 9]
unique_squares = {x**2 for x in nums}
print(unique_squares)


# generator
sum_of_squares = sum(x**2 for x in range(1000000))
print(sum_of_squares)

```


```python
for key in mydict:
    print(key)

for key in mydict.keys():
    print(key)

for key in mydict.keys():
    print(mydict[key])

for value in mydict.values():
    print(value)

for k, v in mydict.items():
    print(k, ":", v)
```

a tuple can be used as a dict key

```python
t1 = (1, 2, 3); t2 = (1, 2, 5); t3 = (5, 5, 5)
mydict = {t1: 1, t2: 2, t3: 3}
```


Sets contain unique elements in an *unordered* collection...

a set will contain no more than one of each value

you cannot rely on the order of a set


Valid But this will not result in the string 'Hello'
`myset = set(Hello)`


## List Partitions

list[n:m:k]
Where *n* is the *first index* of the slice, m is the *last index + 1*, *k* is the *step value,* ie. every k index after n.

list Partitions are copies of the originating list

```python
li[0]        # Value at index 0                                >> a
li[0:3]      # A copy of the first 3 elements in li            >> a, b, c
li[2:]       # A copy of li from index 2 - end                 >> c, b, e
li[:2]       # The first and second elements of list li        >> a, b
li[:]        # A copy of the full list li                      >> a, b, c...
li[::1]      # A copy of the full list li                      >> a, b, c...
li[-1]       # Value at last index. eq. mylist[len(mylist)-1]  >> e
li[::2]      # Every second element of list li                 >> a, c, e
li[::-1]     # A copy of list li in reverse order              >> e, d, c...
li[-1::-1]   # A copy of list li in reverse order              >> e, d, c...
li[0:-1]     # A copy of list li with all except the last element >> a, b, c, d
```

Add a description for this bit of unintuative behavoir.

```python
>>> li == li[:]
True
>>> li[:] == li[::-1]
False
>>> id(li) == id(li[:])
False
>>> id(li[:]) == id(li[::-1])
True
```

## Determining Type

**type(), isinstance()**


# Collections

.copy()
.deepcopy()



## Unpacking a Tuple


`name, age, city = ("Max", 27, "Charlotte")`


Just like for functions we can use the [asterisk operator] to unpack multiple values into one variable. it is important to note after this operation s2 will be a *list*

`s1, *s2, s3 = my_tuple = (1, 2, 3, 4, 5)`


# Loops and Conditionals of Collections

**in**

`for e in mylist: (print(e))`


`if 5 in mylist3: (print("5 is in the list"))`


**.add() .remove(), .discard(), .pop()**

**.intersection(), .union(), .difference(), .update(), .intersection_update(), .difference_update(), .symmetric_difference_update(), .issubset(), .issuperset(), .isdisjoint()**


```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odds = set(digits[::2])
evens = set(digits[1::2])
```

## Name

bytes(), bytearray()

