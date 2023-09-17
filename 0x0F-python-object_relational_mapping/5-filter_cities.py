#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connect = MySQLdb.connect(
        host='localhost', user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT cities.id, cities.name, states.name \
                      FROM cities JOIN states ON cities.state_id = states.id \
                      WHERE states.name = '{}';".format(argv[4]))

    cities = db_cursor.fetchall()

    print(', '.join([cities[1] for city in cities]))
