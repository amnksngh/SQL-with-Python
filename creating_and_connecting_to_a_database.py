import sqlite3

# open("Path", "r")
# text in file
conn = sqlite3.connect("Training.db")

c = conn.cursor()

# f.write() or f.read()
c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT,"+ 
        "temperature REAL, date TEXT)")

conn.commit()
c.close()
conn.close()