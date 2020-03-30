from string import ascii_lowercase as lowercase_letters

# Time Complexity: O(n)
# Space Complexity: O(1)

def is_pangram_1(sentence):
    uniq_letters = set()

    for letter in sentence.lower():
        if letter in lowercase_letters:
            uniq_letters.add(letter)

    return set(lowercase_letters) == uniq_letters


# Time Complexity: O(n)
# Space Complexity: O(1)

def is_pangram_2(sentence):
    all_letters = set(lowercase_letters)

    for letter in sentence.lower():
        all_letters.discard(letter)

    return not all_letters


# Time Complexity: O(n) -- not sure if this is the case
# Space Complexity: O(1)

def is_pangram(sentence):
    all_altters = set(lowercase_letters)

    uniq_chars_in_sentence = set(sentence.lower())

    return len(all_altters - uniq_chars_in_sentence) == 0
