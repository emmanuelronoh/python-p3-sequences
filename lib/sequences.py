def print_fibonacci(length):
    if length == 0:
        print('[]')  # Print '[]' explicitly for length 0
    elif length == 1:
        print('[0]')  # Special case for length 1
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        print(fib_sequence)

# Example usage:
print_fibonacci(0)  # Output: []
print_fibonacci(1)  # Output: [0]
print_fibonacci(5)  # Output: [0, 1, 1, 2, 3]
print_fibonacci(10) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
