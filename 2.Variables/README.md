## Python 🐍: Comments, Variables, Types

### Comments

Comments are notes left by programmers to help further editors of the code (including the orginal author) understand the purpose of the program.

Comments begin with a hash mark (`#`) and the interrupter (Python) ignores them.

### Variables

Variables are boxes in a computer's memory. When you name a variable and give it a value you are assigning that information into a "box" in the computers memory. Variables allow a programmer to remember some information for later use.

For example, imagine you are creating a high score game. If you wanted to display the high score to the screen you would create a variable to hold that information.

### Built-in Types

Python has built-in data types that instruct the interrupter how the program intends to use that information.

| Name           | Types                              |
| -------------- | ---------------------------------- |
| Text Types     | `str`                              |
| Numeric Types  | `int`, `float`, `complex`          |
| Sequence Types | `list`, `tuple`, `range`           |
| Mapping Types  | `dict`                             |
| Set Types      | `set`, `frozenset`                 |
| Boolean Type   | `bool`                             |
| Binary Type    | `bytes`, `bytearray`, `memoryview` |

### Text Types

In python a string is a sequence of charcter data. We can create strings by enclosing them in single or double quotes. If you need to make a multiple line string you can use three single or double quotes.

```python
first_name = 'my first name'
last_name = "my last name"
multi_line = """This is line one
Line 2
Line 3
"""
```

Like many other programming languages strings in Python are a list of bytes representing unicode characters. This means a programmer can access elements within the string using square brackets `[]`. It is important to remember indexs of lists start at `0` instead of `1`.

### Common String operations

When building programs you will find yourself need to modify strings, compare them, retrieve certain substrings out of a larger string, format them and many more. It is important to understand how to effective work with strings

#### Retrieve a character at a certain index.

Since strings are arrays you can pass in the index of the character you want and it will give you that character. You can use postive numbers to find starting from left to right or negative numbers to find starting right to left.

```python
name = 'name'
n = name[0] # 'n'
a = name[1] # 'a'
e = name[-1] # 'e'
```

#### Length of a string

Python has a `len` function that will compute the number of characters in your string

```python
name = 'name'
print(len(name)) # 4
```

#### Create a substring

At times you may have a large string and you only want a piece of it. In that case, a programmer can specify a range and python will return that subset.

```python
name = 'name'
me = name[2:4] # returns 'me'
nam = name[:3] # starts at 0 ends at 3 (not inclusive) returns 'nam'
ame = name[1:] # starts at 1 and goes until the end return 'ame'
ae = name[1::2] # starts at 1 goes to the end and skips every 2nd character return 'ae'
am = name[-3:-1] # starts at -3 (a) and goes to -1 (e) but is not inclusive returns 'am'
```

#### Determine if a string contains a substring

In Python you can use the `in` and `not in` operators to determine if a string contains another string.

```python
hello_world = 'Hello, world!'
print('Hello' in hello_world) # True
print('Bye' in hello_world) # False
print('Bye' not in hello_world) # True
```

#### Methods

Python has built-in methods that allow a programmer to modify strings.

```python
name = 'Name'
print(name.upper()) #NAME
print(name.lower()) #name
message = ' Hello World '
print(message.strip()) # removes begging and ending whitespace returns 'Hello World'
```

#### Combining strings

In Python you can use the `+` operator to combine strings together

```python
greeting = 'Hello'
name = 'Name'
print(greeting + ' ' + name) # Hello Name
```

### Numeric

Python supports 3 types of numeric values: `int`, `float`, `complex`

#### Int

Int, or integer, is a positive or negative whole number without decimals.

```python
x = 1
y = -2
```

#### Float

Float, or floating point number, is a postive or negative number with one or more decimals. Floats can also be represented in scientific notation.

```python
x = 1.20
y = -5.7
z = 35e3
```

#### Complex

Complex numbers contain imaginary numbers, we will not discuss them here.

### Sequence Types

#### List

A list is a built-in data type that allows a programmer to work with a collection of data is sequential order.

Imagine you wanted to collected the ages of everyone in a class. You could store that in a list variable.

```python
ages = [12, 13, 11, 10]
```

A list begins with a opening bracket `[` and ends with a closing bracket `]`. Each item in a list is seperated by a comma `,`.

A list can contain any data type in Python.

```python
mixed_list = [1, False, 2.3, 'Hi']
```

You can access an element of a list by using it's index. Lists start counting at zero.

```python
my_list = [1, 2, 3, 4]
first_element = my_list[0]
second_element = my_list[1]
third_element = my_list[2]
fourth_element = my_list[3]

```

#### Tuple

A tuple is very similar to a list. It allows programmers to store multiple items in one variable. However, a tuple is unchangeable. This means you cannot change, add, or remove items after it has been created.

Tuples begins with a opening brace `(` and ends with a closing brace `)`

```python
my_tuple = ('Hello', 1, True)
```

#### Range

A range type generates a sequence of integers by defining a start and end point of a range. This is useful for looping and will be discussed later.

### Mapping Types

#### Dictonary

A dictionary is used to store key value pairs. Dictonaries do not allow for duplicate records. Dictonaries are created with an opening curly bracket `{` and a ending curly bracket `}`

```python
my_car = {
    make: "Toyota",
    model: "Tacoma",
    year: 1998
}
```

#### Set types

### Set

A set is an unordered, unindexed data type that stores multiple items in a single variable. Duplicates are not allowed in sets and cannot be changed after creation. However, you can add new items to a set after it has been created. Sets are created using a curly brackets `{}`.

```python
set1 = {"abc", 34, True, 40, "hello"}
set1.add(False) # adds False to the set
```

### Frozen Set

A frozen set is a immutable set. This means you cannot add to the set after creation.

```python
set1 = frozenset({"abc", 123})
set1.add(True) # does not work.
```

### Boolean Type

Boolean types represent `True` or `False` values and are useful when performing comparision operations.

### Binary Types

We won't be discussing binary types. There are many useful resources online to help you learn.

### Type Conversion

In python you can convert types into different types. An example is reading input from the user comes in as a `string` type. However, you can convert that into a `int` type if needed.

```python
age_str = input('How old are you? ') # age is a string
age = int(age_str) # age is a int
```

### Suggested Projects

- **Temperature Coverter** - A program that takes the outside temperature in F and converts it to C
- **Roommate Bill Calculator** - A program that splits the utility bill between roommates
