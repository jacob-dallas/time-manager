import sqlite3
import sys
import tkinter as tk

try:
    fp = sys.argv[1]
except IndexError:
    fp = input('filepath?')
    
connection = sqlite3.connect(f'{fp}/timesheet.db')
cur = connection.cursor()
cur.execute("PRAGMA foreign_keys = ON")
connection.commit()

window = tk.Tk()
window.resizable(width=False,height=False)
window.title('Add an Activity')
frame1 = tk.Frame(master=window,width=1000,height=1000,padx=10,bg='gray')
frame1.pack(side='left')
header = tk.Label(text='enter a new activity', master=frame1)
header.pack()
act_name = tk.Entry(frame1, width=20)
act_name.pack()
desc_field = tk.Text(frame1,height=5,width=20)
desc_field.pack()
activity_name = None
def handle_click(event):
    
    activity_name = act_name.get()
    activity_desc = desc_field.get("1.0",'end-2c')
    if activity_name:
        exestrn = f'INSERT INTO activities VALUES (\'{activity_name}\', \'{activity_desc}\', 0, 0)'

        cur.execute(exestrn)

        connection.commit()
        window.destroy()

button = tk.Button(text="Submit",master=frame1,command=handle_click)
# button.bind('<Return>',handle_click)
window.bind('<Return>',handle_click)
button.pack()
window.attributes("-topmost", True)
act_name.focus_set()
window.mainloop()


