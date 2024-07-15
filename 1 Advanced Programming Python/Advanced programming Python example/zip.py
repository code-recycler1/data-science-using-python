students = ["Ann", "Bert", "Chris", "Dave"]
grades = ["A", "B", "A", "C"]


for student, grade in zip(students, grades):
    print(student, grade)
print()

# Zip returns list of tuples
print(list(zip(students, grades)))

# In case of unequal length?
print(list(zip(students, grades, range(2))))
