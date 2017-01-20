import hashlib, sqlite3, string


def addUser(user, full_name, email, password):
    if (special(user)):
        return "invlaid character in username"
    if (len(password)<8):
        return "password too short"
    db=sqlite3.connect('data/potato.db')
    c=db.cursor()
    myHashObj=hashlib.sha1()
    myHashObj.update(password)
    q='SELECT username FROM user'
    c.execute(q)
    userInfo=c.fetchall()
    for data in userInfo:
        if (user in data):
            db.close()
            return "ERROR: username already in use"
    q='SELECT email FROM user'
    c.execute(q)
    emailInfo=c.fetchall()
    for data in emailInfo:
        if (email in data):
            db.close()
            return "ERROR: email already in use"

    q="SELECT id FROM user"
    c.execute(q)
    userInfo=c.fetchall()
    print userInfo
    if len(userInfo) == 0:
        userID = 0
    else:
        userID = userInfo[-1][0] + 1
    q="INSERT INTO user VALUES ("+str(userID)+", \""+user+'\",\"'+full_name+'\",\"'+email+'\",\"'+myHashObj.hexdigest()+'\")'
    c.execute(q)
    db.commit()
    db.close()
    return "registration successful, enter user and pass to login"

def userLogin(user, password):
    db=sqlite3.connect('data/potato.db')
    c=db.cursor()
    myHashObj=hashlib.sha1()
    myHashObj.update(password)
    q='SELECT username FROM user'
    c.execute(q)
    data=c.fetchall()
    for stuff in data:
        if(user in stuff):
            q='SELECT password FROM user WHERE username = "'+user+'";'
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
    return any((ord(char)<48 or (ord(char)>57 and ord(char)<65) or (ord(char)>90 and ord(char)<97) or ord(char)>123) for char in user)
