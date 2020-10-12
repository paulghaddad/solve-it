from operator import itemgetter


class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append((name, grade))

    def roster(self):
        return [
            student[0]
            for student
            in sorted(self.students, key=itemgetter(1, 0))
        ]

    def grade(self, grade_number):
        students_in_grade = [
            student[0]
            for student
            in self.students
                if student[1] == grade_number
        ]

        return sorted(students_in_grade)
