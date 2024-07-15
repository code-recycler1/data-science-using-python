# Parallel iteration with print of counter
students = ["Ann", "Bert", "Chris", "Dave"]
grades = ["A", "B", "A", "C"]

for i, (student, grade) in enumerate(zip(students, grades)):
    print(i, student, grade)
