import sqlite3

# open("Path", "r")
# text in file
conn = sqlite3.connect("Training.db")

c = conn.cursor()

# open("PATH", "r")
c.execute("SELECT time FROM iceCubeMelting")

# f.readline()
result = c.fetchone()
print(result)

result = c.fetchmany(size = 5)
print(result)

# f.read()
result = c.fetchall()
print(result)

# conn.commit()
c.close()
conn.close()
