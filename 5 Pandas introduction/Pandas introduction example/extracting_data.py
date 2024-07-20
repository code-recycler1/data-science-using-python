from creating_dataframes_from_scratch import purchases

# Extract rows based on their index
row = purchases.iloc[2]
print('iloc[2]:')
print(row)
print()

# Extract multiple rows
rows = purchases.iloc[[2, 3]]
print('Extract multiple rows:')
print(rows)
print()

# Extract (multiple) columns
columns = ['oranges', 'apples']
fruits = purchases[columns]
print('Extract (multiple) columns:')
print(fruits)
print()

# Slice rows with indexes
# sliced_with_indexes = purchases[0:4]
sliced_with_indexes = purchases[-1::-1]
# sliced_with_indexes = purchases[1:2]
# sliced_with_indexes = purchases[::+2]
# sliced_with_indexes = purchases[-1:]
# sliced_with_indexes = purchases.iloc[1:2]
print('Sliced with indexes:')
print(sliced_with_indexes)
print()

# Slice rows with labels
sliced_with_labels = purchases.loc['June':'Lily']
print('Sliced with labels:')
print(sliced_with_labels)
print()
