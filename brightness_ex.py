#!/usr/bin/env python
#http://cactusprojects.com/rpi-lcd-brightness-widget
from Tkinter import *
from subprocess import *

app=Tk()
app.resizable(width=False, height=False)
app.title('Screen Brightness Adjuster')
app.geometry('450x100') # Size
slider=Scale(app, length=400, tickinterval=10, from_=0, to=100, orient=HORIZONTAL)
slider.set(50)
slider.pack()

def pressed():
    value = slider.get()
    value = value*2
    call("sudo sh -c 'echo " + str(value) + " > /sys/class/backlight/rpi_backlight/brightness'",shell=TRUE)
    
button=Button(app,text="Set brightness",command=pressed)
button.pack()

mainloop()
