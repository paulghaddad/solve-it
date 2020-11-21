def decode(string):
    decoded = ""

    left, right = 0, 0
    while left < len(string):
        peek = string[right]

        if peek.isdigit():
            while right < len(string) and string[right].isdigit():
                right += 1

            count = int(string[left:right])
            letter = string[right]
        else:
            count = 1
            letter = peek


        decoded += count * letter
        right += 1
        left = right

    return decoded


def encode(string):
    encoded = ""

    if not string:
        return encoded

    left, right = 0, 0

    while left < len(string):
        while right < len(string) and string[left] == string[right]:
            right += 1

        if right-left > 1:
            encoded += str(right-left) + string[left]
        else:
            encoded += string[left]

        left = right

    return encoded
