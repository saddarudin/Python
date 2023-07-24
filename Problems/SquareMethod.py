# Make a method which takes list as an input
# and returns its square

def square(my_list):
    square_list = []
    for i in my_list:
        square_list.append(i*i)

    return square_list


list1 = [1, 2, 3, 4, 5]
print(square(list1))
