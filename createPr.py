#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('test.db')
print ("Create successfully")

#id int AUTO_INCREMENT NOT NULL,
conn.execute('''CREATE TABLE Entries (
            mac text NOT NULL,
            food bool,
            water bool,
            power bool,
            lat int NOT NULL,
            lon int NOT NULL,
            PRIMARY KEY (mac, lat, lon));''')

print ("Table created succccssfngurghotighotgb")

conn.execute("INSERT INTO Entries (mac, food, water, power, lat, lon) \
        VALUES('00:00:00:00:00:00', 0, 0, 0, 123.45, 678.90);")

conn.execute("INSERT INTO Entries (mac, food, water, power, lat, lon) \
        VALUES('00:00:00:00:00:01', 1, 1, 1, 987.6, 543.21);")

conn.commit()
conn.close()
