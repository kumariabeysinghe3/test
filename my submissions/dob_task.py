from os import write

#write a program that reads the data from the text file provided (DOB.txt) 
#and prints it out in two different sections: one for names and another for birthdates

#assign variables name and birthdate to empty strings
Names = ""
Birthdates = ""

#open the file and read/writge the data to the variables
with open("DOB.txt","r+") as file:
    for line in file:
        names= line.split(",")[0]
        birthdates= line.split(",")[2]
        Names += names + "\n"
        Birthdates += birthdates + "\n"
#print the names and birthdates in two different sections
print("Names:")
print(Names)
print("Birthdates:")
print(Birthdates) 

