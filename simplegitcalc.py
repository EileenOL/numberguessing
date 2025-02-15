def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y



def calculator():
    print("Select operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")
    print("\n")

    while True:
        choice = input("Enter choice Add, Subtract, Multiply,Exit calculator: ")

        if choice in ["Add", "Subtract", "Multiply"]:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))

            if choice == "Add":
                print(f"{first_number} + {second_number} = {add(first_number, second_number)}")
            elif choice == "Subtract":
                print(f"{first_number} - {second_number} = {subtract(first_number, second_number)}")
            elif choice == "Multiply":
                print(f"{first_number} * {second_number} = {multiply(first_number, second_number)}")
            
        elif choice == "Exit":
            print("Thank you for using the Calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid operation. \n")


calculator()