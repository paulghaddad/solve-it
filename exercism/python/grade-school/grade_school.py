from collections import defaultdict


class School:
    def __init__(self):
        self._students = defaultdict(list)

    def add_student(self, name, grade):
        self._students[grade].append(name)

    def roster(self):
        roster_by_grade = []
        for grade in sorted(self._students.keys()):
            roster_by_grade.extend(sorted(self._students[grade]))

        return roster_by_grade

    def grade(self, grade_number):
        return sorted(self._students[grade_number])
