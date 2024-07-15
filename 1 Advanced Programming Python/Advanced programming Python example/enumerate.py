students = ["Ann", "Bert", "Chris", "Dave"]


for i, student in enumerate(students):
    print(i, student)
print()


for i, student in enumerate(students, start=1):
    print(i, student)
print()


# Enumerate returns list of tuple
print(list(enumerate(students)))
