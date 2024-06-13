#11.Write a python program that generates the first n numbers in the Fibonacci sequence.
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Example usage:
n = int(input("Enter the number of Fibonacci numbers needed: "))
print(fibonacci(n))
