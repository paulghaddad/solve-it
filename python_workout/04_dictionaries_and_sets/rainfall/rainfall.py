from collections import defaultdict

rainfall_totals = defaultdict(int)

while True:
    print('Enter city and rainfall amount: ')
    city = input()
    if not city:
        break

    rainfall_amount = int(input())
    rainfall_totals[city] += rainfall_amount

for city, amount in rainfall_totals.items():
    print(f'{city}: {amount}')
