#!/usr/bin/python3
"""
displays states matching given argument in database
"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print("{}".format(row))
