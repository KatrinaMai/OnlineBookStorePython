from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import query_db, execute_db, init_db

app = Flask(__name__)

# Required for Flask sessions and flash messages.
app.config["SECRET_KEY"] = "online-bookstore"

# Makes login status and cart count available to every HTML page
@app.context_processor
def inject_global():
    return {
        "logged_in": "customer_id" in session,
        "current_username": session.get("username"),
        "cart_count": len(session.get("cart", []))
    }


@app.route("/")
def index():
    allBooks = query_db("SELECT * FROM Book")
    return render_template("index.html", books=allBooks)


@app.route("/cart")
def cart():
    cart_item = session.get("cart", [])
    return render_template("cart.html", cart=cart_item)


@app.route("/logout")
def logout():
    session.clear()
    flash("You're signed out. See you next time!", "error")
    return redirect(url_for("index"))


# Display the login page and processes login submissions.
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        customer = query_db(
            "SELECT * FROM Customer WHERE username = ?",
            (username,), one=True
        )

        if customer and customer["password"] == password:
            session["customer_id"] = customer["customerID"]
            session["username"] = customer["username"]
            return redirect(url_for("account"))
        
    return render_template("login.html")

# Displays the create-account page and processes registration.
@app.route("/create-account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        first_name = request.form["firstName"].strip()
        last_name = request.form["lastName"].strip()

        if not username or not password or not first_name or not last_name:
            flash("All fields are required.", "error")
            return render_template("create_account.html")

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return render_template("create_account.html")

        existing_customer = query_db(
            "SELECT customerID FROM Customer WHERE username = ?",
            (username,), one=True
        )

        if existing_customer:
            flash("That username is already in use.", "error")
            return render_template("create_account.html")

        # Insert a new customer into the database
        execute_db(
            """
            INSERT INTO Customer
            (username, password, firstName, lastName, type)
            VALUES (?, ?, ?, ?, ?)
            """,
            (username, password, first_name, last_name, "customer")
        )

        flash("Account created successfully. You can now log in.", "success")
        return redirect(url_for("login"))

    return render_template("create_account.html")

# Displays the logged-in user's account page.
@app.route("/account")
def account():

    # If the user is not logged in, ask them to login
    if "customer_id" not in session:
        flash("Please log in to view your account.", "error")
        return redirect(url_for("login"))

    # Retrieve the current user's information.
    customer = query_db(
        """
        SELECT *
        FROM Customer
        WHERE customerID = ?
        """,
        (session["customer_id"],), one=True
    )

    if customer is None:
        session.clear()
        return redirect(url_for("login"))

    return render_template(
        "account.html",
        customer=customer
    )




if __name__ == "__main__":
    app.run(debug=True, port=5000)