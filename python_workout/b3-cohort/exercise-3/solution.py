from functools import reduce
from itertools import zip_longest


def tr(source_chars, translations):
    if not source_chars or not translations:
        raise TypeError("The source characters or translation cannot be empty")

    translation_map = dict(zip_longest(source_chars, translations, fillvalue=translations[-1]))

    def translate_char(char):
        return translation_map.get(char, char)

    def translate_str(source_str):
        return reduce(
            lambda translated_str, char: translated_str + translate_char(char),
            source_str,
            "",
        )

    return translate_str
