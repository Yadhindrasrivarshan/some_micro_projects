from tkinter import  *
import  time

win=Tk()
win.title("DIGITAL CLOCK")
win.geometry("300x150")

def digital_clock():
    time1=time.strftime("%H:%M:%S")
    current_time.config(text=time1)
    current_time.after(250,digital_clock)

digi_clock=Label(win,text="Digital Clock",font=("arial",25,'bold'))
digi_clock.grid(row=0,column=0)

current_time=Label(win,font=("times new roman",35,"bold"),bg="yellow")
current_time.grid(row=1,column=0,padx=60,pady=35)
digital_clock()

win.mainloop()
