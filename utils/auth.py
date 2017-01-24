import hashlib, sqlite3, string

'''
isValidRegister returns:
False if user was not successfully registered
True if the user was successfully registered
'''
def isValidRegister(username, password, confirm):
    if (special(user) or len(password) > 8):
        return False

    #connect to database
    db = sqlite3.connect("data/potato.db")
    c = db.cursor()

    #hash password
    myHashObj = hashlib.sha1()
    myHashObj.update(password)

    #get all registered usernames
    q = "SELECT username FROM user"
    c.execute(q)
    user_list = c.fetchall()

    #determine if username is already registered
    for user in user_list:
        if (user_name in user):
            db.close()
            return False

    return True

'''
addUser adds user into database
'''
def addUser(username, password):
    #connect to database
    db = sqlite3.connect("data/potato.db")
    c = db.cursor()

    #hash password
    myHashObj = hashlib.sha1()
    myHashObj.update(password)

    #register user in database
    q="INSERT INTO user(username, password) VALUES (\"%s\", \"%s\")" % (username, myHashObj.hexdigest())
    c.execute(q)

    #save changes
    db.commit()
    db.close()

'''
isValidLogin returns:
False if the login is unsuccessful
True if the login is successful 
'''
def userLogin(username, password):
    #connect to database
    db = sqlite3.connect("data/potato.db")
    c = db.cursor()

    #hash password
    myHashObj=hashlib.sha1()
    myHashObj.update(password)

    #validate credentials
    q = "SELECT username FROM user"
    c.execute(q)
    user_list = c.fetchall()
    for user in user_list:
        if (username in user):
            q="SELECT password FROM user WHERE username = \"%s\""
            c.execute(q)
            password=c.fetchall()
            q='SELECT username From user WHERE username = "'+user+'";'
            c.execute(q)
            stuff=c.fetchall()
            db.close()
            if(myHashObj.hexdigest()==password[0][0]):
                return ['True', str(stuff[0][0])]
    db.close()
    return ['False', 'bad user/pass']

def special(user):
    return any((ord(char)<48 \
                or (ord(char)>57 and  ord(char)<65) \
                or (ord(char)>90 and ord(char)<97) \
                or ord(char)>123) for char in user)
