from database_connector import conn

def get_user_by_username(username: str):
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cur.fetchone()
    cur.close()
    return user

def safe_login_data(username: str, password: str, checkbox: bool):
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password, agb_accepted) VALUES (?, ?, ?)", (username, password, checkbox))
    conn.commit()
    cur.close()


def get_cocktails():
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT Name FROM Cocktail WHERE verfuegbar = 1")
    cocktails = cur.fetchall()
    cur.close()
    return cocktails

def get_cocktail_by_name(name):
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Cocktail WHERE Name = ?", (name,))
    row = cur.fetchone()
    cur.close()
    return row

def get_ingredients_for_cocktail(cocktail_name: str):
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT Z.Name AS Zutat, R.Menge AS Menge
        FROM Rezept R
        JOIN Cocktail C ON C.CocktailID = R.CocktailID
        JOIN Zutat Z ON Z.ZutatID = R.ZutatID
        WHERE C.Name = ?
        ORDER BY R.RezeptPos ASC
    """, (cocktail_name,))
    zutaten = cur.fetchall()
    cur.close()
    return zutaten

def get_pumps_from_db():
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT Z.Name, Z.ZutatID, Z.Zapfstelle, Z.Alkohol, ZS.PumpenNR
        FROM Zutat Z
        JOIN Zapfstelle ZS ON Z.Zapfstelle = ZS.ZapfstelleID
        WHERE ZS.Pumpe = 1
    """)
    pumps = cur.fetchall()
    cur.close()
    result = {}
    for p in pumps:
        result[p["ZutatID"]] = {
            "liquid": p["Name"],
            "zutat_id": p["ZutatID"],
            "pwm_channel": p["PumpenNR"],
            "alkohol": p["Alkohol"]
        }
    return result

def get_servo_positions_from_db():
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT Z.Name, Z.ZutatID, Z.Zapfstelle, ZS.SchienenPos
        FROM Zutat Z
        JOIN Zapfstelle ZS ON Z.Zapfstelle = ZS.ZapfstelleID
        WHERE ZS.Pumpe = 0
    """)
    positions = cur.fetchall()
    cur.close()
    result = {}
    for p in positions:
        result[p["ZutatID"]] = {
            "liquid": p["Name"],
            "zutat_id": p["ZutatID"],
            "use": "servo",
            "steps": (p["SchienenPos"])  # Example mapping, adjust as needed!
        }
    return result

def get_station_positions():
    """
    Fetch Zapfstelle information (SchienenPos and PumpenNR) and map them to logical names.
    Returns a dictionary where keys are 'pump_<channel>' or 'outlet', values are step positions.
    """
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Zapfstelle")
    data = cur.fetchall()
    cur.close()

    station_positions = {}

    for row in data:
        pos = row['SchienenPos']  # Convert logical slot to steps (e.g. 1 → 1000)

        if row['Pumpe']:  # Pumpe == 1 => Pump station
            pump_channel = row['PumpenNR']
            if pump_channel:
                station_positions[f'pump_{pump_channel}'] = pos
        else:
            # Assume one outlet only in SchienenPos where Pumpe = 0
            station_positions['outlet'] = pos

    return station_positions


def get_all_zapfstellen():
    """
    get all Zapfstelle information (SchienenPos and PumpenNR) safed in Database
    """
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Zapfstelle")
    data = cur.fetchall()
    cur.close()
    return data

def get_single_zapfstelle(id: int):
    """
    get single instance of Zapfstelle
    """
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM ZapfstelleID WHERE = ? LIMIT 1", (id,))
    data = cur.fetchone()
    cur.close()
    return data