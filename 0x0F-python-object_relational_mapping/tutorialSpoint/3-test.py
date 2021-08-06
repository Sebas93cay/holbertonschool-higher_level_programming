#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB")

cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE,
SEX, INCOME) VALUES('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
