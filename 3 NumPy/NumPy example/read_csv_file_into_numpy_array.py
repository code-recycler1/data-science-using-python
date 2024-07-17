import numpy as np

loaded_data = np.loadtxt(fname='student_grades.txt', delimiter=',')
print(type(loaded_data))
print(loaded_data)

loaded_data = np.loadtxt(fname='student_grades.txt', delimiter=',', dtype=int)
print(type(loaded_data))
print(loaded_data)

loaded_data = np.genfromtxt(fname='student_grades_2.txt', delimiter=',', dtype=int, filling_values=0)
print(loaded_data)
