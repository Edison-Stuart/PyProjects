#!/usr/bin/env python3
import tkinter

my_window = tkinter.Tk()

def Kg_convert():
    myEntry = float(entry_1_var.get())
    # Kg to Grams
    textB_1.insert(tkinter.END,myEntry*1000)
    # Kg to pounds approximate
    textB_2.insert(tkinter.END,myEntry*2.205)
    # Kg to ounces
    textB_3.insert(tkinter.END,myEntry*35,274)

def Text_clear():
    box = (textB_1,textB_2,textB_3)
    for stuff in box:
        stuff.delete("1.0","end")

label_1 = tkinter.Label(my_window,text="Kg")
label_1.grid(row=0,column=0)

entry_1_var = tkinter.StringVar()
entry_1 = tkinter.Entry(my_window,textvariable=entry_1_var)
entry_1.grid(row=0,column=1)

button_1 = tkinter.Button(my_window,text="Convert",command=Kg_convert)
button_1.grid(row=0,column=2)

button_2 = tkinter.Button(my_window,text="Clear Boxes",command=Text_clear)
button_2.grid(row=0,column=3)

textB_1 = tkinter.Text(my_window,height=1,width=20)
textB_1.grid(row=1,column=0)

textB_2 = tkinter.Text(my_window,height=1,width=20)
textB_2.grid(row=1,column=1)

textB_3 = tkinter.Text(my_window,height=1,width=20)
textB_3.grid(row=1,column=2)

my_window.mainloop()