import re

from collections import Counter


def count_words(sentence):
    words = re.findall(r'\d+|[a-z]+\'[a-z]+|[a-z]+', sentence.lower())

    return Counter(words)
