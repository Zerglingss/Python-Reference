# Boolean literals

**True, False, None**

A Boolean comparison, also known as a Boolean expression, is a way to compare two values and produce a result of either True or False.

Expressions make up the fundamental building blocks of code, and a surprising number of statements reduce down to a simple True or False.

Python has a few oddities in that it has three comparison values. Neither None nor False will match each other in an equals statement. However, not None is equal to False, and not False is equal to True. False is equal to 0 when comparing the values numerically, and None is not.

The following will all evaluate to not True:

A zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)

Empty sequences and collections: '', (), [], {}, set(), range(0)


# Binary Operators

**or, and, not**

'and' and 'or' are binary operators. 'and' will evaluate the statement to True if both left and right expressions are True. 'or' will evaluate to True if either the left, right, or both expressions are True.

Both 'and' and 'or' will shortcut if the value of the left expression eliminates the need to check the second. For example, in the statement 'True or func()', the function func will never be called. This behavior is sometimes used intentionally if the function has side effects.

'not' is a unary operator and will return the opposite of its operand.


# Conditionals

**if, elif, else**

Python uses the 'if' keyword to define conditional statements. These allow the program to execute different blocks of code depending on whether a condition evaluates to True or False. Additional conditions can be specified with 'elif', and a final fallback can be defined with 'else'.

x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

Indentation is critical in Python, as it defines the scope of each block.

# Loops

**while, for, pass, break, continue**

while: Executes a block of code as long as its condition is True.
for: Iterates over a sequence (like a list, string, or range).

**for... else**


The 'else' block is usally omited but is useful to know of. The else block will execute if the loop completes normally (i.e., not terminated by a 'break' statement).

**break, continue, pass**

break: Exits the loop immediately, regardless of the condition. If a for loop is followed by an else block, the block will not run if break is called.

continue: Skips the current iteration and moves to the next one.

pass: A placeholder statement that does nothing. Useful for stubbing out code blocks.

**in**

'in' can be used to check if the value of one variable exists in a list, set, or dictionary.  It is also used in a for loop to iterate over a sequence.

# Functions

**def, return, lambda, yield**

Function: A reusable block of code defined using the def keyword. Functions can take parameters, perform operations, and return results using the return statement.

Parameters: Variables listed in a function definition.

Arguments: Values passed to the function when called.

Return: A value returned to the function's caller once the function is complete.  Python functions can return almost any value, object, or even other functions. This value can be set to a variable, passed as an argument to another function, or ignored.

Yield: A special type of return statement used in generator functions to return a value and pause the function's state, allowing iteration over large datasets without consuming excessive memory.

def generate_numbers():
    for i in range(30):
        yield i

for number in generate_numbers():
    print(number)


## Lambdas

`lambda a, b, ...: (expression)`

A Lambda is a compact annonymous function defined using the lambda keyword. Often primarily for passing to other functions as arguments or, sometimes, for an operation that is repeated several times in a short block of code.  A lambda can be set to a variable.

`square = lambda x: x * x
print(square(4))  # Output: 16`


# Variable Scope

**global, nonlocal, del**



# Import

**import, from**


__import__()


## Naming Project files for Import

Filenames should be valid Python identifiers, which means they must start with a letter or underscores, followed by any combination of letters, digits, or underscores. They cannot start with a number, contain spaces, or include any special characters like @, #, or -.  A filename begining with an underscore generally indicates it is for internal module use only, and should not be imported by an external program.

To navigate to a folder within a project use a . before the folder name or for each folder name.

- Avoid naming files after functions or variables within the same file.
- Stick to lowercase and underscores in filenames.
- Don't use Python keywords or reserved words as filenames.
- Be cautious with circular imports when splitting code into multiple files.


# Class

**class**

**super()**

**is, id()**

The id() method is unique to each individual object, even objects of the same class have different ids. The keyword 'is' can be used to check if two variables refer to the same instance of an object.  For instance if an object is created and assigned to variable 'a', and 'a' is assigned to 'b,' then 'b' is assigned to 'c'; 'a' will equal 'c'.

# Getting an objects properties

**issubclass(), isinstance, type**



**len()**



# Context Management

**with, open(), as**




# Exceptions

**try, finally, except, raise, assert**


**breakpoint()**

globals()
locals()
## Types of Exceptions

*AssertionError, FileNotFoundError, ZeroDivisionError, ValueError, IndexError, KeyError, NameError*


## Custom Exceptions





# Multithreading

**await, async**



# Operations on lists

**any(), all() ,filter(), map()**





# String Formating

**format()**


## f'Strings

`f'variable: {var1}, variable: {var2}, variable: {var3}'`

If you notate a double-quoted or single-quoted string with f, the string will have special formating rules allowing you to insert variables in braces without escaping the string.  If you have quotation marks within the brackets it is best to use the type you didn't use to notate the string, either ' or ", as they cannot be escaped.

Further notation will allow you to round floating point numbers, justify (align) text, display variable names, print formatted dates, and more.

{string:10}  Right Justify a string within the next 10 characters. If the string is longer than 10 characters this will have no effect.

{string:10:10}  Right Justify and limit the length to 10 characters, any remaining characters will not be printed.

{num:10.3}  Limits the number to 3 total characters, this results in rounding for numbers smaller than 3 major digits. The number will be right justified.  For strings this will print the first 3 characters within the first 3 spaces, and replace or fill the remaining area of 10 characters with spaces.

{num:.2f}  Given a floating point value, this will round the result to 2 decimal places.

{var1:{var2}}  Another set of brackets can allow you to justify based on the value of a variable instead of a set length.

{var=} Using an = sign after a variable name will print the variable name, along with it's value.  This is very useful when debugging a program.

{day:%b %d, %y}  Given a datetime object, this format will format the date to a 3 letter month, 2 digit day, and 2 digit year.  %D can be used to print the date in MM/DD/YY format.




In Python, single and double quotes are functionally identical for defining strings. The choice between them is purely stylistic or based on avoiding escaping (e.g., using single quotes to avoid escaping double quotes inside the string).

# Iterators

**range(), reversed(), enumerate(), sorted(), zip()**

Creates an iterater from passed in arguments.

**iter(), aiter(), next(), anext()**



# Executing Strings as Code

eval(), exec(), compile()

eval evaluates an expression, exec executes a statement.



# Built-in Functions

**sum(), min(), max(), abs(), divmod(), pow(), round()**


## Number Conversions

**bin(), oct(), hex(), complex()**


# Random Numbers




**dir()**

callable()
classmethod()
object()


Returns a list of all methods and variables available to be called on an object.  This includes all built-in and inhereted methods as well.  It can be very useful when you receive an object from another program and you do not have documentation on what you can do with the object.


**setattr(), delattr(), getattr(), hasattr()**


vars()


hash()


memoryview()


property()


slice()


staticmethod()


help()