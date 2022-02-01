#!/usr/bin/env python3
from flask import Flask
from flask import render_template as RT

app = Flask(__name__)

@app.route('/')
def home():
    return RT("home.html")

@app.route('/about/')
def about():
    return RT("about.html")


if __name__ =="__main__":
    app.run(debug=True,host='0.0.0.0')
