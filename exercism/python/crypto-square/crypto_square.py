def cipher_text(plain_text):
    letters = [char for char in plain_text.lower() if char.isalnum()]

    cols, rows = _get_rect_dimensions(len(letters))

    spaces_needed = cols*rows - len(letters)
    if spaces_needed:
        for i in range(spaces_needed):
            letters.append(' ')

    rect = [letters[cols*i:cols*i+rows+1] for i in range(rows)]

    encoded_rect = [[rect[row][col] for row in range(rows)] for col in range(cols)]

    encoded = ''
    for col in range(cols):
        encoded += ''.join(encoded_rect[col])

        if col < cols-1:
            encoded += ' '

    return encoded


def _get_rect_dimensions(num_elements):
    r = 0
    c = 1

    while True:
        if c*r >= num_elements and c >= r and c-r <= 1:
                return c, r

        if c*(r+1) >= num_elements and c >= (r+1) and c-(r+1) <= 1:
            return c, r+1

        c += 1
        r += 1
