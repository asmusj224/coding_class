## Python 🐍: Errors

### Errors

Errors are issues in the code. There are `3` types of Errors in Python.

- Syntax Errors
- Logical Errors
- Exceptions

#### Syntax Errors

A syntax error occurs when the programmer doesn't follow the rules of the language. The python interupter goes through the file line by line parsing and running the code. When the parser doesn't understand the line of code a syntax error is thrown. Syntax errors are fatal error meaning the program can't recover and stops executing. Common causes of syntax errors is typos, incorrect indenting, and incorrect arguments. When a syntax error is discovered a log will be shown with the number line of the issue.

// Photo here?

#### Logical Errors

A logical error is when the program is syntaxally correct but performs incorrectly. These errors require a programmer to follow their logic line by line to determine the source of the issue. Logical errors can be difficult to track down and fix. A debugger will be helpful when in this situtaion.

### Exceptions

An exception is an object with a description of what went wrong and a traceback to where the issue occured. When Python encounters an error, it stops execution and raises an exception.

There are many different types of expections in Python. Each one describes a different type of issue.

Common Exceptions

- File Not Found Error is raised when python could not find the file your program is intending to use.
- Type Error is raised whenever an operation is performed on an incorrect/unsupported object
- Value Error is raised when the type is correct but the value cannot be handled

The way for handling expections in Python is using the try, expect, else, finally clauses. You can have more than one expect clause if necessary, giving you the ability to respond to different types of exceptions in different ways.

```python
try:
    # runs first
except ValueError:
    # runs if a value error exception occurs
except:
    # runs if any exception besides ValueError occurs in try block
else:
    # runs if try block succeeds
finally:
    # always runs no matter what
```

Try statement flow:

- The code within the try clause is executed
- If no exceptions are raised, then the except class is skipped and the else clause is run
- If an exception is raised then the rest of the try clause is skipped. Then if its type matches the exception type of the except keyword, then that clause is exected
- If and exception is raised and there is no matching type then it is an unhandled exception and the program will terminate.
- The finally clause will also run no matter if there is an expection or not.

Raising Exceptions:
A programmer can raise an exception allowing to protect against certain conditions. For example, if you have a function that is expecting a number as an argument you can raise an exception if that argument is not a number.

```python
x = "2"

if not type(x) is int:
  raise TypeError("Unexpected type. Int is required.")
```

User defined Exceptions
Python allows you to define your own exception. A programmer will create their own exception class that will typically derive from Pythons exception class.

```python
class Custom_Error(Exception):
```

### Suggested Projects

- Return to the programs you have previously written and add some expection handling. :)
