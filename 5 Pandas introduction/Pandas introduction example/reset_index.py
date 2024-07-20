from creating_dataframes_from_scratch import purchases

# Go back to the default numeric indexing
# The drop parameter (optional) avoids the old index being added as a column
purchases = purchases.reset_index(drop=True)
print(purchases)
