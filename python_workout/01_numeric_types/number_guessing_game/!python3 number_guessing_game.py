import random


def start_game():
    number_to_guess = random.randint(0, 100)
    print(number_to_guess)


if __name__ == '__main__':
    start_game()
