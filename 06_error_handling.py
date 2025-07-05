# 06_error_handling.py
# Try-Except Blocks

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Invalid input")

# Common Errors:
# ZeroDivisionError, ValueError, TypeError, IndexError, KeyError, FileNotFoundError
