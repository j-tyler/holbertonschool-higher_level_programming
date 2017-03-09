#!/usr/bin/python3
"""
lists all states starting with N
"""


import MySQLdb
import sys

db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()

cur.execute("SELECT id, name FROM states")
rows = cur.fetchall()
for row in rows:
    if (row[1][0] == 'N'):
        print("{}".format(row))
