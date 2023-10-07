from tkinter import *
import os

def restart():
    os.system('Shutdown /r /t 1')

def restart_time():
    os.system('Shutdown /r /t 20')
def logout():
    os.system('Shutdown -1')
def shutdown():
    os.system('Shutdown /s /t/ 1')

st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg = "Grey")

r_button = Button(st, text = "Restart" , 
                  font = ("Times New Roman", 20, "bold"), 
                  relief = RAISED, cursor = "plus" ,command=restart)
r_button.place(x=200, y=60, height = 50, width = 150)

rt_button = Button(st, text = "Restart Time" , 
                   font = ("Times New Roman", 20, "bold"), 
                   relief = RAISED, cursor = "plus" ,command=restart_time )
rt_button.place(x=200, y=150, height = 50, width = 150)

lg_button = Button(st, text = "Log Out" , 
                   font = ("Times New Roman", 20, "bold"), 
                   relief = RAISED, cursor = "plus" ,command=logout)
lg_button.place(x=200, y=250, height = 50, width = 150)

st_button = Button(st, text = "Shut Down" , 
                   font = ("Times New Roman", 20, "bold"), 
                   relief = RAISED, cursor = "plus" ,command=shutdown )
st_button.place(x=200, y=350, height = 50, width = 150)
st.mainloop()