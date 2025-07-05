# 05_builtins_lambdas.py
# Built-in Functions, Lambda, Map, Filter

numbers = [12, 45, 23, 67, 34, 89, 5]
print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Type of first element:", type(numbers[0]))

# Access each element with index
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

# Lambda functions are anonymous 1-line functions
# Syntax: lambda arguments: expression

n = [1,2,3,4,5,6,7,8,9,10]

# Double each number using map
double = list(map(lambda x: x*2, n))
print(double)

# Filter even numbers
even = list(filter(lambda x: x%2 == 0, n))
print(even)
