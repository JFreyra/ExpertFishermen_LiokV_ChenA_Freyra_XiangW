from flask import Flask, render_template, url_for, request, redirect, session, flash
from utils import flaskUtils, auth, spotify, timerUtils
import json

def redirect_url():
    return request.referrer or url_for("index")

app = Flask(__name__)
app.secret_key = "abcdefghijklmnopqrstuvwxyzcompletelyunguessablekeybois"

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/timer')
def timer():
    return render_template("timer.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else: #assert method is POST
        username = request.form.get("username")
        password = request.form.get("password")
        print username
        print password
        if auth.userLogin(username, password):
            user_id = auth.getUserId(username)
            session["user_id"] = user_id

            flash('Login successful!', 'success')
            print "login successful"
            return redirect('/')
        
        else:
            flash("Login unsuccessful! Please create an account if you haven't already!", 'error')
            print "login unsuccessful"
            return render_template("login.html")

        
@app.route('/saveCustomTimer', methods=['POST'])
def saveCustomTimer():
    if "user_id" in session:
        try:
            work_mins = int(request.form.get("work_mins"))
            work_secs_total = (work_mins * 60) + int(request.form.get("work_secs"))
            rest_mins = int(request.form.get("rest_mins"))
            rest_secs_total = (rest_mins * 60) + int(request.form.get("rest_secs"))
        except:
            return "Make sure you only enter numbers for times! Go back and try again!"
        timerUtils.storeTimer(session["user_id"], 0, work_secs_total, rest_secs_total, 0)
        
        #put in timer format
        intervals = [
            {
                "name": "work",
                "startTime": work_secs_total,
                "curTime": work_secs_total
            },
            {
                "name":"break",
                "startTime": rest_secs_total,
                "curTime": rest_secs_total
            }
        ]
        print intervals
        session["intervals"] = json.dumps(intervals)
        session["custom"] = True
    return redirect( url_for("timer") )
        
    
    
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")

    else: #assert method is POST
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        if auth.isValidRegister(username, password, confirm):
            auth.addUser(username, password)
            
            user_id = auth.getUserId(username)
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


@app.route('/songform')
def songform():
    return render_template("songsinit.html")


@app.route('/songs', methods=['POST'])
def songs():
    title = request.form.get("title")
    artist = request.form.get("artist")
    print title
    print artist
    if (not artist and not title):
        return render_template("songsinit.html", message="Please enter either an artist or a title!")
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
    if "custom" in session:
        session.pop("custom", None)
    if "user_id" in session:
        session.pop("user_id", None)
    else:
        flash('Not logged in yet!', 'error')
    return redirect(flaskUtils.redirect_url())


if __name__ == "__main__":
    app.run( debug=True );
