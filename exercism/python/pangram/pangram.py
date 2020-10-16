from string import ascii_lowercase as letters


def is_pangram(sentence):
    letters_in_sentence = set(sentence.lower())

    return set(letters).issubset(letters_in_sentence)
