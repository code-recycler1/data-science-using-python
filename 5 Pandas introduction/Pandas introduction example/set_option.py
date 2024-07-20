import pandas as pd

df_movies = pd.read_csv('data/movies/IMDB-Movie-Data.csv', index_col='Title')
pd.set_option('display.max_columns', 4)
pd.set_option('display.max_rows', 6)

print(df_movies)
