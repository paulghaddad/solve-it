from functools import reduce


def mysum(nums, initial=0):
    return reduce(lambda x, y: x + y, nums, initial)
