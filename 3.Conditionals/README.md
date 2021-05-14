## Python 🐍: Conditionals, Comparison Operators

### Conditionals

Computers are able to evalulate information and make decisions quickly. For example, sensors on cars are able to react and apply the brakes helping prevent car accidents.

In this case the computer checks a set of conditions: Is there something in the path of the car? If yes, apply breaks; If no, continue driving.

The statement that allows for conditonial checks is called the **if** statement.

```python
if condition:
    #perform actions
```

The **if** statement if an important tool in programming, it allows the programmer to tell the computer wheter to run a group of instructions based on the value of a condition.

The condition a programmer is usually testing with a **if** statement is a **Boolean** expression, **True** or **False**.

If the condition is true, the program will run the indented statement(s). However, if the condition is false the program will skip the indented statements and continue on.

You may need to check more then one possible outcome. In that case you can add a else conditional to run code when the condition is false

```python
if condition:
    #runs if True
else:
    #runs if False
```

If you need to check more then two outcomes you can use the **elif** conditional clause. This will allow you to check many conditions

```python
if condtion1:
    # runs if condition1 true
elif condition2:
    #runs if condition2 is true
else:
    # runs if condition1 and condition2 are false
```

### Comparison Operators

Comparison operators allow you to evalulate two values to see how the compare to each other. Are the values the same? Is one larger than the other? Is one smaller than the other?

| Python Symbol | Meaning                  | Example | Result |
| ------------- | ------------------------ | ------- | ------ |
| <             | Less than                | 1 < 2   | True   |
| <=            | Less than or equal to    | 1 <= 2  | True   |
| >             | Greater                  | 1 > 2   | False  |
| >=            | Greater than or equal to | 1 >= 2  | False  |
| ==            | Equal to                 | 1 == 2  | False  |
| !=            | Not equal to             | 1 != 2  | True   |

### Complex conditions If, and, or, not

There are times when a single conditional statement is not enough. What if you wanted to know if it cold and rainy or warm and sunny?

Programmin languages support compound **if** statements, which are similar to compound sentences. In the example below we check that today is Tueday and you have money, if that is true then you can eat some Tacos.

```python
if today == 'tuesday' and i_have_money == True:
    # eat some tacos
```

### Logic Operators

| Logical Operator | Usage                         | Result                                               |
| ---------------- | ----------------------------- | ---------------------------------------------------- |
| and              | if(condition1 and condition2) | True only if both condition1 and condition2 are true |
| or               | if(condition1 or condition2)  | True if either condition1 or condition2 is true      |
| not              | if not (condition)            | True only if the condition is False                  |

### Suggested Projects

- what to wear - a program that determines what to wear based on the weather
- adventure game - a program that creates a adventure game where the result changes based on the path the user takes
