#!/usr/bin/python3
"""
In this module we list all cities
"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(
        'localhost', sys.argv[1], sys.argv[2], sys.argv[3], port=3306)
    cursor = db.cursor()

    sql = """SELECT cities.id, cities.name, states.name FROM cities
    LEFT JOIN states ON cities.state_id = states.id"""

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for state in result:
            print(state)

    except Exception as e:
        print(e)

    db.close()
