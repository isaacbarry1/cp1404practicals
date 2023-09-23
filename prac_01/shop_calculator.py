num_items = int(input('Number of items: '))

# Loop to make sure the number of items is above 0
while num_items < 0:
    print('Invalid number of items!')
    num_items = int(input('Number of items: '))

price = 0

# Loop to prompt and calc total price of items entered by user
for i in range(0, num_items, 1):
    price += float(input('Price of item: '))

print(f'Total price for {num_items} is ${price:.2f}')

