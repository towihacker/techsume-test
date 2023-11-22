#!/bin/python3

# Importing flask
from flask import Flask, render_template, request, flash, redirect, url_for, session, redirect

import sqlite3
# import requests -- unused

# Initialize flask app
app = Flask(__name__)
app.secret_key = "techsumeKey"

def init_database():
    con = sqlite3.connect("techsume.db")
    con.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            username TEXT,
            password TEXT,
            name TEXT,
            phone INTEGER,
            email TEXT
        )
    """)
    con.close()



# Directed to home page aka 'index.html'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    formid = request.args.get('formid', 1, type=int)
    session.pop('_flashes', None)
    
    if request.method == 'POST' and formid == 1:
        con = sqlite3.connect('techsume.db')
        cur = con.cursor()
        
        cur.execute("INSERT INTO customer (username, password, name, phone, email) VALUES ('ian', '123', 'ian', '781', 'a@s')")
        
        username = request.form['name']
        password = request.form['password']
        
        cur.execute("SELECT username,password FROM customer WHERE username=? AND password=?", (username, password))
        result = cur.fetchall()
        
        if result:
            return redirect(url_for("user"))
        else:
            flash("Incorrect username or password", "danger")
        con.close()
    elif request.method == 'POST' and formid == 2:
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        
        con = sqlite3.connect("techsume.db")
        cur = con.cursor()
        
        cur.execute("SELECT username,password,name FROM customer WHERE  username=? OR (name=? AND password=?)", (username, name, password))
        result = cur.fetchall()
        
        if result:
            flash("Username taken")
        else:
            cur.execute("INSERT INTO customer (name, username, password) VALUES (?, ?, ?)", (name, username, password))
            con.commit()
            flash("You are registered", "success")
            con.close()
            return redirect(url_for("user"))
        
    return render_template('login.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == '__main__':
    init_database()
    app.run(debug=True)
