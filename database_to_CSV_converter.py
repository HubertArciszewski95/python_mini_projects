# print form file database.db those countries that have area grater than 2m
# and save them to CSV file
import sqlite3
import pandas

conn = sqlite3.connect("/Users/hubertarciszewski/Downloads/database.db")
cur = conn.cursor()

cur.execute("SELECT * FROM countries WHERE area > 2000000")
rows = cur.fetchall()
conn.close()

labels = ["Rank", "Country", "Area", "Population"]
df = pandas.DataFrame.from_records(rows, columns=labels)

df.to_csv("file1.csv", index=False)
