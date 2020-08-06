EQUILATERAL_UNIQ_SIDES = 1
ISOSCELES_UNIQ_SIDES = (1, 2)
SCALENE_UNIQ_SIDES = 3


def equilateral(sides):
    return all(sides) and len(set(sides)) == EQUILATERAL_UNIQ_SIDES


def isosceles(sides):
    return valid_triangle(sides) and len(set(sides)) in ISOSCELES_UNIQ_SIDES


def scalene(sides):
    return valid_triangle(sides) and len(set(sides)) == SCALENE_UNIQ_SIDES


def valid_triangle(sides):
    sorted_lengths = sorted(sides)

    return all(sides) and sum(sorted_lengths[0:2]) >= max(sorted_lengths)
