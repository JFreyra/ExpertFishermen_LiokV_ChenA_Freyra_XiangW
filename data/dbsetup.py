import sqlite3

def createTables():
    db=sqlite3.connect("potato.db")
    c=db.cursor()
    q = "CREATE TABLE user(id integer PRIMARY KEY, username varchar(64), password varchar(64));"
    c.execute(q)
    q = "CREATE TABLE timer (user_id integer NOT NULL, is_looped boolean NOT NULL, workSecs integer NOT NULL, restSecs integer NOT NULL, longRestSecs integer NOT NULL);"
    c.execute(q)
    q = "CREATE TABLE task (id integer NOT NULL CONSTRAINT task_pk PRIMARY KEY, user_id integer NOT NULL, name varchar(255) NOT NULL, next_task_id integer);"
    c.execute(q)
    db.commit()
    db.close()
    return True
