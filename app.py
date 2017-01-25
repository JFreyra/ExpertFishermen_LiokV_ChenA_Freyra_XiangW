from flask import Flask, render_template, url_for, request, redirect, session, flash
from utils import flaskUtils, auth, spotify

def redirect_url():
    return request.referrer or url_for("index")

app = Flask(__name__)
app.secret_key = "abcdefghijklmnopqrstuvwxyz"

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

        if isValidLogin(username, password):
            user_id = getUserID(username)
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
        username = request.form.get("username")
        password = request.form.get("password")
        name_first = request.form.get("firstname")
        name_last = request.form.get("lastname")

        if isValidRegister(username, password):
            addUser(username, password)
            
            user_id = getUserID(username)
            session["user_id"] = user_id

            flash('Registration successful!', 'success')

            return redirect('/')
        
        else:
            flash('Registration unsuccessful! Username probably already exists!', 'error')
            return render_template("register.html")


@app.route('/todo')
#Frontend sends AJAX request (POST) to /todo every time todo list changed
def todo( methods=['POST'] ):
    return request.args.get('')

    return ""


@app.route('/songs', methods=['GET','POST'])
def songs():
    song_list = spotify.keywordSearch(request.form.get("artist"), request.form.get("track"))
    print song_list
    return render_template("songs.html") #need to pass song_list to jinja 

@app.route('/logout')
def logout():
    if "user_id" in session:
        session.pop("user_id")
    else:
        flash('Not logged in yet!', 'error')
    return redirect(flaskUtils.redirect_url())


if __name__ == "__main__":
    app.run( debug=True );
