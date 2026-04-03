def largest_number (num_list):
    #base case- if list only has one integer 
    if len(num_list) == 1:
        return num_list[0]

    #recursive case if list has multiple integers to return max 
    larger_list = largest_number(num_list[1:])

    if num_list[0] > larger_list:
        return num_list[0]
    
    else: 
        return larger_list 
    

#test 
print(largest_number([4,2,6,10,2,4,7,12,5]))




 
