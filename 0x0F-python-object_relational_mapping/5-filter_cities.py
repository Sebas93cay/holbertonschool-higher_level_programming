#!/usr/bin/python3
"""
In this module we list all cities from a state
"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(
        'localhost', sys.argv[1], sys.argv[2], sys.argv[3], port=3306)
    cursor = db.cursor()

    sql = """SELECT cities.name FROM cities WHERE cities.state_id IN
    (SELECT id FROM states WHERE states.name = \"{}\")""".format(sys.argv[4])

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(", ".join([a for (a,) in result]))

    except Exception as e:
        print(e)

    db.close()
