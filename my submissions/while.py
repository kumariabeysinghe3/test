#variables for average calculation:
total = 0
count = 0

while True:
    number= int(input("Please enter a number (enter -1) to stop:"))
    
    #break loop id number is -1
    if number== -1:
        break

    #make 0 an invalid entry 
    if number== 0:
        print("0 is not a valid entry, please enter another number")
        continue 

    #add valid numbers to total and the count
    total += number 
    count += 1 

#calculate and print average 
if count > 0:
    average = total/count
    print(f"The average of the numbers you entered was {average}")

else:
    print("You have not entered any numbers")
