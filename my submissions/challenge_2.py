#request users favourite request
string_fav= input ("Please enter your favourite restaurant?")
#ask users favourite number 
int_fav = int(input ("Please enter your favourite number?"))
print(f"Your favourite restaurant is {string_fav}")
print (f"Your favourite number is {int_fav}")
#cast string_fav to an interger and print it
try:
    int_string_fav = int(string_fav)
    print(f"Your favourite restaurant as an integer is {int_string_fav}")
except ValueError:
    #this happens as the restaurant name cannot be converted to an integer