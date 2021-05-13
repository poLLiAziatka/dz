import sqlite3

conn = sqlite3.connect("C:\ProgramPoli\SQLiteStudio-3.2.1\lib")

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM Library")
    rows = cur.fetchall()

    for row in rows:
        print(row)

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM Book")
    rows = cur.fetchall()

    for row in rows:
        print(row)