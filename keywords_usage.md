```python
# Standard If
if condition_1:
  # ...
elif condition_2:
  # ...
else:
  # ...

# Single Line Ifs
if True: print(True)
elif False: print(False)
else: print(None)

# Ternary if statement
x = 1 if True else 0
print('Hello' if True else 'Goodbye')

# Empty variables will eval to False
x = ''
if x: print(True) # > False
```

```python
while condition:
  print('reapeat until condition == False')
```

```python
for i in range(10):
  print(i) #>> 0 1 2 3 4 5 6 7 8 9
```

```python
for i in range(100, 1000):
  print(i) #>> 100 101... 999
```

```python
for i in range(10, 20, 2):
  print(i) #>> 10 12 14... 18
```

```python
for i in range(10, 0, -1):
  print(i) #>> 10 9 8... 1
```

for i in range(x) will loop a constant amount of times, even if the values of x or i change throughout the loop.

```python
for element in variable:
    # ...
for element in iterator:
    # ...
```


```python
for i in range(10):
  if i % 2 == 1:
    continue
  print(i) #>> 0 2 4 6 8

for i in range(10):
  if i % 2 == 1:
    break
  print(i) #>> 0
```


```python
for i in range(10):
  print(i) #>> 0 1 2 3 4 5 6 7 8 9
else:
  print(i) #>> 9
  print('Loop Completed')

for i in range(10):
  print(i) #>> 0 1 2 3 4 5 6 7 8 9
  if i == 5:
    break
else:
  print('Loop Completed') # This won't run if the break condition above is met
```

```python
for i in range(10):
  if i % 2 == 0:
    continue
  print(i) #>> 1 3 5 7 9
else:
  print(i) #>> 9

for i in range(11):
  if i % 2 == 0:
    continue
  print(i) #>> 1 3 5 7 9
else:
  print(i) #>> 10
```

```python
for i, e in enumerate(items):
  print(i) # +1 for each item processed
  print(e) # the entry being processed
```




```python
def function():
  # ...
def function(a, b, c):
  # ...
```

```python
def function(a: str, b: int, c: int): -> str
```

```python
def foo(a, b, c):
    print(a, b, c)

foo(1, 2, 3)
foo(c=1, a=2, b=3)
foo(1, c=2, b=3)
```

```python
def defaultargs(a, b, c, d=4):
    print(a, b, c, d)

defaultargs(1, 2, 3)
defaultargs(1, 2, 3, 5)
```

```python
def varfunc(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

varfunc(1, 2, 3, 4, 5, 8, num1=9, num2=10)


def forcedkeywords(a, b, *, c, d):
    print(a, b, c, d)

forcedkeywords(1, 2, c=3, d=4)

def lastparam(*args, last):
    for arg in args:
        print(arg)
    print(last)

lastparam(1, 2, 3, last=4)
```

```python
def listfunc(a, b, c):
    print(a, b, c)

mylist = [1, 2, 3]
listfunc(*mylist)
```

```python
def dictionary_params(a, b, c):
    print(a, b, c)

params = {'a': 1, 'b': 2, 'c': 3} # Dictionary

dictionary_params(**params)
```

```python
def list_modify(li):
    li.append(4)

li = [1, 2, 3]
list_modify(this_list)
print(this_list) #>> 1, 2, 3, 4
```


```python
if x <= 0:
    raise Exception('x should be greater than 0')
```

*ZeroDivisionError*

```python
x = 0

try:
    a = 5 / x
except:
    print('Something Went Wrong')
```

```python
try:
    a = 5 / x
except Exception as e:
    print('error', e)
```

better...

```python
try:
    a = 5 / x
except Exception as e:
    print('error', e)
    raise
```

*AssertionError*

```python
assert(x > 0), 'x should be greater than 0'
```

```python
try:
    # Insert strange sort algorithim
except ValueError as e:
    #
    print('error', e)
except TypeError as e:
    #
    print('error', e)
else:
    # Try success, we found a value
finally:
    # This block will always run
```


```python
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value)
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)


try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
```



```python
number = 0

def bar():
    global number
    x = number
    number = 3
    print('number inside function ', x)

bar()
print(number)
```