print((lambda x, y: x + y)(2, 3))

grades = ["A", "B", "A", "C"]

passed_grades = list(filter(lambda grade: grade in ("A", "B"), grades))
print(passed_grades)

marks = list(map(lambda grade: {"A": 8, "B": 6, "C": 4, "D": 2}.get(grade), grades))
print(marks)
