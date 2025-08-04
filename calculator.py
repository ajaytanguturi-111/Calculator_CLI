def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    print("Welcome to the CLI Calculator!\n")

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {result}")
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
