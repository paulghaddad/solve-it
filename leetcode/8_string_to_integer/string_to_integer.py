INT_MAX = 2**31 - 1
INT_MIN = -2**31

# Time Complexity: O(n)
# Space Complexity: O(n)

def my_a_to_i(s):
    pointer = 0
    integer = 0
    negative = False
    positive_sign = False

    for i in range(len(s)):
        if s[pointer] == ' ':
            pointer += 1
        else:
            break

    if pointer < len(s) and s[pointer] == '+':
        positive_sign = True
        pointer += 1

    if pointer < len(s) and s[pointer] == '-':
        if positive_sign:
            return 0

        negative = True
        pointer += 1

    for i in range(pointer, len(s)):
        if not s[i].isdigit():
            break

        integer = integer * 10 + int(s[i])

    if negative:
        integer = -integer
    if integer > INT_MAX:
        return INT_MAX
    if integer < INT_MIN:
        return INT_MIN

    return integer
