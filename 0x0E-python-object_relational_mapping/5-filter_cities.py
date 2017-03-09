#!/usr/bin/python3
"""
Take the name of a state and list al cities of that state.
"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    injclean = "{}".format(sys.argv[4].split()[0])
    cur.execute("""SELECT cities.name, states.name FROM cities
                INNER JOIN states ON states.id=cities.state_id
                WHERE states.name="{}"
                ORDER BY cities.id ASC""".format(injclean))
    rows = cur.fetchall()
    print("{}".format(", ".join([row[0] for row in rows])))
