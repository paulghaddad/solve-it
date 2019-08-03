import re

WORD_REGEX = re.compile(r"[a-zA-Z']+")


def abbreviate(long_name):
    words = re.findall(WORD_REGEX, long_name)
    return "".join([word[0].upper() for word in words])
