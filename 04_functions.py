# 04_functions.py
# Functions, Parameters vs Arguments

def greet(name):
    print(f"Hi {name}!")

greet("Karina")

# Function with return value
def square(a):
    return a * a
print(square(5))

# Function that adds two numbers and checks even/odd
def add_evenorodd(x, y):
    return x + y

result = add_evenorodd(10, 2)
print(result)
if result % 2 == 0:
    print("EVEN")
else:
    print("ODD")
