import sqlite3

def storeTimer( userID, isLooped, workSec, restSec, longRestSec):
    db=sqlite3.connect("data/potato.db")
    c=db.cursor()
    q = "INSERT INTO timer VALUES (" + str(userID) + "," + str(isLooped) + "," + str(workSec) + "," + str(restSec) + "," + str(longRestSec) + ")"
    c.execute(q)
    db.commit()
    db.close()
    return True

def displayTimers( userID ):
    db=sqlite3.connect('data/potato.db')
    c=db.cursor()
    q = "SELECT is_looped,workSecs,restSecs,longRestSecs FROM timer WHERE user_id =" + str(userID)
    c.execute(q)
    timerInfo = c.fetchall()
    db.close()
    return timerInfo[0]

def deleteTimer( userID, isLooped, workSec, restSec, longRestSec ):
    db=sqlite3.connect("data/potato.db")
    c=db.cursor()
    q = "DELETE FROM timer WHERE user_id = " + str(userID) + " AND is_looped = " + str(isLooped) + " AND workSecs = " + str(workSec) + " AND restSecs = " + str(restSec) + " AND longRestSecs = " + str(longRestSec)
    c.execute(q)
    db.commit()
    db.close()
    return True

'''
print displayTimers( 1 )
this returns ( isLooped, workSecs, restSecs, longRestSecs )
for example ( 0, 1234, 12, 123 )
'''
