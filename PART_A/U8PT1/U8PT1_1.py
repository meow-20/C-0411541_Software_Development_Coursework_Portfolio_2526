# 1. Factorial of a Number (Mathematical Sequence)
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

number = float(input("Enter a number: "))
print(f"Factorial of {number} is {factorial(number)}")
