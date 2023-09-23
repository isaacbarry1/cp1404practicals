
password_length = 10
password = input(f'Enter a password with a min length of {password_length} : ')

while len(password) < password_length:
    print("Password to short, Please enter a longer password")
    password = input(f'Enter a password with a min length of {password_length} : ')

print(len(password) * '*')

