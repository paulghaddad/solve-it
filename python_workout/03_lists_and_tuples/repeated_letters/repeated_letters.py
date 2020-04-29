from collections import Counter
from operator import itemgetter


def most_repeating_word(words):
    word_counts = {
        word: Counter(word).most_common(1)[0][1]
        for word in words
    }

    return max(word_counts.items(), key=itemgetter(1))[0]
