#12.Write a python program that calculates the sum of the digits of a given number.
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Example usage:
number = int(input("Enter a number to calculate the sum of its digits: "))
print(sum_of_digits(number))

