import sqlite3

#add task one at a time
def addTask( user_id, name, position ):
    db=sqlite3.connect("data/potato.db")
    c=db.cursor()
    q = "SELECT id FROM task"
    c.execute(q)
    infoid = c.fetchall()
    if len(infoid) == 0:
        lengthid = 0
    else:
        lengthid = len(infoid)
    if position > lengthid or position < 0:
        db.close()
        return False
    times = lengthid - position
    counter = lengthid - 1
    num = 0
    while num < times:
        q = "UPDATE task SET id = " + str(counter+1) + ", next_task_id = " + str(counter+2) + " WHERE id = " + str(counter)
        c.execute(q)
        counter-=1
        num+=1
    q = "INSERT INTO task VALUES( " + str(position) + ", " + str(user_id) + ", \"" + name + "\", " + str(position+1) + ")"
    c.execute(q)
    db.commit()
    db.close()
    return True

#delete task one at a time
def deleteTask( user_id, position ):
    db=sqlite3.connect("data/potato.db")
    c=db.cursor()
    q = "DELETE FROM task WHERE id = " + str(position) + " AND user_id = " + str(user_id)
    c.execute(q)
    q = "SELECT id FROM task"
    c.execute(q)
    infoid = c.fetchall()
    if len(infoid) == 0:
        lengthid = 0
    else:
        lengthid = len(infoid)
    times = lengthid - position
    counter = position
    num = 0
    while num < times:
        q = "UPDATE task SET id = " + str(counter) + ", next_task_id = " + str(counter+1) + " WHERE id = " + str(counter+1)
        c.execute(q)
        counter+=1
        num+=1
    db.commit()
    db.close()
    return True

#add and delete multiple tasks all at once
def saveTasks( user_id, listTasks ):
    db=sqlite3.connect("data/potato.db")
    c=db.cursor()
    q = "DELETE FROM task WHERE user_id = " + str(user_id)
    c.execute(q)
    counter = 0
    for task in listTasks:
        q = "INSERT INTO task VALUES( " + str(counter) + ", " + str(user_id) + ", \"" + task + "\", " + str(counter+1) + ")"
        c.execute(q)
        counter+=1
    db.commit()
    db.close()
    return True

#returns a list of tasks
def getTasks( user_id ):
    db=sqlite3.connect("data/potato.db")
    c=db.cursor()
    q = "SELECT name FROM task WHERE user_id = " + str(user_id)
    c.execute(q)
    listTasks = c.fetchall()
    newList = []
    for task in listTasks:
        newList.append( task[0] )
    db.close()
    return newList
