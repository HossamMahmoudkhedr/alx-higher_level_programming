#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of hbtn_0e_0_usa 
where name matches the argument.
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    connect to the database and get the data
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
    )

    db_cursor = db_connect.cursor()

    db_cursor.execute('SELECT * FROM states WHERE name={}', format(argv[4]))

    states = db_cursor.fetchall()

    for state in states:
        print(state)
