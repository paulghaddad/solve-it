def is_isogram(string):
    letters = set()

    for letter in string.lower():
        if letter in letters:
            return False

        if letter.isalpha():
            letters.add(letter)

    return True


# def is_isogram(string):
#     bs = 0
#     for c in string:
#         n = ord(c.lower()) - ord('a')
#         if not 0 <= n < 26:
#             continue
#
#         print('1 << n', n, 1 << n, bin(1 << n))
#         if bs & (1 << n):
#             return False
#
#         print('bs & (1 << n)', n, bin(bs & (1 << n)))
#
#         bs |= (1 << n)
#         print('bs |= (1 << n)', bin(bs))
#
#     return True
