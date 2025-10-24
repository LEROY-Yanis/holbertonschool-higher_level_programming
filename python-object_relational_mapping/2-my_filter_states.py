#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
WARNING: This script is vulnerable to SQL injection as requested by the task.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        pass

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name = '{}'" \
            " ORDER BY id ASC".format(state_name)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

