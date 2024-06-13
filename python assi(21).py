#21.Write a python program that counts the occurrences of a specific element in a list.
def count_occurrences(lst, element):
    return lst.count(element)

# Example usage:
lst = [1, 2, 3, 4, 2, 2, 5]
element = int(input('enter a number from a list to count the occurence:'))
print(f"The element {element} occurs {count_occurrences(lst, element)} times in the list.")

