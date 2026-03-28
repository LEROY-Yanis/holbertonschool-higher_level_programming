#!/usr/bin/python3
"""Script that safely takes a state name and displays matching states."""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
        (sys.argv[4],),
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
