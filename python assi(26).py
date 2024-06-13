#26.Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
def check_prefix_suffix(string, prefix='', suffix=''):
    return string.startswith(prefix) and string.endswith(suffix)

# Example usage:
string = input("Enter the string: ")
prefix = input("Enter the prefix (leave empty if not checking for prefix): ")
suffix = input("Enter the suffix (leave empty if not checking for suffix): ")
print(f"String starts with prefix: {check_prefix_suffix(string, prefix=prefix)}")
print(f"String ends with suffix: {check_prefix_suffix(string, suffix=suffix)}")
