import hashlib
import os
import sqlite3

class DataBase:
    """ This class connects to and interacts with a book keeping database."""
    def __init__(self,my_db):
        self.conn = sqlite3.connect(my_db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, name text, password text, security text)")
        self.conn.commit()

    def insert(self,uname, pword, security_answer):
        """ This method adds a new book to the database using the title, author, year, and isbn."""
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?)",(uname,pword,security_answer))
        self.conn.commit() 
    
    def view_user_security_data(self, uname):
        """This method allows you to see all the books added thus far."""
        self.cur.execute("SELECT password, security FROM book WHERE name=?",(uname,))
        rows=self.cur.fetchall()
        return rows
    
    def view_user_login_data(self, uname):
        """This method allows you to see all the books added thus far."""
        self.cur.execute("SELECT password FROM book WHERE name=?",(uname,))
        rows=self.cur.fetchall()
        return rows
    
    # def search(self,title="",author="",year="",isbn=""):
    #     """This method allows you to search for a book using any of the four identifiers."""
    #     self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    #     rows=self.cur.fetchall()
    #     return rows
    
    # def delete(self,book_id):
    #     """This method deletes a selection from the database."""
    #     self.cur.execute("DELETE FROM book WHERE id=?",(book_id,))
    #     self.conn.commit()
    
    def update_password(self,password,uname):
        """This method lets you update existing books with new information."""
        self.cur.execute("UPDATE book SET password=? WHERE name=?",(password,uname))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()


def hash_password(password, salt):
    """Takes a string password and a byte-like-object as a salt
        and then creates a key from it"""
    my_key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return my_key

def validate_password(u_input, saved_password, salt):
    """Takes a saved password and salt combo then checks
        if the input password is the same as the saved one"""
    my_key = hashlib.pbkdf2_hmac('sha256', u_input.encode('utf-8'), salt, 100000)
    if my_key == saved_password:
        return True
    else:
        return False
