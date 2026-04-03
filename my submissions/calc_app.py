file_name = "equations.txt"

def print_previous_equations():
    try:
        with open(file_name, "r") as file:
            equations = file.readlines()
            if equations:
                print("Previous Equations:")
                for equation in equations:
                    print(equation.strip())
            else:
                print("No previous equations found.")
    except FileNotFoundError:
        print("No previous equations found.")

def perform_calculation():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers.")
        return

    operator = input("Enter the operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Cannot divide by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    print(f"{num1} {operator} {num2} = {result}")

    with open(file_name, "a") as file:
        file.write(f"{num1} {operator} {num2} = {result}\n")


# MAIN PROGRAM
choice = input("Enter '1' to calculate or '2' to view history: ")

if choice == '1':
    perform_calculation()   
elif choice == '2':
    print_previous_equations()
else:
    print("Invalid choice.")




