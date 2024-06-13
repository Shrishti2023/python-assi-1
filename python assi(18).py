#18.Write a python program that checks if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example usage:
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print("The strings are anagrams:" if are_anagrams(str1, str2) else "The strings are not anagrams.")