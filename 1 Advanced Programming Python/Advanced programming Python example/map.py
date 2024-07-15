def transform(grade):
    lookup_dict = {"A": 8, "B": 6, "C": 4, "D": 2}
    return lookup_dict.get(grade)


grades = ["A", "B", "A", "C"]
marks = list(map(transform, grades))
print(marks)
