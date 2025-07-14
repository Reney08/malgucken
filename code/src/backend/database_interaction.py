from database_connector import conn

def safe_login_data(username, password, checkbox):
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password, agb_accepted) VALUES (?, ?, ?)", (username, password, checkbox))
    conn.commit()
    cur.close()

def get_user_by_username(username):
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cur.fetchone()
    cur.close()
    return user

def get_cocktails():
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT Name FROM Cocktail WHERE verfuegbar = 1")
    cocktails = cur.fetchall()
    cur.close()
    return cocktails
