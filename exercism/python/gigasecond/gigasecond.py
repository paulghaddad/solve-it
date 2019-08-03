import datetime

GIGASECOND = 10 ** 9


def add_gigasecond(birth_date):
    return birth_date + datetime.timedelta(seconds=GIGASECOND)
