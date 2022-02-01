#!/usr/bin/env python3
import tkinter

window = tkinter.Tk()

def km_to_Mi():
    miles = float(e1_value.get())*1.6
    t1.delete("1.0",tkinter.END)
    t1.insert(tkinter.END,miles)

b1 = tkinter.Button(window,text="Execute",command=km_to_Mi)
b1.grid(row=0,column=0)

e1_value = tkinter.StringVar()
e1 = tkinter.Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = tkinter.Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()