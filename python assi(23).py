#23.Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
def convert_temperature(temp, scale):
    if scale.lower() == 'c':
        return (temp * 9/5) + 32
    elif scale.lower() == 'f':
        return (temp - 32) * 5/9
    else:
        return "Invalid scale! Use 'C' for Celsius or 'F' for Fahrenheit."

# Example usage:
temp = float(input("Enter the temperature: "))
scale = input("Enter the scale ('C' for Celsius, 'F' for Fahrenheit): ")
print(f"The converted temperature is {convert_temperature(temp, scale)} degrees.")
