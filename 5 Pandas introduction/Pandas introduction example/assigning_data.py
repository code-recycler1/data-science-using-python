from creating_dataframes_from_scratch import purchases

print('Assigning data to a DataFrame:')

print('Using a constant value:')
purchases['bananas'] = 3
print(purchases)
print()


print('Using an array of values:')
purchases['bananas'] = [2, 0, 5, 7]
print(purchases)
print()

print('Using an iterable:')
purchases['lemons'] = range(1, len(purchases)+1)
print(purchases)
