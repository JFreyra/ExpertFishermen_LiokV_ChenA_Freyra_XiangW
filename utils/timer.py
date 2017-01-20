import sqlite3

def storeTimers( userID, isLooped, workSec, restSec, longRestSec ):
    q = "INSERT INTO timer VALUES (" + str(userID) + "," + str(isLooped) + "," + str(workSec) + "," + str(restSec) + "," + str(longRestSec) + ")"
    c.execute(q)
    db.commit()
    db.close()
    return True

def displayTimers( userID ):
    db=sqlite3.connect('../data/potato.db')
    c=db.cursor()
    q = "SELECT is_looped,workSecs,restSecs,longRestSecs FROM timer WHERE user_id =" + str(userID)
    c.execute(q)
    timerInfo = c.fetchall()
    return timerInfo

print displayTimers( 0 )
    
