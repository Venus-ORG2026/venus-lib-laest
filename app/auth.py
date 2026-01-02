import sqlite3
import hashlib

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def login_user(email, password):
    conn = sqlite3.connect("venus.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT password FROM users WHERE email=?",
        (email,)
    )
    row = cur.fetchone()
    conn.close()

    if not row:
        return {"success": False}

    return {"success": row[0] == hash_pw(password)}

def register_user(email, password):
    conn = sqlite3.connect("venus.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users VALUES (?, ?)",
        (email, hash_pw(password))
    )
    conn.commit()
    conn.close()
    return {"success": True}
