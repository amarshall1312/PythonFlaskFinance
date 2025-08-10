from flask import Flask, render_template, request, redirect
import sqlite3
import os

db = "finance.db"

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/")
def index():
    connection = get_db_connection()
    items = connection.execute("SELECT * FROM savingpots").fetchall()
    connection.close()
    return render_template("index.html", items=items)

