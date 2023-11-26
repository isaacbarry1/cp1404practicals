"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When a non int number is entered
2. When will a ZeroDivisionError occur? When the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


def zero_check(denominator):
    """Function to check if a number is 0"""
    while denominator == 0:
        print('Denominator cannot be Zero')
        denominator = int(input("Enter the denominator: "))
    return denominator


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    denominator = zero_check(denominator)  # Function  to check if denominator is zero

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
