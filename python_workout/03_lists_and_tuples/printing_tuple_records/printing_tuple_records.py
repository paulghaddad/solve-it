from operator import itemgetter


people = [
    ('Donald', 'Trump', 7.85),
    ('Vladimir', 'Putin', 3.626),
    ('Jinping', 'Xi', 10.603)
]


def arrival_times(people):
    for first, last, travel_time in sorted(people, key=itemgetter(1, 0)):
        row = '{:<10} {:<10} {:5.2f}'.format(last, first, travel_time)
        print(row)


print(arrival_times(people))
