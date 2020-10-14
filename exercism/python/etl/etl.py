def transform(legacy_data):
    return {
        letter.lower(): count
        for count, letters in legacy_data.items()
        for letter in letters
    }
