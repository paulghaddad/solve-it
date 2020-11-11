def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if _is_anagram(word, candidate)]


def _is_anagram(word1, word2):
    return word1.lower() != word2.lower() and sorted(word1.lower()) == sorted(word2.lower())
