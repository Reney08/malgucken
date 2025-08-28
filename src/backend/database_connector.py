import mariadb

conn = mariadb.connect(
    username='barbot',
    password='Keins123!',
    host='db',
    port=3306,
    database='BarbotDB'
)

cur = conn.cursor()

