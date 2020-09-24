def is_isogram(string):
    letters = set()

    for letter in string.lower():
        if letter in letters:
            return False

        if letter.isalpha():
            letters.add(letter)

    return True
