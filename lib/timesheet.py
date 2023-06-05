import sqlite3


connection = sqlite3.connect('./timesheet.db')

connection.commit()

cur = connection.cursor()

cur.execute("PRAGMA foreign_keys = ON")
connection.commit()

cur.execute('CREATE TABLE hours(id INTEGER PRIMARY KEY, day, time, overtime, time_desc, overtime_desc)')

cur.execute('CREATE TABLE activities(name TEXT PRIMARY KEY, total_time, week_time, day_time)')
cur.execute('CREATE TABLE projects(name TEXT PRIMARY KEY, desc, fp)')

cur.execute('CREATE TABLE log(id INTEGER PRIMARY KEY, date, time_in, time_out, time_tot, goal, accomplished, next, activity, project, FOREIGN KEY(activity) REFERENCES activities(name),FOREIGN KEY(project) REFERENCES projects(name))')

cur.execute('CREATE TABLE status(user INTEGER PRIMARY KEY, logged_in INTEGER, activity TEXT, project, FOREIGN KEY(activity) REFERENCES activities(name),FOREIGN KEY(project) REFERENCES projects(name))')
connection.commit()

connection.close()