#25.Write a program that copies the contents of one text file to another.
def copy_file_contents(source_file, destination_file):
    with open(source_file, 'r') as src:
        data = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(data)

# Example usage:
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")
copy_file_contents(source_file, destination_file)
