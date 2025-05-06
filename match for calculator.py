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
    if b==0:
        return "Error : Division by Zero is not allowed !"
    else:
        return a / b

# --- Main Program ---
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")


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
        print("Result:", divide(num1, num2))
    case _:
        print("Invalid input")
