VOWELS = set(['a', 'e', 'i', 'o', 'u'])


def convert_to_pig_latin(english_string):
    pig_latin_words = []

    for english_word in english_string.split(' '):
        if english_word[0].lower() in VOWELS:
            pig_latin_words.append(english_word + 'way')
        else:
            first_letter, rest_of_word = english_word[0], english_word[1:]
            pig_latin_words.append(rest_of_word + first_letter + 'ay')

    return ' '.join(pig_latin_words)
