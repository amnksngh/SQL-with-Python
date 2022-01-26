import sqlite3

conn = sqlite3.connect("Database/Training.db")
c = conn.cursor()

# UPDATE tablename SET  column1 = values1, ..., columnN = valuesN
# WHERE condition

# c.execute("UPDATE iceCubeMelting SET date = '26-01-2022'"+
#           " WHERE date IS NULL")

# c.execute("UPDATE iceCubeMelting SET date = '27-01-2022',"+
#           " temperature = 26.5 WHERE time > 6")


# DELETE FROM tablename WHERE condition
c.execute("DELETE FROM iceCubeMelting WHERE time < 5")

# DELETE FROM tablename
c.execute("DELETE FROM iceCubeMelting")

conn.commit()
c.close()
conn.close()
