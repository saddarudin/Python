# define a function that takes a number n and
# returns a dictionary containing
# cube of numbers form 1 to n

def cube_finder(n):
    cube = {}
    for i in range(1, n+1):
        cube[i] = i**3
    return cube


print(cube_finder(5))

