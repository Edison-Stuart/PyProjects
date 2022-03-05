#!/usr/bin/env python3
import tkinter
import random

window = tkinter.Tk()

def roll_20():
    my_roll = random.randint(1,20)
    t1.delete("1.0",tkinter.END)
    t1.insert(tkinter.END,my_roll+bonus_var.get())


def roll_12():
    my_roll = random.randint(1,12)
    t1.delete("1.0",tkinter.END)
    t1.insert(tkinter.END,my_roll+bonus_var.get())

def roll_10():
    my_roll = random.randint(1,10)
    t1.delete("1.0",tkinter.END)
    t1.insert(tkinter.END,my_roll+bonus_var.get())

def roll_8():
    my_roll = random.randint(1,8)
    t1.delete("1.0",tkinter.END)
    t1.insert(tkinter.END,my_roll+bonus_var.get())

def roll_6():
    my_roll = random.randint(1,6)
    t1.delete("1.0",tkinter.END)
    t1.insert(tkinter.END,my_roll+bonus_var.get())

def roll_4():
    my_roll = random.randint(1,4)
    t1.delete("1.0",tkinter.END)
    t1.insert(tkinter.END,my_roll+bonus_var.get())

b1 = tkinter.Button(window,text="D20",command=roll_20)
b1.grid(row=0,column=0)

b2 = tkinter.Button(window,text="D12",command=roll_12)
b2.grid(row=1,column=0)

b3 = tkinter.Button(window,text="D10",command=roll_10)
b3.grid(row=2,column=0)

b4 = tkinter.Button(window,text="D8",command=roll_8)
b4.grid(row=3,column=0)

b5 = tkinter.Button(window,text="D6",command=roll_6)
b5.grid(row=4,column=0)

b6 = tkinter.Button(window,text="D4",command=roll_4)
b6.grid(row=5,column=0)

t1 = tkinter.Text(window,height=1,width=20)
t1.grid(row=0,column=1)

bonus_var = tkinter.IntVar()
bonus = tkinter.Entry(window,textvariable=bonus_var)
bonus.grid(row=0,column=2)

label_1 = tkinter.Label(window,text="your roll")
label_1.grid(row=1,column=1)

label_2 = tkinter.Label(window,text="put any bonus here, if none put 0")
label_2.grid(row=1,column=2)

window.mainloop()