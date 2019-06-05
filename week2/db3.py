

import csv
import sqlite3

csvfile = 'employees.csv'

connection = sqlite3.connect('em.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS employees;')
cursor.execute('''CREATE TABLE employees (
	name VARCHR,
	cellphone VARCHAR,
	homephone VARCHAR,
	workphone VARCHAR,
	email VARCHAR,
	country VARCHAR
	);''')

with open(csvfile) as f:
	creader = csv.reader(f)
	next(creader)
	for row in creader:
		cursor.execute('INSERT INTO employees VALUES (?,?,?,?,?,?);',(row[0],row[1],row[2],row[3],row[4],row[5]))

connection.commit()
connection.close()


# row next()
