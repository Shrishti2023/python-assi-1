#9.Write a python program that checks if a substring is present in a given string.
def is_substring_present(main_string, substring):
    return substring in main_string

# Example usage:
main_string = "Hello world!"
substring_to_check = "world"
if is_substring_present(main_string, substring_to_check):
    print(f"'{substring_to_check}' is present in the string.")
else:
    print(f"'{substring_to_check}' is not present in the string.")
