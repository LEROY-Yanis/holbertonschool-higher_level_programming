#!/usr/bin/env python3
"""Script that takes a state name and displays matching states."""

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
    query = (
        "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(
            sys.argv[4]
        )
    )
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()