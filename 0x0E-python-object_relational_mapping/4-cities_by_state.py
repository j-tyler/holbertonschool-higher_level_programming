#!/usr/bin/python3
"""
lists all states starting with N
"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT states.id, cities.name, states.name
                FROM states, cities ORDER BY cities.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
