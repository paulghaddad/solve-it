# Time Complexity: O(n)
# Space Complexity: O(1)
def plus_one_approach_1(digits):
    i = len(digits) - 1

    while digits[i] == 9:
        digits[i] = 0
        i -= 1
        if i < 0:
            digits.insert(0, 1)
            return digits

    digits[i] += 1

    return digits

# Time Complexity: O(n)
# Space Complexity: O(1)
def plus_one_approach_2(digits):
    decimal = 0
    num_digits = len(digits)

    for i, digit in enumerate(digits):
        if i < num_digits - 1:
            decimal = 10 * (decimal + digit)
        else:
            decimal += digit

    decimal += 1

    return [int(digit) for digit in str(decimal)]
