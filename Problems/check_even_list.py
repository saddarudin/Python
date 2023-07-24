# Define a function that takes list as a parameter and returns true 
# if all the elements of a list are even

def is_even(original_list):
    for num in original_list:
        if num % 2 != 0:
            return False
    return True


list1 = [2, 4, 6, 8, 101]
print(is_even(list1))
