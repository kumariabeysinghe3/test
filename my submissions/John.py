#takes in a user’s input as a string
name_str= input ("Please enter your name")
#add every string entered to a list until “John” is entered and stores all incorrectly entered strings in a list where “John” is the only correct string
incorrect_names = []
while name_str != "John":
    incorrect_names.append(name_str)
    name_str = input("Please enter your name")
correct_name = "John"

if name_str == correct_name:
#prints out the list of incorrectly entered strings
    print("Incorrectly entered names:")
    print(incorrect_names)
