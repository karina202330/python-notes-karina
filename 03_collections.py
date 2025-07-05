# 03_collections.py
# Lists, Tuples, Dictionaries, Sets

# LISTS
my_list = [10, 20, 30, 40]
print(my_list[3])

# Modify list element
nums = [5, 10, 15]
nums[1] = 100
print(nums)

# List slicing
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[0:3])        # First 3 elements
print(numbers[-2:])        # Last 2 elements
print(numbers[1:-1])       # All except first and last
print(numbers[::-1])       # Reverse the list

# DICTIONARIES
student = {"name": "Karina", "age": "8"}
print(student.get("name"))         # Safe access
student["grade"] = "A+"             # Add new key-value
student["age"] = "18"              # Update value
del student["grade"]               # Delete key
print(student.keys())               # Print keys
print(student.values())             # Print values

# TUPLES
fruits = ("apple", "banana", "cherry")
print(fruits[2])

# SETS
colour = {"pink", "blue", "purple"}  # No duplicates, unordered
colour.add("yellow")
colour.remove("blue")
print(colour)
