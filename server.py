from flask import Flask, render_template, request, redirect
import sqlite3
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
    outgoings = connection.execute("SELECT * FROM outgoings").fetchall()
    incomes = connection.execute("SELECT * FROM baseincomes").fetchall()
    savingpots = connection.execute("SELECT * FROM savingpots").fetchall()
    total = 0
    connection.close()
    return render_template("index.html", items=outgoings, incomes=incomes, total=total, saving_pots=savingpots)

@app.route("/second")
def second_page():
    return render_template("second.html")

@app.route("/add-outgoing", methods=["POST"])
def add_outgoing():
    name = request.form["name"]
    monthly_cost = request.form["monthly-cost"]
    fixed = 1 if request.form.get("fixed") == "on" else 0
    frequency = request.form.get("frequency", "monthly")
    # Optionally handle date and category, or set to None/default
    date = request.form["date"]
    category = request.form["category"]

    if name.strip():
        connection = get_db_connection()
        connection.execute(
            "INSERT INTO outgoings (name, fixed, amount, frequency, date, category) VALUES (?, ?, ?, ?, ?, ?)",
            (name, fixed, monthly_cost, frequency, date, category)
        )
        connection.commit()
        connection.close()
    return redirect("/")

@app.route("/add-income", methods=["POST"])
def add_income():
    owner_id = request.form.get("ownerid", 1)
    amount = request.form["amount"]
    frequency = "monthly"

    if amount:
        connection = get_db_connection()
        connection.execute(
            "INSERT INTO baseincomes (owner_id, amount, frequency) VALUES (?, ?, ?)",
            (owner_id, amount, frequency)
        )
        connection.commit()
        connection.close()
    return redirect("/")

@app.route("/add-savingpot", methods=["POST"])
def add_saving_pot():
    name = request.form["name"]
    type = request.form["type"]
    target = request.form["target"]

    if name.strip():
        connection = get_db_connection()
        connection.execute(
            "INSERT INTO savingpots (name, type, target) VALUES (?, ?, ?)",
            (name, type, target)
        )
        connection.commit()
        connection.close
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

