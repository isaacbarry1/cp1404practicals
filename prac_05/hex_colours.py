"""
CP1404/CP5632 Practical
Hex colour lookup
"""

COLOUR_CODES = {'Absolute Zero': '#0048ba', 'Amber': '#ffbf00', 'AntiqueWhite1': '#ffefdb',
                'Aquamarine1': '#7fffd4', 'Ash Grey': '#b2beb5', 'Bisque1': '#ffe4c4'}

colour_name = input('Enter a colour name: ')
while colour_name != '':
    print(f"Code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")
