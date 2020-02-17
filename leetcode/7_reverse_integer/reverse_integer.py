def reverse(x):
    reversed_int = 0

    el = abs(x)
    while (el):
        rdigit = el % 10
        el = int(el / 10)
        reversed_int = reversed_int * 10 + rdigit

    if reversed_int > 2**31:
        return 0

    if x < 0:
        return -reversed_int

    return reversed_int
