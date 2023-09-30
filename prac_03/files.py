"""
CP1404/CP5632 - Practical
"""

# Question 1
name = input("Enter your name: ")
with open(name + '.txt', 'w') as out_file:
    print(name, file=out_file)

# Question 2
with open(name + '.txt', 'r') as in_file:
    name = in_file.read().strip()
    print(f'Your name is {name}')
