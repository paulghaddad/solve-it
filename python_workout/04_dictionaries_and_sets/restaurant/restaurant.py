MENU = {
    'fish': 25,
    'pizza': 10,
    'steak': 20,
}

total = 0
while True:
    item = input('Order: ').strip()
    if item in MENU:
        total += MENU[item]
        print(f'{item} costs {MENU[item]}, total is {total}')
    elif not item:
        break
    else:
        print(f'Sorry, we are out of fresh {item} today')

print(f'Your total is {total}')
