# USING SPLIT METHOD:
#ask user to enter a string 
user_string = input ("Please enter a string of words:")

#make each alternate character in string upper case and the rest lowercase
split_new_string = ""
for i in range(len(user_string)):
    if i % 2 == 1:
        split_new_string += user_string[i].upper()
    else:
        split_new_string += user_string[i].lower()
print(split_new_string)

#USING JOIN METHOD:
#ask user to enter a string
user_string = input ("Please enter a string of words")

#make each alternate word in the string upper case and the rest lowercase 
join_new_string= []
for i in range(len(user_string.split())):
    if i % 2 == 1:
        join_new_string.append(user_string.split()[i].upper())
    else:
        join_new_string.append(user_string.split()[i].lower())
print(" ".join(join_new_string))


