#!/usr/bin/env python3
import sqlite3

class DataBase:
    """ This class connects to and interacts with a book keeping database."""
    def __init__(self,my_db):
        self.conn = sqlite3.connect(my_db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        """ This method adds a new book to the database using the title, author, year, and isbn."""
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit() 
    
    def view(self):
        """This method allows you to see all the books added thus far."""
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows
    
    def search(self,title="",author="",year="",isbn=""):
        """This method allows you to search for a book using any of the four identifiers."""
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows
    
    def delete(self,book_id):
        """This method deletes a selection from the database."""
        self.cur.execute("DELETE FROM book WHERE id=?",(book_id,))
        self.conn.commit()
    
    def update(self,book_id,title,author,year,isbn):
        """This method lets you update existing books with new information."""
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,book_id))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()



#insert("The Sun","John Smith",1976,4364645754)
# delete(5)
# update(6,"The Moon","John Smooth",1917,9999)
# print(view())
# print(search(author="John Smooth"))
