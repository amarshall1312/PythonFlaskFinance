from flask import Flask, render_template, request, redirect
import sqlite3
import os
import income

db = "finance.db"

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/")
def index():
    connection = get_db_connection()
    items = connection.execute("SELECT * FROM outgoings").fetchall()
    connection.close()
    return render_template("index.html", items=items, incomes=income.calculate_total_income([2100,1800]))

@app.route("/second")
def second_page():
    return render_template("second.html")

@app.route("/add-outgoing", methods=["POST"])
def add_item():
    name = request.form["name"]
    monthly_cost = request.form["monthly-cost"]
    fixed = 1 if request.form.get("fixed") == "on" else 0
    frequency = request.form.get("frequency", "monthly")
    # Optionally handle date and category, or set to None/default
    date = None
    category = None

    if name.strip():
        connection = get_db_connection()
        connection.execute(
            "INSERT INTO outgoings (name, fixed, amount, frequency, date, category) VALUES (?, ?, ?, ?, ?, ?)",
            (name, fixed, monthly_cost, frequency, date, category)
        )
        connection.commit()
        connection.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

