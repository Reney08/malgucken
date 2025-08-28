import mariadb
import time

for attempt in range(10):
    try:
        conn = mariadb.connect(
            username='barbot',
            password='Keins123!',
            host='db',
            port=3306,
            database='BarbotDB'
        )
        print('Successfully connected to database')
        break
    except mariadb.Error as e:
        print(f'Versuch {attempt + 1}: Verbindung zur Datenbank fehlgeschlagen. Felder Sie {e}')
        time.sleep(2)
else:
    raise Exception('Could not connect to database')


cur = conn.cursor()

