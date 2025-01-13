# Strings are Iterable

```python
for char in string:
    print(char)
```

# Strings support the `in` keyword

```python
if "c" in "char":
    print(True)
```

# Formating with fStrings

```python
n1 = 7; n2 = 12
string = f'{n1}. {n2}.'             #>> 7. 12.
string = f'{n1=}. {n2=}.'           #>> n1=7. n2=12.
string = f'n1 is {n1}. n2 is {n2}.' #>> n1 is 7 n2 is 12
```

```python
pi = 3.14159

print(f"result:{pi:10.3}") # >>esult:      3.14
print(f"result:{pi:10.1}") # >>esult:         3
```

```python
var = 'string'

print(f'~{var:10.2}~') # ~st        ~
print(f'~{var:10.5}~') # ~strin     ~
```

```python
width = 8
precision = 4
pow(12, 0.5)
print(f"result:{value:{width}.{precision}}") # >>result:    3.464
```

```python
import datetime

today = datetime.date.today()

day = datetime.date(year=2012, month=12, day=21)
print(f"{day:%D}")         #>> 12/21/12
print(f"{day:%b %d, %y}")  #>> Dec 21, 12
print(f"{day:%B %d, %Y}")  #>> December 21, 2012
print(f"{day:%a}")         #>> Friday
```

```python
string = 'World'
string = f'Hello {string}!' # > Hello World!

string = '\tHello\n\tWorld!\n'
# Show special characters and surrounding delimiters
print(f"{string!r}") #>> '\tHello\n\tWorld!\n'
```

# Escape and Special chars Chars

*tab* `\t`
*newline* `\n`
*backslash* `\\`
*quotations* `\', \"`
*linefeed* `\b, \r, \v, \f `

# Command Prompt Colors

```python
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
```


# Other Format Methods


## Replacement

```python
# Formating decimal numbers
n = 1
deg = 360
string = "our number is %d" % deg    # >> our number is 360
       = "our number is %5.d" % n    # >> our number is     1
       = "our number is %5.d" % deg  # >> our number is   360
       = "our number is %.5d" % deg  # >> our number is 00003
```

```python
# Formating floating point numbers
pi = 3.14159
string = "pi is %f" % pi    # >> n is 3.140000
       = "pi is %.2f" % pi  # >> n is 3.14
       = "pi is %2.f" % pi  # >> n is  3
       = "pi is %5.f" % pi  # >> n is     3 
       = "pi is %5.2f" % pi # >> n is  3.14
```

```python
# Formating multiple values at once
string = "pi is %.2f and there are %d degrees in a circle" % (var_a, var_b)
```


## String.format()

```python
var_1 = 7; var_2 = 12
string = "var1: {0} var2: {1}".format(var_1, var_2) #>> var1: 7 var2: 12
       = "var1: {} var2: {}".format(var_1, var_2)   #>> var1: 7 var2: 12
       = "var1: {1} var2: {0}".format(var_1, var_2) #>> var1: 12 var2: 7
       = "var1: {1} var2: {2}".format(var_1, var_2) #>> IndexError

string = "The sum of 1 + 2 is {}".format(sum(1, 2))
```


## String.format_map

class Default(dict):
    def __missing__(self, key):
        return key

print('{name} was born in {country}'.format_map(Default(name='Guido')))


# Single vs Double Quotations

Single quoted and double quoted strings resolve to the same value. Both statements below will produce the same result.

`string = 'Hello World'`
`string = "Hello World"`


# Multi-line Strings

```python
"""

"""
```

```python
def do_whos(self, arg):
    """List all local variables with their types and values."""

```

Multi-line strings are often used to describe a functions purpose usage.