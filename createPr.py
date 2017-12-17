#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('test.db')
print ("Create successfully")

conn.execute('''CREATE TABLE Entries (
            id int NOT NULL,
            mac text NOT NULL,
            food bool,
            water bool,
            power bool,
            lat int NOT NULL,
            lon int NOT NULL,
            PRIMARY KEY (mac, lat, lon));''')

print ("Table created succccssfngurghotighotgb")

conn.close()
