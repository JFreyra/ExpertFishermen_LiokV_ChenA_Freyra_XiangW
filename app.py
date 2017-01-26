from flask import Flask, render_template, url_for, request, redirect, session, flash
from utils import flaskUtils, auth, spotify
import json

def redirect_url():
    return request.referrer or url_for("index")

app = Flask(__name__)
app.secret_key = "abcdefghijklmnopqrstuvwxyzcompletelyunguessablekeybois"

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else: #assert method is POST
        username = request.form.get("username")
        password = request.form.get("password")

        if auth.userLogin(username, password):
            user_id = auth.getUserID(username)
            session["user_id"] = user_id

            flash('Login successful!', 'success')

            return redirect('/')
        
        else:
            flash("Login unsuccessful! Please create an account if you haven't already!", 'error')

            return render_template("login.html")

    
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")

    else: #assert method is POST
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm"]
        print username
        print password
        print confirm

        if auth.isValidRegister(username, password, confirm):
            auth.addUser(username, password)
            print "user added"
            
            user_id = auth.getUserID(username)
            session["user_id"] = user_id

            flash('Registration successful!', 'success')

            return redirect('/')
        
        else:
            flash('Registration unsuccessful! Username probably already exists!', 'error')
            print "something went wrong"
            return render_template("register.html")


@app.route('/todo')
#Frontend sends AJAX request (POST) to /todo every time todo list changed
def todo( methods=['POST'] ):
    return request.args.get('')



@app.route('/songform')
def songform():
    return render_template("songsinit.html")


@app.route('/songs', methods=['POST'])
def songs():
    title = request.form["title"]
    artist = request.form["artist"]
    print title
    print artist
    song_list = spotify.keywordSearch(artist, title)
    print song_list
    return render_template("songs.html", songlist=song_list)


@app.route('/sessionPush', methods=['POST'])
def pushToSession():
    name = request.form.get("name")
    data = request.form.get("data")
    print "%s: %s" % (name, data)
    session[name] = data;
    return "" #idt it matters what i return

@app.route('/logout')
def logout():
    if "intervals" in session:
        session.pop("intervals", None)
    if "user_id" in session:
        session.pop("user_id", None)
    else:
        flash('Not logged in yet!', 'error')
    return redirect(flaskUtils.redirect_url())


if __name__ == "__main__":
    app.run( debug=True );
