# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:  # Check for division by zero
        return "Error: Division by zero is not allowed!"
    else:
        return a / b

# --- Main Program ---
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Handle invalid choice input with a try-except block
try:
    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        raise ValueError("Invalid operation choice. Please select a valid operation.")

    # Get the numbers from the user, ensuring they are valid
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Using match statement instead of if-elif
    match choice:
        case '1':
            print("Result:", add(num1, num2))
        case '2':
            print("Result:", subtract(num1, num2))
        case '3':
            print("Result:", multiply(num1, num2))
        case '4':
            print("Result:", divide(num1, num2))  # Handles division by zero

except ValueError as ve:
    print(f"Error: Please enter numeric values only.")

except ZeroDivisionError as zde:
    print(f"Error: {zde}")

except OverflowError:
    print("Error: The numbers are too large to handle.")

except TypeError:
    print("Error: Invalid data type entered. Please enter numeric values.")

except KeyboardInterrupt:
    print("\nOperation was interrupted by the user.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print("No errors occurred. The operation was successful!")  # This runs only if no exception occurs

finally:
    print("✅ Program execution completed. Thank you for using the calculator! 👋")
