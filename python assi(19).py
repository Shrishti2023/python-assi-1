#19.Write a python program that removes all punctuation from a given string.
import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Example usage:
text = input("Enter a string to remove punctuation: ")
print(remove_punctuation(text))
