# Task-3 Debugging
# Given below is a Bash / Python script that performs following computation on an integer input (n):
# If n is less than 10: Calculate its Square
# Example: 4 => 16
# If n is between 10 and 20: Calculate the factorial of (n-10)
# Example: 15 => 120
# If n is greater than 20: Calculate the sum of all integers between 1 and (n-20)
# Example: 25 => 15
# The task is to identify the bugs in the script, fix them and share the new script.


def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n-9):  # Adjusted the range to calculate factorial correctly
            out *= i
    else:
        lim = n - 20
        out = sum(range(1, lim+1))  # Corrected the calculation for sum of integers
    print(out)

# Test the function
compute(4)  # Expected output: 16
compute(15)  # Expected output: 120
compute(25)  # Expected output: 15
