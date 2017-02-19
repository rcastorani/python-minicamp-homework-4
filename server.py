from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/new-friend', methods = ['POST'])
def newFriend():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    name = request.form['name']
    age = request.form['age']

    try:
        cursor.execute('INSERT INTO friends(name, age) VALUES (?, ?)', (name, age))
        connection.commit()
        message = 'Successfully inserted into friends table'
    except:
        connection.rollback()
        message = 'There was an issue inserting the data'
    finally:
        connection.close()
        return message

@app.route('/friends')
def friends():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM friends')
    friendsList = cursor.fetchall()
    connection.close()
    return jsonify(friendsList)

app.run(debug = True)
