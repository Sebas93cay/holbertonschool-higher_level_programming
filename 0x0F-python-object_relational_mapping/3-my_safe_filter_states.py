#!/usr/bin/python3
"""
In this module we avoid SQLs injections
"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(
        'localhost', sys.argv[1], sys.argv[2], sys.argv[3], port=3306)
    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name = \"{}\"".format(sys.argv[4])

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for state in result:
            print(state)

    except Exception as e:
        print(e)

    db.close()
