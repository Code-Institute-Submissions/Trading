import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from index import rsi_dataframe as rsi
if os.path.exists("env2.py"):
    import env2


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.api_key = os.environ.get("api_key")

mongo = PyMongo(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#loads data page
@app.route("/base")
def base():
    tasks = mongo.db.tasks.find()
    return render_template("data.html", tasks=tasks)


#pulls data from mongo db
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.ohlc.find())
    return render_template("data.html", tasks=tasks)

#registers user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(register)

        #put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                #invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            #username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    #remove user from session cookies
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/stock", methods=["GET"])
def stock():
    stock_ticker = request.args['stockName']
    stock_data = rsi(stock_ticker)
    return render_template("data.html", stock_data=stock_data)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)