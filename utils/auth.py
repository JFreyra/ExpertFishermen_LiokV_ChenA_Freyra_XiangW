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
    db = sqlite3.connect("/data/potato.db")
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
    db = sqlite3.connect("/data/potato.db")
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
            q = "SELECT password FROM user WHERE username = \"%s\"" % (username)
            c.execute(q)
            passw = c.fetchall()[0][0]

            if (myHashObj.hexdigest() == passw):
                db.close()
                return True
            
    db.close()
    return False


'''
special checks if there are any characters that will break code in a string
'''
def special(user):
    return any((ord(char)<48 \
                or (ord(char)>57 and  ord(char)<65) \
                or (ord(char)>90 and ord(char)<97) \
                or ord(char)>123) for char in user)


'''
getUserId returns the numerical id of a username in the database
'''
def getUserId(username):
    # connect to database
    db = sqlite3.connect("../data/potato.db")
    c = db.cursor()

    #find numerical id
    q = "SELECT id FROM user where username = \"%s\"" % (username)
    c.execute(q)
    
    result = c.fetchall()[0][0]

    return result
    
