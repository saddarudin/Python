with open('file1.txt', 'r', newline='') as f:
    for line in f.readlines():
        name, age = line.split(',')
        print(f"{name} is {age} years old")
