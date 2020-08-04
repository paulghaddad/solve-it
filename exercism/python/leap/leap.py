def leap_year(year):
    div = divisible(year)

    return div(400) or div(4) and not div(100)

def divisible(year):
    return lambda n: year % n == 0
