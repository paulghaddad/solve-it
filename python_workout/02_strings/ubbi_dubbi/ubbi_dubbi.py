import re

VOWELS = set(['a', 'e', 'i', 'o', 'u'])


def translate_to_Ubbi_dubbi_1(english_string):
    ubbi_dubbi_chars = []

    for char in english_string:
        if char in VOWELS:
            ubbi_dubbi_chars.append('ub' + char)
        else:
            ubbi_dubbi_chars.append(char)

    return ''.join(ubbi_dubbi_chars)


def translate_to_Ubbi_dubbi_2(english_string):
    vowel_regex = r'[aeiou]'
    return re.sub(vowel_regex, lambda match: 'ub'+match.group(0), english_string)
