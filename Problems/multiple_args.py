# create  a method that takes input a number and variable
# args (*args) and returns the list of variable_args with
# power of the given number
# e.g: fun(3,2,3,1)
# output:[8,27,1]
# if variable args are not provided then print the message
# "you did not pass args"

def power_list(num, *args):
    return [x**num for x in args]


my_list = [2, 4, 5, 3]
# either you can pass the arguments one by one like (2,3,4) or list with
# * operator it will unpack the list and pass the elements one by one
print(power_list(4, *my_list))
