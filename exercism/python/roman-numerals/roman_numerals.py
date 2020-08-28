arabic_to_roman = {
    1000: 'M',
    500: 'D',
    100: 'C',
    50: 'L',
    10: 'X',
    5: 'V',
    1: 'I',
}

def roman(number):
    if number == 0:
        return ''

    for ar, rom in arabic_to_roman.items():
        if number >= 900 and number < 1000:
            return 'CM' + roman(number-900)

        if number >= 400 and number < 500:
            return 'CD' + roman(number-400)

        if number >= 90 and number < 100:
            return 'XC' + roman(number-90)

        if number >= 40 and number < 50:
            return 'XL' + roman(number-40)

        if ar - number == 1:
            return 'I' + rom + roman(number-(ar-1))

        if number // ar > 0:
            return rom + roman(number-ar)
