import sqlite3

conn = sqlite3.connect("Database/Training.db")
c = conn.cursor()


#c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT PRIMARY KEY," +
#          "temperature REAL, date TEXT)")

# SELECT column1, ..., columnN FROM tablename
# c.execute("SELECT time, temperature, date FROM iceCubeMelting")


# SELECT * FROM tablename
# c.execute("SELECT * FROM iceCubeMelting")

# SELECT * FROM tablename LIMIT #NoRows OFFSET #Offset
# c.execute("SELECT * FROM iceCubeMelting LIMIT 2 OFFSET 3")

# SELECT * FROM tablename ORDER BY column1, column2, ..., columnN
# [ASC|DESC]
# c.execute("SELECT * FROM iceCubeMelting ORDER BY temperature DESC")

# SELECT DISTINCT column1, ..., columnN FROM tablename
c.execute("SELECT DISTINCT time, date, temperature FROM iceCubeMelting")
data = c.fetchall()
for piece in data:
    print(piece)

c.close()
conn.close()
