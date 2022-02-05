#!/usr/bin/env python3
import tkinter
from backend import DataBase
"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete entry
Close
"""
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)
        entry1.delete(0,tkinter.END)
        entry1.insert(tkinter.END,selected_tuple[1])
        entry2.delete(0,tkinter.END)
        entry2.insert(tkinter.END,selected_tuple[2])
        entry3.delete(0,tkinter.END)
        entry3.insert(tkinter.END,selected_tuple[3])
        entry4.delete(0,tkinter.END)
        entry4.insert(tkinter.END,selected_tuple[4])
    except IndexError:
        pass

database=DataBase("books.db")

def view_command():
    list1.delete(0,tkinter.END)
    for row in database.view():
        list1.insert(tkinter.END,row)

def search_command():
    list1.delete(0,tkinter.END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(tkinter.END,row)

def add_command():
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,tkinter.END)
    list1.insert(tkinter.END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
    entry1.delete(0,tkinter.END)
    entry2.delete(0,tkinter.END)
    entry3.delete(0,tkinter.END)
    entry4.delete(0,tkinter.END)

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()

window = tkinter.Tk()
window.wm_title("Bookstore")

label1 = tkinter.Label(window,text="Title")
label1.grid(row=0,column=0)

label2 = tkinter.Label(window,text="Author")
label2.grid(row=0,column=2)

label3 = tkinter.Label(window,text="Year")
label3.grid(row=1,column=0)

label4 = tkinter.Label(window,text="ISBN")
label4.grid(row=1,column=2)

title_text = tkinter.StringVar()
entry1 = tkinter.Entry(window,textvariable=title_text)
entry1.grid(row=0,column=1)

author_text = tkinter.StringVar()
entry2 = tkinter.Entry(window,textvariable=author_text)
entry2.grid(row=0,column=3)

year_text = tkinter.StringVar()
entry3 = tkinter.Entry(window,textvariable=year_text)
entry3.grid(row=1,column=1)

isbn_text = tkinter.StringVar()
entry4 = tkinter.Entry(window,textvariable=isbn_text)
entry4.grid(row=1,column=3)

list1 = tkinter.Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

scrollb1 = tkinter.Scrollbar(window)
scrollb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=scrollb1.set)
scrollb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

button1 = tkinter.Button(window,text="View all",width=12,command=view_command)
button1.grid(row=2,column=3)

button2 = tkinter.Button(window,text="Search entry",width=12,command=search_command)
button2.grid(row=3,column=3)

button3 = tkinter.Button(window,text="Add entry",width=12,command=add_command)
button3.grid(row=4,column=3)

button4 = tkinter.Button(window,text="Update selected",width=12,command=update_command)
button4.grid(row=5,column=3)

button5 = tkinter.Button(window,text="Delete selected",width=12,command=delete_command)
button5.grid(row=6,column=3)

button6 = tkinter.Button(window,text="Close",width=12,command=window.destroy)
button6.grid(row=7,column=3)

window.mainloop()
