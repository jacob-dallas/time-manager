import sqlite3
import sys
import datetime

log = sys.argv[1]
activity = sys.argv[2]
# get project name

#get project id by name
time = datetime.datetime.now()

activity = input('What activity are you doing today?')

connection = sqlite3.connect(log)

cur = connection.cursor()
cur.execute("PRAGMA foreign_keys = ON")
connection.commit()

cur.execute(exestrn)

exestrn = f'INSERT INTO log VALUES (activity name, 0, 0, 0)'
cur.execute(exestrn)

connection.commit()

connection = sqlite3.connect('./timesheet.db')
