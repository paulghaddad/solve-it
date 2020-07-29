factor_to_sound = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong',
}


def convert(number):
    sound = ""

    if number % 3 == 0:
        sound += factor_to_sound[3]
    if number % 5 == 0:
        sound += factor_to_sound[5]
    if number % 7 == 0:
        sound += factor_to_sound[7]

    if sound:
        return sound

    return str(number)
