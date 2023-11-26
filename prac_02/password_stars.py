"""Password stars
gets user to input password and confirm it meets the min lentgh
than print the password in *
"""


def get_password():
    """Retrieves the password from the user and confirms it meets min length"""

    password_length = 10
    password = input(f'Enter a password with a min length of {password_length} : ')

    while len(password) < password_length:
        print("Password to short, Please enter a longer password")
        password = input(f'Enter a password with a min length of {password_length} : ')

    return password


def password_print(password):
    """Prints the password in *"""
    print(len(password) * '*')


password = get_password()
password_print(password)
