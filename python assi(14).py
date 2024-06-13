#14.Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
def read_multiple_lines():
    lines = []
    print("Enter multiple lines (an empty line to finish):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines

# Example usage:
for line in read_multiple_lines():
    print(line)

