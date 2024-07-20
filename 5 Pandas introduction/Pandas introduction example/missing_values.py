import pandas as pd

df_movies = pd.read_csv('data/movies/IMDB-Movie-Data.csv', index_col='Title')

print('Shape at the start:', df_movies.shape)
print()

# Look for missing values
print('Missing values:')
print(df_movies.isnull().sum())
print()

# Drop rows OR columns with null values
df_movies.dropna(inplace=True)
print('Shape after removing rows with missing values:', df_movies.shape)  # Output: (838, 11)

# df_movies.dropna(axis=1, inplace=True)
# print('Shape after removing columns with missing values:', df_movies.shape)  # Output: (1000, 9)
