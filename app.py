from flask import Flask, render_template, url_for, request, redirect, session
from utils import flaskUtils

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
        '''
        DB function needed: verifyLogin(username, password)
        * return 1 if username or password blank
        * return 2 if username doesn't exist
        * return 3 if username exists, put password incorrect
        * return 0 otherwise (login successful)
        '''
        if verifyLogin == 0:
            '''
            DB function needed: getUserID()
            * given username, get user ID
            '''
            #user_id = getUserID()
            #session["user_id"] = user_id
            return redirect('/')
        else:
            return "dere wuz a eror"

    
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else: #assert method is POST
        # do verification stuff
        pass


@app.route('/clock')
def cock():
    return kek
                

@app.route('/logout')
def logout():
    if "user_id" in session:
        session.pop("user_id")
    return redirect(flaskUtils.redirect_url())


if __name__ == "__main__":
    app.run( debug=True );
