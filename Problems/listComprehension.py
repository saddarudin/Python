# define a function that takes list of strings
# and returns a list containing reverse of every string

def reverse_each_string(original_list):
    return [x[::-1] for x in original_list]


my_list = ["Saddar", "Shams", "Shahid", "Azhar", "Jawad"]
print(reverse_each_string(my_list))
