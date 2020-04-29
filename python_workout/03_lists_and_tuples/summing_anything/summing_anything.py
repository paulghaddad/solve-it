from functools import reduce
from operator import add


def mysum(*args):
    if not args:
        return ()

    return reduce(add, args)
