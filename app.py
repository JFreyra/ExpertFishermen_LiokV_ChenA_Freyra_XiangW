from flask import Flask, render_template, url_for, request, redirect, session
from utils import flaskUtils

def redirect_url():
    return request.referrer or url_for("index")

app = Flask(__name__)
app.secret_key = "abcdefghijklmnopqrstuvwxyz"

@app.route('/')
def index():
    return "kek"


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else: #assert method is POST
        # do verification stuff
        pass
    
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else: #assert method is POST
        # do verification stuff
        pass
        

@app.route('/logout')
def logout():
    if "user_id" in session:
        session.pop("user_id")
    return flaskUtils.redirect_url() 
    
if __name__ == "__main__":
    app.run( debug=True );
