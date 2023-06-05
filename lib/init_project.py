import sqlite3
import sys
import tkinter as tk
import os


filename = sys.argv[1]
project_path = sys.argv[2]

project = os.path.basename(project_path)

connection = sqlite3.connect(f"{filename}/timesheet.db")

cur = connection.cursor()
cur.execute("PRAGMA foreign_keys = ON")
connection.commit()

window = tk.Tk()
window.resizable(width=False,height=False)
window.title('Configure Project')
frame1 = tk.Frame(master=window,width=1000,height=1000,padx=10,bg='gray')
frame1.pack(side='left')
header = tk.Label(text='Enter Project Name', master=frame1)
header.pack()
proj_name = tk.Entry(frame1, width=20)
proj_name.pack()
proj_name.delete(0,tk.END)
proj_name.insert(0,project)
desc_field = tk.Text(frame1,height=5,width=20)
desc_field.pack()
activity_name = None
def handle_click(event):
    
    project_name = proj_name.get()
    project_desc = desc_field.get("1.0",'end-2c')
    if project_name:
        exestrn = f'INSERT INTO projects VALUES (\'{project_name}\', \'{project_desc}\', \'{project_path}\')'

        cur.execute(exestrn)

        connection.commit()
        window.destroy()

button = tk.Button(text="Submit",master=frame1,command=handle_click)
# button.bind('<Return>',handle_click)
window.bind('<Return>',handle_click)
button.pack()
window.attributes("-topmost", True)
proj_name.focus_set()
window.mainloop()