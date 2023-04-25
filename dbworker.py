import sqlite3
import pickle

db = "horoscope.db"


def initialize_user(user_id, horoscope):
    try:
        command = "INSERT INTO users VALUES(?, ?)"
        sqlite_db = sqlite3.connect(db)
        cur = sqlite_db.cursor()
        cur.execute(command, (str(user_id), str(horoscope)))
        sqlite_db.commit()
        sqlite_db.close()
    except Exception as e:
        pass


def check_user_exist(user_id):
    user_list_command = "SELECT UserID from users"
    sqlite_db = sqlite3.connect(db)
    cur = sqlite_db.cursor()
    cur.execute(user_list_command)
    users = cur.fetchall()
    user_list = []

    for user in users:
        user_list.append(user[0])

    if str(user_id) in user_list:
        return True
    else:
        return False


def get_horoscope(user_id):
    command = "SELECT Horoscope from users WHERE UserID = {}".format(user_id)
    sqlite_db = sqlite3.connect(db)
    cur = sqlite_db.cursor()
    cur.execute(command)
    horoscope = cur.fetchall()
    return horoscope[0][0]


def add_to_subscribers(user_id, messageobject):
    command = "INSERT INTO subscribers VALUES(?, ?)"
    sqlite_db = sqlite3.connect(db)
    cur = sqlite_db.cursor()
    cur.execute(command, (str(user_id), sqlite3.Binary(messageobject)))
    sqlite_db.commit()
    sqlite_db.close()


def get_all_subscribers():
    command = "SELECT messageobj from subscribers"
    sqlite_db = sqlite3.connect(db)
    cur = sqlite_db.cursor()
    cur.execute(command)
    subscribers = cur.fetchall()
    list_of_subscriber = []
    for subscriber in subscribers:
        data = pickle.loads(subscriber[0])
        list_of_subscriber.append(data)
    return list_of_subscriber


def remove_subscriber(user_id):
    command = "DELETE from subscribers WHERE UserID = {}".format(user_id)
    sqlite_db = sqlite3.connect(db)
    cur = sqlite_db.cursor()
    cur.execute(command)
    sqlite_db.commit()
    sqlite_db.close()


def change_db_horoscope(user_id, horoscope):
    command = "UPDATE users SET Horoscope = ? WHERE UserID = ?"
    sqlite_db = sqlite3.connect(db)
    cur = sqlite_db.cursor()
    cur.execute(command, (str(horoscope), str(user_id)))
    sqlite_db.commit()
    sqlite_db.close()