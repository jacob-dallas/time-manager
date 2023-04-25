import sqlite3

connection = sqlite3.connect('test')

connection.commit()

cur = connection.cursor()

cur.execute('CREATE TABLE activity(goal, accomplished, time, logged_out)')

connection.close()