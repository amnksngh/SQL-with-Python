import sqlite3

conn = sqlite3.connect("Database/Training.db")
c = conn.cursor()

c.execute("DROP TABLE iceCubeMelting")

c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT PRIMARY KEY," +
          "temperature REAL, date TEXT)")

# INSERT INTO tablename VALUES (value1, value2, value3, ...)
c.execute("INSERT INTO iceCubeMelting VALUES" +
          " (0, 27.0, '26-01-2022')")


# INSERT INTO tablename (column1, column2, ..., columnN) VALUES
# (?, ?, ..., ?)(value1, value2, ..., valueN)

for i in range(1, 5):
    c.execute("INSERT INTO iceCubeMelting (time, temperature, date)"+
              " Values (?, ?, ?)", (i, 27-0.1*i, "26-01-2022"))

for i in range(5, 8):
    c.execute("INSERT INTO iceCubeMelting (time, temperature)"+
              " Values (?, ?)", (i, 27-0.1*i))


for i in range(8, 10):
    c.execute("INSERT INTO iceCubeMelting (temperature, time)"+
              " Values (?, ?)", (27-0.1*i, i))

conn.commit()

c.close()
conn.close()
