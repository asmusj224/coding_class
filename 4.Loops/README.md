## Python 🐍: Loops

### Loops

When steps of a program need to be repeated multiple times, programmer use loops instead of writing each statement out multiple times.

For example, say you wanted to draw a square.
Pseudocode would like like the following.

```python
draw line
pivot 90 degrees
draw line
pivot 90 degrees
draw line
pivot 90 degrees
draw line
pivot 90 degrees
```

Instead of writing each of those lines, we can create a loop that will repeat the steps a set number of times.

Python supports three types of loops

- for loops - executes statements a set number of times
- while loops - executes statements while the condition is true
- nested loops - A loop that is contain within another loop.

**For**

```python
for i in range(4):
    draw line
    pivot 90 degress
```

**While**

```python
count = 0
while count < 5:
    print('In while loop')
    count += 1
```

**Nested**

```python
for i in range(2):
    for j in range(3):
        print('inner loop')
    print('outer loop')
```

### Suggested Projects

- **Art Project** - A program that uses the turtle module and creates a work of art. You can use loops to change pen color, shape, width, etc.
