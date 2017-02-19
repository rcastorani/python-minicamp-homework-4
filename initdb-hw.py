import sqlite3

connection = sqlite3.connect('databasehw.db')
print('Connected!')

connection.execute('CREATE TABLE movies (name TEXT, genre TEXT)')
print('Table created!')

connection.close()
