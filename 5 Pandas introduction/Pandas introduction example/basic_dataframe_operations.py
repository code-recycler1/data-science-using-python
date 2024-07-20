import pandas as pd

df_movies = pd.read_csv('data/movies/IMDB-Movie-Data.csv', index_col='Title')
head = df_movies.head(3)
tail = df_movies.tail(2)

print('Head:\n', head)
print()
print('Tail:\n', tail)
