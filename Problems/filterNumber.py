# Define a function that takes list of strings mixed
# with numbers, strings, lists e.t.c and returns the list
# with numbers only (in simple you have to filter the numbers
# from the mixed list ). Numbers should be string type

def filtered_list(mixed_list):
    return [x for x in mixed_list if (type(x) == int or type(x) == float)]


mixed = [1, 2, "Saddar", [1, 2, 3], 2.5, 6, ("Saddar", "19")]
print(filtered_list(mixed))
