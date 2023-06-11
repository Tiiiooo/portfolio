from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    day_string = strftime("%A")
    day_label.config(text=day_string)
    date_string = strftime("%B %d %V")
    date_label.config(text=date_string)

    time_label.after(1000,update)      # if error use window in place of time_label

window = Tk()

window.title(" Clock ")

window.geometry('500x500')

time_label = Label(window,font=("Arial",50),fg="light green",bg="teal",pady=180)
time_label.pack()

day_label = Label(window,font=("Ink Free",25),fg='orange',bg="teal")
day_label.place(x=20,y=120)

date_label = Label(window,font=("Ink Free",25),fg='orange',bg="teal")
date_label.place(x=280,y=120)

window.resizable(False,False)

window.config(background="teal") 

update() 

window.mainloop()
