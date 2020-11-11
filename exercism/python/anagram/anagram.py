from collections import Counter

def find_anagrams(word, candidates):
    lower_word = word.lower()
    letter_counts = Counter(lower_word)

    return [
        candidate
        for candidate in candidates
            if lower_word != candidate.lower()
            and letter_counts == Counter(candidate.lower())
    ]
