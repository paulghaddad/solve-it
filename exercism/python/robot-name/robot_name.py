import random
from string import (
    ascii_uppercase as upper_letters,
    digits
)


class Robot(object):


    @classmethod
    def create_random_name(cls):
        random.seed()
        name_chars = random.sample(upper_letters, 2) + random.sample(digits, 3)
        return ''.join(name_chars)

    def __init__(self):
        self.reset()


    def reset(self):
        self.name = self.__class__.create_random_name()
