import sqlite3

conn = sqlite3.connect("Database/Training.db")
c = conn.cursor()


#c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT PRIMARY KEY," +
#          "temperature REAL, date TEXT)")

# SELECT column1, ..., columnN FROM tablename
# c.execute("SELECT time, temperature, date FROM iceCubeMelting")


# SELECT * FROM tablename
# c.execute("SELECT * FROM iceCubeMelting")

# SELECT * FROM tablename WHERE condition
# >, <, =, NOT
# c.execute("SELECT * FROM iceCubeMelting WHERE "+
#           "date = '26-01-2022'")
# c.execute("SELECT * FROM iceCubeMelting WHERE "+
#           "date IS NOT NULL")

# AND or OR
c.execute("SELECT * FROM iceCubeMelting WHERE "+
          "time < 5 OR temperature > 26.2")
data = c.fetchall()
for piece in data:
    print(piece)

c.close()
conn.close()
