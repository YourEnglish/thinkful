import sqlite3 as lite
import pandas as pd

cities = (('Las Vegas', 'NV'), ('Atlanta', 'GA'), ('Los Angeles', 'CA'), ('San Francisco', 'CA'))
weather = (('Las Vegas', 2016, 'July', 'January', 74), ('Atlanta', 2016, 'July', 'December', 64), ('Los Angeles', 2016, 'August', 'January', 85), ('San Francisco', 2016, 'July', 'January', 78))
con = lite.connect('getting_started.db')

# Inserting rows by passing values directly to `execute()`
with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("DROP TABLE IF EXISTS weather")
	cur.execute("CREATE TABLE cities (name text, state text)")
	cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
	cur.executemany("INSERT INTO cities VALUES(?, ?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?, ?, ?, ?, ?)", weather)
	cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON city=name WHERE warm_month='July'")
	
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows)

	print df
#	print "The cities that are warmest in July are: " + df[0][0] + ", " + df[1][0] + ", " + df[0][1] + ", " + df[1][1] + ", " + df[0][2] + ", " + df[1][2]   
	
	print "The cities that are warmest in July are: ",

	for index, row in df.iterrows():
		print row[0] + ", " + row[1] + ", ",





