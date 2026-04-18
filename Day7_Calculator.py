# calculator.py

def run_calculator():
    print("--- Simple Python Calculator ---")

    try:
        # 1. Ask for user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # 2. Ask for the operation
        operation = input("Choose an operation (+, -, *, /): ")

        # 3. Perform calculation and handle division by zero
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: You cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operation selected.")
            return

        # 4. Print the result
        print(f"Result: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    run_calculator()