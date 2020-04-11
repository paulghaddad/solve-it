import random


def start_game():
    number_to_guess = random.randint(0, 100)

    while True:
        guess = int(input('Guess a number from 0 to 100: '))

        if guess > number_to_guess:
            print('Your guess was too high')
        elif guess < number_to_guess:
            print('Your guess was too low')
        else:
            print('You guessed the correct number!')
            break


if __name__ == '__main__':
    start_game()
