## Python 🐍: Functions

### Functions

Functions allow us to name a block of code and then reuse it later by using the name. You can pass data, known as parameters, into a function. Functions can return data as a result.

There are two steps in order to define your own functions.

1. Define the function. Think of this as teaching the computer a new word.

2. Invoke the function. Using the new word you have made.

Functions in Python are created by using the `def` keyword, any parameters (the input data), and a colon `:`.

#### Examples

Void Function (No return value)

```python
def hello_world():
    print('Hello, world!')

hello_world() # prints Hello, world! to the screen
```

Function with parameters

```python
def hello_name(name):
    print('Hello, ' + name)
hello_name('Jane') # prints Hello Jane to screen
```

Function that returns data

```python
def my_name():
    return 'Jane'
name = my_name() #assigns Jane to my name variable
```

### Suggested Projects

- **rock paper scissors** - a program that plays rock paper scissors
