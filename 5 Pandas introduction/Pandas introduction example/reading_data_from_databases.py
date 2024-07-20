import sqlite3
import pandas as pd

con = sqlite3.connect('data/purchases/purchases.db')  # Connect to the SQLite database
df = pd.read_sql_query('SELECT * FROM purchases', con)

print(df)
