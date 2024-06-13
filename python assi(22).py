#22.Write a python program that returns the minimum and maximum values in a list of numbers.
def min_max_values(lst):
    return min(lst), max(lst)

# Example usage:
lst = [23, 1, 45, 92, 7, 34]
min_val, max_val = min_max_values(lst)
print(f"The minimum value is {min_val} and the maximum value is {max_val}.")
