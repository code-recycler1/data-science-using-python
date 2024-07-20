import pandas as pd

# Create a dictionary with the data
data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

# Create a DataFrame from the dictionary
purchases = pd.DataFrame(data)

# Display the DataFrame (works in Jupyter or IPython)
purchases

print('Start DataFrame:')
# Or use print() to display the DataFrame in scripts or other environments
# print(purchases)

# Customize the default index
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

print(purchases)

# Locate specific customer's purchases
customers_purchases = purchases.loc['Lily']
# print('Specific customer\'s purchases:')
# print(customers_purchases)

print()
