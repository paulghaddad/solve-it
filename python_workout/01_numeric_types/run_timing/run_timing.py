from decimal import Decimal


def calculate_average_run_times():
    run_times = []

    while True:
        run_time = input('Enter 10 km run time, or "q" to exit: ')

        if run_time == 'q':
            break

        try:
            run_times.append(Decimal(run_time))
        except ValueError:
            print('You entered an invalid number!')


    return sum(run_times) / len(run_times)


if __name__ == '__main__':
    average_run_time = calculate_average_run_times()
    print(f'You averaged {average_run_time} seconds for your runs')
