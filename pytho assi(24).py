#24.Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
def simple_calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator!"

# Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
print(f"The result is: {simple_calculator(num1, num2, operator)}")
