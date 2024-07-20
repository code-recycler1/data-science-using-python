import pandas as pd

df_movies = pd.read_csv('data/movies/IMDB-Movie-Data.csv', index_col='Title')

# Rename specific columns
df_movies.rename(
    columns={
        'Runtime (Minutes)': 'Runtime',
        'Revenue (Millions)': 'Revenue_millions'
    },
    inplace=True
)

# Clean up column names by lowercasing them, removing special characters,
# and replacing spaces with underscores
df_movies.columns = [col.lower().replace(' ', '_') for col in df_movies.columns]

# print(df_movies[['runtime', 'revenue_millions']])
