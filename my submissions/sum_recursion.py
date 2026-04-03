#Define a function which takes two arguments
def sum_recursion (num_list, index):
    #base case
    if index == 0:
        return num_list[0]

    else: 
    #recursive case 
        return num_list[index] + sum_recursion(num_list, index -1)


#test function 
print(sum_recursion([3,4,6,3,5,1], 2))

