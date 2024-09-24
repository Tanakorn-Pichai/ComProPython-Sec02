import sqlite3

conn =sqlite3.connect('mydatabase.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users 
            (id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             age  INTEGER NOT NULL,
            city TEXT  NOT NULL)''')

cur.execute("INSERT INTO  users (name, age, city) VALUES ('John', 25, 'New York')")
cur.execute("INSERT INTO  users (name, age, city) VALUES ('Tanakorn', 30, 'Thai')")
cur.execute("INSERT INTO  users (name, age, city) VALUES ('Bob', 35, 'Bkk')")

conn.commit()

cur.execute("SELECT * FROM users WHERE age >28")
result = cur.fetchall()
print("User age > 28")
for row in result:
    print(f"ID:{row[0]},Name:{row[1]},Age:{row[2]},City:{row[3]}")
conn.close()
