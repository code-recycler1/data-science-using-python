from column_names_cleanup import df_movies

# Extract that column into its own variable
revenue = df_movies['revenue_millions']

print('Head of revenue:')
print(revenue.head())
print()

# Impute the missing values of revenue using the mean
# Calculate the mean value
revenue_mean = revenue.mean()
print('Revenue mean:', revenue_mean)
print()

print('Missing values before:')
print(df_movies.isnull().sum())
print()

# Fill the nulls
revenue.fillna(revenue_mean, inplace=True)

print('Missing values after:')
print(df_movies.isnull().sum())
print()
