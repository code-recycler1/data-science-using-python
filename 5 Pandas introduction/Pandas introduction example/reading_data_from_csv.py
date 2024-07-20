import pandas as pd

print('Read csv:')
df = pd.read_csv('data/purchases/purchases.csv')
print(df)
print()

print('Read csv, if the csv does not contain indexes:')
df = pd.read_csv('data/purchases/purchases.csv', index_col=0)
print(df)
