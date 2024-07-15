squares = [i ** 2 for i in range(1, 11)]
print(squares)

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)


# Replace map() and filter() with list comprehensions
grades = ["A", "B", "A", "C"]
marks = [{"A": 8, "B": 6, "C": 4, "D": 2}.get(grade) for grade in grades]
print(marks)

passed_grades = [grade for grade in grades if grade in ("A", "B")]
print(passed_grades)
