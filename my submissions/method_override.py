#ask user for input 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hair_colour = input("Enter your hair colour: ")
eye_colour = input("Enter your eye colour: ")


#create class 
class Adult: 
    def __init__(self):
        self.name = name 
        self.age = age 
        self.hair_colour = hair_colour 
        self.eye_colour = eye_colour
    #create method 
    def can_drive(self):
        print(f"{self.name} can drive as they are over 18")

#create subclass of adult class called child and override method to print they are too young to drive
class Child(Adult):
    def can_drive(self):
        print(f"{self.name} cannot drive as they are too young")


#create logic based on age and print relevant message 
if age >= 18:
    adult = Adult()
    adult.can_drive()
else:
    child = Child()
    child.can_drive()
    