UNIQUE_SIDES = {
    'equilateral': 1,
    'isosceles': (1, 2),
    'scalene': 3,
}


def equilateral(sides):
    return all(sides) and len(set(sides)) == UNIQUE_SIDES['equilateral']


def isosceles(sides):
    return valid_triangle(sides) and len(set(sides)) in UNIQUE_SIDES['isosceles']


def scalene(sides):
    return valid_triangle(sides) and len(set(sides)) == UNIQUE_SIDES['scalene']


def valid_triangle(sides):
    a, b, c = sorted(sides)
    return all(sides) and a+b >= c
