#6.Write a program that reads the content of a text file and prints it to the console.
# Create a text file and write content to it
file_path = 'my_file.txt'
content_to_write = "Hello, world! This is some sample content."

try:
    with open(file_path, 'w') as file:
        file.write(content_to_write)
    print(f"Content written to '{file_path}' successfully.")

    # Now let's read the content from the file
    with open(file_path, 'r') as file:
        file_content = file.read()
        print("File Content:\n", file_content)
except Exception as e:
    print(f"An error occurred: {e}")

