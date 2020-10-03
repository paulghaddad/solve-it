from datetime import timedelta

GIGASECOND = timedelta(seconds=1e9)


def add(moment):
    return moment + GIGASECOND
