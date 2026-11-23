# app.py
from flask import Flask, render_template, request, redirect, url_for
from database import *

app = Flask(__name__)

@app.route("/")
def index():
    books = query_db("SELECT * FROM Book")
    sales = query_db("SELECT * FROM Sale")
    return render_template("index.html", books=books, sales=sales)


@app.route("/add_book", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    publisher = request.form["publisher"]
    year = int(request.form["year"])
    quantity = int(request.form["quantity"])
    sale_price = float(request.form["sale_price"])
    rent_price = float(request.form["rent_price"])

    execute_db(
        "INSERT INTO Book (title, author, publisher, year, quantity, sale_price, rent_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (title, author, publisher, year, quantity, sale_price, rent_price),
    )

    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)