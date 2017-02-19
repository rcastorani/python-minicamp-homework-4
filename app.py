from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movie', methods = ['POST'])
def movie():
    connection = sqlite3.connect('databasehw.db')
    cursor = connection.cursor()

    name = request.form['name']
    genre = request.form['genre']

    try:
        cursor.execute('INSERT INTO movies(name, genre) VALUES (?, ?)', (name, genre))
        connection.commit()
        message = 'Successfully inserted into movies table'
    except:
        connection.rollback()
        message = 'There was an issue inserting the data'
    finally:
        connection.close()
        return message

@app.route('/movies')
def movies():
    connection = sqlite3.connect('databasehw.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM movies')
    moviesList = cursor.fetchall()
    connection.close()
    return jsonify(moviesList)

@app.route('/search')
def search():
    name = request.args.get('name')
    dbQuery = 'SELECT * FROM movies WHERE name = "' + name + '"'
    connection = sqlite3.connect('databasehw.db')

    cursor = connection.cursor()
    cursor.execute(dbQuery)

    favoriteMovie = cursor.fetchall()
    connection.close();

    return jsonify(favoriteMovie);

# @app.route('/new-friend', methods = ['POST'])
# def newFriend():
#     connection = sqlite3.connect('database.db')
#     cursor = connection.cursor()
#
#     name = request.form['name']
#     age = request.form['age']
#
#     try:
#         cursor.execute('INSERT INTO friends(name, age) VALUES (?, ?)', (name, age))
#         connection.commit()
#         message = 'Successfully inserted into friends table'
#     except:
#         connection.rollback()
#         message = 'There was an issue inserting the data'
#     finally:
#         connection.close()
#         return message
#
# @app.route('/friends')
# def friends():
#     connection = sqlite3.connect('database.db')
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM friends')
#     friendsList = cursor.fetchall()
#     connection.close()
#     return jsonify(friendsList)

app.run(debug = True)
