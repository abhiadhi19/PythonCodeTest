def calculator():
    while True:
        print("\nOptions: +, -, *, /")
        print("Enter 'quit' to end")
        operator = input("Enter operator: ")

        if operator == 'quit':
            break

        if operator in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operator == '+':
                    print("Result:", num1 + num2)
                elif operator == '-':
                    print("Result:", num1 - num2)
                elif operator == '*':
                    print("Result:", num1 * num2)
                elif operator == '/':
                    print("Result:", num1 / num2 if num2 != 0 else "Error: Division by Zero")
            except ValueError:
                print("Invalid input! Please enter numerical values.")
        else:
            print("Invalid operator!")

# Start the calculator
calculator()