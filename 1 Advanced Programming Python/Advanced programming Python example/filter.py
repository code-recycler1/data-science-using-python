def passed(grade):
    return grade in ("A", "B")


grades = ["A", "B", "A", "C"]
passed_grades = list(filter(passed, grades))
print(passed_grades)
