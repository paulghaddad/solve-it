# Score categories
# Change the values as you see fit
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12

SINGLE_CATEGORIES = (ONES, TWOS, THREES, FOURS, FIVES, SIXES)


category_scorer = {
    'YACHT': lambda dice: _is_yacht(dice) and 50
}


def score(dice, category):
    if category in SINGLE_CATEGORIES:
        return _score_singles(dice, category)

    counts_of_matches = _count_matches(dice)


    if category == FULL_HOUSE and _is_full_house(counts_of_matches):
        return sum(dice)

    if category == FOUR_OF_A_KIND and _is_four_of_a_kind(counts_of_matches):
        match_counts = _count_matches(dice)
        for die, count in match_counts.items():
            if count == 4 or count == 5:
                return 4 * die

    if category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30

    if category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30

    if category == CHOICE:
        return sum(dice)

    if category == YACHT:
        return category_scorer['YACHT'](dice)

    return 0


def _score_singles(dice, category):
    num_matches = filter(lambda x: x == category, dice)
    return len(list(num_matches)) * category


def _is_yacht(dice):
    return len(set(dice)) == 1

def _is_full_house(counts):
    match_counts = counts.values()
    return 2 in match_counts and 3 in match_counts


def _is_four_of_a_kind(counts):
    match_counts = counts.values()
    for count in match_counts:
        if count >= 4:
            return True

    return False


def _count_matches(dice):
    counts = {}

    for die in dice:
        if die in counts:
            counts[die] += 1
        else:
            counts[die] = 1

    return counts
