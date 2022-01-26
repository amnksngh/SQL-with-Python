import sqlite3

# open("Path", "r")
# text in file
conn = sqlite3.connect("Database/Training.db")

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT PRIMARY KEY," +
          "temperature REAL, date TEXT)")

# DROP TABLE table_name
c.execute("DROP TABLE iceCubeMelting")

# conn.commit()
c.close()
conn.close()
