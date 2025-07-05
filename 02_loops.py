# 02_loops.py
# While and For Loops

# While loop example
i = 0
while i < 3:
    print(i)
    i += 1

# For loop with range
for i in range(1, 4):
    print(i)

# Loop through a string
for letter in "cat":
    print(letter)

# Loop with custom step
for i in range(10, 0, -2):
    print(i)

# Skip specific values using continue
for i in range(2, 20, 2):
    if i == 10 or i == 14:
        continue
    print(i)
