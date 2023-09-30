"""
CP1404/CP5632 - Practical
"""

name = input("Enter your name: ")

with open(name + '.txt', 'w') as out_file:
    print(name, file=out_file)



