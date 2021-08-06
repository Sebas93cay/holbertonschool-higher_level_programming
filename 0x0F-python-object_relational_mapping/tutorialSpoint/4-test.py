#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB")

cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '4000'"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname={}, lanme={}, age={}, income={}".format(
            fname, lname, age, sex, income))
except:
    print("Error")
db.close()
