x = 10

def function1():
    x = 15
    print(x)

function1()
print(x)

def function2():
    global x
    x = 15

function2()
print(x)
