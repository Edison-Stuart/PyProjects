#!/usr/bin/env python3
import psycopg2
HOST = "0.0.0.0"
PORT = "8080"
USERNAME = "postgres"
PASSWORD = "agoodpassword"
DBNAME = "postgres"

def get_connection():
    return psycopg2.connect(f"dbname='{DBNAME}' user='{USERNAME}' password='{PASSWORD}' host='{HOST}' port='{PORT}'")

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {DBNAME} (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO %s VALUES ('%s','%s','%s')"%(DBNAME, item, quantity, price))
    conn.commit()
    conn.close()


def view_data():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {DBNAME}")
    rows = cur.fetchall()
    conn.close
    return rows

def delete(item):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {DBNAME} WHERE item={item}")
    conn.commit()
    conn.close

def update(quantity,price,item):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"UPDATE {DBNAME} SET quantity={quantity}, price={price} WHERE item={item}")
    conn.commit()
    conn.close