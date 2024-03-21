import sqlite3

myBase = "mybase.db"


def connexion():
    conn = sqlite3.connect(myBase)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                    username  TEXT,
                    telephone TEXT,
                    email     TEXT,
                    password  TEXT)""")
    conn.commit()
    conn.close()


def new_user(username, telephone, email, password):
    conn = sqlite3.connect(myBase)
    cur = conn.cursor()
    cur.execute("""INSERT INTO users values (?,?,?,?)""", (username, telephone, email, password))
    conn.commit()
    conn.close()


def all_users():
    conn = sqlite3.connect(myBase)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    r = cur.fetchall()
    conn.commit()
    conn.close()
    return r


connexion()

for user in all_users():
    print(user)
