
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You cannot divide by zero")
    elif (type(a) is not int) or (type(b) is not int):
        raise TypeError("Provide numbers only")
    return a/b


print(divide(4, '2'))
