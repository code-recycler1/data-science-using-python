from column_names_cleanup import df_movies

# Movies directed by Ridley Scott OR James Gunn sorted by director in descending order
movies = df_movies[df_movies['director'].isin(['Ridley Scott', 'James Gunn'])].sort_values(by='director',
                                                                                           ascending=False)
print(movies)
print()

# Group the movies by director
grouped = df_movies.groupby('director')
# Get the movies directed by Ridley Scott
ridley_scott_movies = grouped.get_group('Ridley Scott')
print('Directed by Ridley Scott:')
print(ridley_scott_movies)
print()

print('Number of movies directed by Ridley Scott:', len(ridley_scott_movies))
print()

# Retrieve the number of movies directed per director in descending order
print('Movies per director:')
print(df_movies.groupby('director').size().sort_values(ascending=False))
print()

# The get the same result without grouping
print('Using value_counts():')
print(df_movies['director'].value_counts())
