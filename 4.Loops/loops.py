count = 0
while count < 10:
    print("while Count is ", count)
    count += 1

for index in range(10):
    print("For loop index is ", index)


for i in range(2):
    print('Outer loop variable is ', i)
    for j in range(3):
        print('Inner loop variable is ', j)
