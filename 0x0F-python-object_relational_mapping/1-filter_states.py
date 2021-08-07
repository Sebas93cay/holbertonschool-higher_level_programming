#!/usr/bin/python3
"""
This module selects all states that starts with N
"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    sql = """SELECT * FROM states WHERE name LIKE BINARY 'N%'
    ORDER BY states.id ASC"""
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for state in result:
            print(state)

    except Exception as e:
        print(e)

    db.close()
