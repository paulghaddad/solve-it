import re


def abbreviate(words):
    return ''.join([word[0] for word in re.split(r'[-_\s]+', words)]).upper()
