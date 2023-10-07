from tkinter import *
import speedtest

sp = Tk()
sp.title("\n******Internet Speed******\n")
sp.geometry("800x800")
sp.config(background="Blue")

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str( round(sp.download()/(10**6) , 3)) + " MPBS"
    up = str(round(sp.upload() / (10**6) , 3)) + " MPBS"
    lab_d.config(text = down)
    lab_u.config(text = up)




lab = Label(sp, text="Internet Sped Test" , font = ("Time new Roman" , 30 ) ,bg = "Blue",fg = "White" )
lab.place(x=60, y=20, height  = 50 , width = 380)# Your tkinter GUI code here

lab= Label(sp, text="Downloading Spped " , font = ("Time new Roman" , 30 ) ,bg = "Black",fg = "White" )
lab.place(x=60, y=150, height  = 50 , width = 380)# Your tkinter GUI code here


lab_d= Label(sp, text="00" , font = ("Time new Roman" , 30 ) ,bg = "Black",fg = "White" )
lab_d.place(x=60, y=280, height  = 50 , width = 380)# Your tkinter GUI code here

lab= Label(sp, text="Uploading Spped " , font = ("Time new Roman" , 30 ) ,bg = "Black",fg = "White" )
lab.place(x=60, y=410, height  = 50 , width = 380)# Your tkinter GUI code here


lab_u= Label(sp, text="00" , font = ("Time new Roman" , 30 ) ,bg = "Black",fg = "White" )
lab_u.place(x=60, y=530, height  = 50 , width = 480)# Your tkinter GUI code here


button = Button(sp, text= 'Check Speed' , font = ("Time new Roman" , 30 ) ,fg = "White" , relief = RAISED , bg = "Green", command = speedcheck)
button.place(x=60, y=680, height  = 50 , width = 380)

sp.mainloop()
