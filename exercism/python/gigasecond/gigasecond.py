from datetime import timedelta


GIGASECOND = timedelta(seconds=10**9)

def add(moment):
    return moment + GIGASECOND
