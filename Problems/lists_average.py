# define a function that takes any number of lists containing
# integers. This function returns the average of the corresponding
# numbers from each list. For example
# l1 = [1,2,3,4] , l2 = [5,6,2,4], l3= [7,8,9,0]
# average = [(1+5+7)/3, (2+6+8)/3, (3+2+9)/3, (4,4,0)/3]

# def average(*args):
#     average_list = []
#     for pair in zip(*args):
#         average_list.append(sum(pair)/len(pair))
#     return average_list


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
# print(average(l1, l2, l3))

# the above function can also be defined as

average = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]

print(average(l1, l2, l3))
