from column_names_cleanup import df_movies

# Make conditional selections using logical operators
conditional_selection = df_movies[df_movies['director'] == 'Ridley Scott']
print('Conditional selection:')
print(conditional_selection)
print()

# Combine conditions (use '&' or '|')
combined_conditions = df_movies[(df_movies['director'] == 'Ridley Scott') & (df_movies['rating'] > 7.0)]
print('Combined conditions:')
print(combined_conditions)
print()

# Movies directed by Ridley Scott OR James Gunn
isin = df_movies[df_movies['director'].isin(['Ridley Scott', 'James Gunn'])]
print('Using the isin method:')
print(isin)
