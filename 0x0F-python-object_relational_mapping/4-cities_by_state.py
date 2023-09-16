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

    db_cursor.execute('SELECT * FROM cities')

    cities = db_cursor.fetchall()

    for city in cities:
        print(city)
