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
        if 1000 - number > 0 and 1000 - number < 100:
            return 'CM' + roman(number-900)

        if 500 - number > 0 and 500 - number < 100:
            return 'CD' + roman(number-400)

        if 100 - number > 0 and 100 - number < 10:
            return 'XC' + roman(number-90)

        if 50 - number > 0 and 50 - number < 10:
            return 'XL' + roman(number-40)

        if ar - number == 1:
            return 'I' + rom + roman(number-(ar-1))

        if number // ar > 0:
            return rom + roman(number-ar)
