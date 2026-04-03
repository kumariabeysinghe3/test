# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #syntax, error missing parenthesis

print("\n") #syntax error, error missing parenthesis

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" #syntax error, error missing parenthesis and wrong operator
age =age_Str.replace(" years old", "") #syntax error, error missing parenthesis and wrong operator
age = int(age) #syntax error, error missing parenthesis and wrong operator
print("I'm " + str(age) + " years old.")#runtime error, error missing space between "I'm" and the age variable

    # Variables declaring additional years and printing the total years of age
years_from_now = int("3") #syntax error, error missing parenthesis and wrong operator
total_years = age + years_from_now

print(f"The total number of years: {total_years}") #syntax error, missing parenthesis and wrong variable 

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = (total_years * 12) + 6   #syntax error, incorrect variable name and addition operator 6
print(f"In 3 years and 6 months, I'll be {total_months} months old")

#HINT, 330 months is the correct answer
