import pandas as pd

df_movies = pd.read_csv('data/movies/IMDB-Movie-Data.csv', index_col='Title')

print(df_movies.info())
print()
print('Shape:', df_movies.shape)
print()
print('Describe:\n', df_movies.describe())

# Select columns of a certain type using the include parameter
print('Object:\n', df_movies.describe(include="object"))
print('Int:\n', df_movies.describe(include="int"))
