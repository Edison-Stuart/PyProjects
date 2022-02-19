import hashlib
import sqlite3

class DataBase:
    """ This class connects to and interacts with a database filled with app user data."""
    def __init__(self,my_db):
        self.conn = sqlite3.connect(my_db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, name text, password text, security text)")
        self.conn.commit()

    def insert(self,uname, pword, security_answer):
        """ This method adds a new user to the database."""
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?)",(uname,pword,security_answer))
        self.conn.commit() 
    
    def view_user_security_data(self, uname):
        """This method allows you to get the saved security answer data."""
        self.cur.execute("SELECT password, security FROM book WHERE name=?",(uname,))
        rows=self.cur.fetchall()
        return rows
    
    def view_user_login_data(self, uname):
        """This method allows you to get the saved user password."""
        self.cur.execute("SELECT password FROM book WHERE name=?",(uname,))
        rows=self.cur.fetchall()
        return rows
    
    def view_all(self):
        """This method selects all from the database"""
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def is_in_db(self,uname):
        """This method allows you to search for a book using any of the four identifiers."""
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        answer = None
        for users in rows:
            if users[1] != uname:
                answer = False
            elif users[1] == uname:
                answer = True
                break
        return answer
    
    
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
