sound_factors = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong',
}

def convert(number):
    sounds = [sound for factor, sound in sound_factors.items() if number % factor == 0]

    return ''.join(sounds) or str(number)
