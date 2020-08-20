factor_to_sound = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong',
}

factors = (3, 5, 7)


def add_sound(number, factor):
    if number % factor == 0:
        return factor_to_sound[factor]
    else:
        return ""


def convert(number):
    sounds = [add_sound(number, factor) for factor in factors]

    return ''.join(sounds) or str(number)
