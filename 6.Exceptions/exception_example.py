try:
    x = int(input("Enter a number: "))
except ValueError as err:
    print("Not a valid number {err}".format(err=err))
else:
    print(x, "is a number")
finally:
    print("I always run")


try:
    f = open('unknown_file.txt', 'r')
except OSError as err:
    print("OS ERROR", err)
except:
    print("This is not run because OSError was raised and handled.")
else:
    f.close()
