"""
CP1404/CP5632 - Practical
Fixed program to determine score status
"""


def main():
    """Get a score and print the status"""
    score = float(input("Enter score: "))

    print(determine_status(score))


def determine_status(score):
    """Find the status of a score"""
    if score < 0 or score > 100:
        return "Invalid score"

    elif score >= 90:
        return "Excellent"

    elif score >= 50:
        return "Passable"

    else:
        return "Bad"


main()




