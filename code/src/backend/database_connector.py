import mariadb

conn = mariadb.connect(
    username='barbot',
    password='Keins123!',
    host='127.0.0.1',
    port=3306,
    database='BarbotDB'
)

cur = conn.cursor()

