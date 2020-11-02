def steps(number):
    if number < 1:
        raise ValueError('The number must be greater than 0')

    steps = 0
    while number > 1:
        steps += 1

        if number%2 == 0:
            number //= 2
        else:
            number = 3*number + 1

    return steps
