SIDES_FOR_TYPE = {"equilateral": 1, "isoceles": 2, "scalene": 3}


def is_equilateral(sides):
    return is_kind("equilateral")(sides)


def is_isosceles(sides):
    return is_kind("isoceles")(sides) or is_equilateral(sides)


def is_scalene(sides):
    return is_kind("scalene")(sides)


def is_kind(type):
    return lambda sides: _is_triangle(sides) and len(set(sides)) == SIDES_FOR_TYPE[type]


def _is_triangle(sides):
    return all(sides) and _valid_triangle(sides)


def _valid_triangle(sides):
    return sum(sorted(sides)[:2]) > max(sides)
