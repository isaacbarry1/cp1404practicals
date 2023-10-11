"""
CP1404/CP5632 Practical
Emails
"""


def main():
    """Create a dictionary of users emails and names"""

    email_to_name = {}
    email = input('Email: ')

    while email != '':

        name = get_name_from_email(email)
        confirmation = input(f'Is your name {name}? (Y/n) ')

        if confirmation.upper() != 'Y' and confirmation != "":
            name = input('Name: ')

        email_to_name[email] = name
        email = input('Email: ')

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Get the name from an email"""

    prefix = email.split('@')[0]
    sections = prefix.split('.')

    name = ' '.join(sections).title()
    return name


main()
