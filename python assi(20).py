#20.Write a python program that takes a list of numbers and returns their sum.
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage:
my_list = [12, 15, 3, 10]
result = sum_of_list(my_list)
print("Sum of all elements in the list:", result)

