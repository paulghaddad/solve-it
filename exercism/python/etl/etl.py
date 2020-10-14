def transform(legacy_data):
    transform = {}
    for count, letters in legacy_data.items():
        for letter in letters:
            transform[letter.lower()] = count

    return transform
