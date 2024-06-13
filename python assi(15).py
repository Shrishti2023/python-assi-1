#15.Write a program that reads data from a CSV file and prints it to the console.
import csv

# Imaginary student data
data = [
    ['Name', 'Age', 'Branch', 'CGPA'],
    ['Alice', 20, 'Computer Science', 8.5],
    ['Bob', 22, 'Electrical Engineering', 7.8],
    ['Carol', 21, 'Mechanical Engineering', 7.2]
]

# Specify the file path
csv_file_path = 'students_data.csv'

# Write the data to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' created successfully.")
import csv

def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(', '.join(row))

# Example usage:
csv_file_path = 'students_data.csv'  # Replace with the actual path to your CSV file
read_csv_file(csv_file_path)

