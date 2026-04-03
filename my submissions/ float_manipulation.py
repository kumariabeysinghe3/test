import statistics
#ask user to enter a list of 10 floats and store the floats in a list
float_list =  []
for i in range(10):
    float_list.append(float(input("Enter a float: ")))
#when the user has entered all 10 floats, calculate and print the sum, minimum, maximum, mean (rounded to 2 decimal places) and median of the list of floats
while len(float_list) < 10:
    float_list.append(float(input("Enter a float: ")))
if len(float_list) == 10:
    print(sum(float_list))
    print(min(float_list))
    print(max(float_list))
    print(round(statistics.mean(float_list), 2))
    print(statistics.median(float_list))
    

