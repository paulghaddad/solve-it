user_records = {}

with open('/etc/passwd') as f:
    for line in f:
        if line.startswith('#'):
            continue

        user, _, record, *others = line.strip().split(':')
        user_records[user] = record

for user, record in sorted(user_records.items()):
    print(f'User: {user} Record: {record}')
