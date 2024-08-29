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
