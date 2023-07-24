# define a function that takes list as an argument
# and returns reversed list

def reverse(original_list):
    reversed_list = []
    for i in range(len(original_list)-1, -1, -1):
        reversed_list.append(original_list[i])
    return reversed_list

number = [1, 2, 3, 4, 5]

print(reverse(number))
