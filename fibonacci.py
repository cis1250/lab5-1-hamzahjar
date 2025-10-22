#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def validate_input():
    while True:
        try:
            i = int(input("Please enter a POSITIVE number corresponding to the term you would like to know: "))
            if i > 0:
                return i
            print("Please input a POSITIVE number.")
        except ValueError:
            print("Please input a positive INTEGER.")


def calculate_fibonacci(n):
    term1, term2, term3 = 0, 1, 0
    fib_sequence = []

    if n == 1:
        fib_sequence.append(term1)
    elif n == 2:
        fib_sequence.extend([term1, term2])
    else:
        fib_sequence.extend([term1, term2])
        for _ in range(3, n + 1):
            term3 = term1 + term2
            term1 = term2
            term2 = term3
            fib_sequence.append(term3)
    return fib_sequence


def print_fibonacci(fib_sequence):
    print(*fib_sequence)


# Main program flow
i = validate_input()
fib_sequence = calculate_fibonacci(i)
print_fibonacci(fib_sequence)
