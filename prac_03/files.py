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

# Question 3
with open('numbers.txt', 'r') as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# Question 3 extension
total = 0
with open('numbers.txt', 'r') as in_file:
    for line in in_file:
        total += int(line)
print(total)


