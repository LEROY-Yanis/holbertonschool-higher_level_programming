#!/usr/bin/python3
"""Script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py username password database_name
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        pass
    # Connect to the MySQL database
    db = MySQLdb.connect(
        port=3306,
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    # Create a cursor object
    cursor = db.cursor()
    # Execute the SQL query to fetch states with names starting with 'N'
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    # Fetch all results
    query_rows = cursor.fetchall()
    # Print each row (state)
    for row in query_rows:
        print(row)
    # Close the cursor and database connection
    cursor.close()
    db.close()

