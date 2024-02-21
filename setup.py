import psycopg2


conn = psycopg2.connect(dbname='postgres', host='127.0.0.1')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, pass TEXT)")
cur.execute("INSERT INTO users (name, pass) VALUES ('test', 'qweqwe')")
conn.commit()
cur.close()
conn.close()

