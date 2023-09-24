"""CP1404/CP5632 - Practical
Score menu
"""


def main():
    """Navigate the menu"""

    MENU = """(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit"""
    score = 0
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_score()

        elif choice == "P":
            print(determine_status(score))

        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def show_stars(score):
    """Prints the score in stars"""
    print(score * '*')


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


def get_score():
    """Get a valid score from the user"""

    score = int(input("Enter score: "))

    while score <= 0 or score >= 100:
        print("Invalid score. Must be 0-100 inclusive")
        score = int(input("Enter score: "))

    return score


main()
