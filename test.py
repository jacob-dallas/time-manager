import sqlite3
import sys


filename = sys.argv[1]

connection = sqlite3.connect(filename)

connection.commit()

cur = connection.cursor()

cur.execute('CREATE TABLE activity(goal, accomplished, time, logged_out)')

connection.close()