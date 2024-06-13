#16.Write a program in python that counts the frequency of each character in a string.
def character_frequency(string):
    return {char: string.count(char) for char in set(string)}

# Example usage:
string = input("Enter a string to count the frequency of each character: ")
print(character_frequency(string))
