from flask import Flask, render_template, request, redirect, url_for, session
from database import *

app = Flask(__name__)

@app.route("/")
def index():
    books = query_db("SELECT * FROM Book")
    return render_template("index.html", books=books, page_titel="All Books")


@app.route("/cart")
def cart():
    cart = session.get("cart", [])
    return render_template("cart.html", cart=cart)


@app.route("/login")
def login():
    session["logged_in"] = True
    return redirect(request.referrer or url_for("index"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))




if __name__ == "__main__":
    app.run(debug=True, port=5000)