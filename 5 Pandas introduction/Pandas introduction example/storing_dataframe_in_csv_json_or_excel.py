import pandas as pd

df = pd.read_csv('data/purchases/purchases.csv')

# Cleaning and transforming your data ...

# Save the dataframe into a new file
df.to_csv('data/purchases/new_purchases.csv')
df.to_json('data/purchases/new_purchases.json')
df.to_excel('data/purchases/new_purchases.xlsx')
