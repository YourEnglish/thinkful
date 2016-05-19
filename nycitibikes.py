import pandas as pd
import statsmodels.api as sm
from pandas.io.json import json_normalize
import requests
import sqlite3 as lite


# not only json, also beautifulsoup
r = requests.get('http://www.citibikenyc.com/stations/json')

# json vs python dictionary
key_list = [] #unique list of keys for each station listing
for station in r.json()['stationBeanList']:
    for k in station.keys():
        if k not in key_list:
            key_list.append(k)

# go from nested structure to table structure
df = json_normalize(r.json()['stationBeanList'])


con = lite.connect('citi_bike13.db')
cur = con.cursor()

with con:
    #cur.execute('DROP TABLE citibike_reference') 
    # also look at possibility if exist function
	cur.execute('CREATE TABLE citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT )')

#a prepared SQL statement we're going to execute over and over again
sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

#for loop to populate values in the database
with con:
    for station in r.json()['stationBeanList']:
        #id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location)
        cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))

#extract the column from the DataFrame and put them into a list
station_ids = df['id'].tolist() 

#add the '_' to the station name and also add the data type for SQLite
station_ids = ['_' + str(x) + ' INT' for x in station_ids]


#create the table
#in this case, we're concatenating the string and joining all the station ids (now with '_' and 'INT' added)
with con:
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")

n = 0

while n < 60:

	#take the string and parse it into a Python datetime object
	exec_time = parse(r.json()['executionTime'])

	with con:
	    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))

	id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station

	#loop through the stations in the station list
	for station in r.json()['stationBeanList']:
	    id_bikes[station['id']] = station['availableBikes']

	#iterate through the defaultdict to update the values in the database
	with con:
	    for k, v in id_bikes.iteritems():
	        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")

	n += 1
	# Committing changes and closing the connection to the database file
	time.sleep(60)
	con.commit()
	con.close()
	r = requests.get('http://www.citibikenyc.com/stations/json')
	df = json_normalize(r.json()['stationBeanList'])
	con = lite.connect('citi_bike13.db')
	cur = con.cursor()

# unique method and describe method!!

	

