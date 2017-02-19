import sqlite3

connection = sqlite3.connect('database.db')
print('Connected!')

connection.execute('CREATE TABLE friends (name TEXT, age INTEGER)')
print('Table created!')

connection.close()
