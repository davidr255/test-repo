


import sqlite3 # this is a module in python.

# hit help(sqlite3) to get manual

# Create connection object
# Create cursor object
# To do so, need to connect to database first

# connection = sqlite3.connect('example.db', check_same_thread=False)
# check_same_thread = False. written in C laguage. could have diff opeation op at diff times

# help(sqlite3.connect) will give documentation

# cursor = connection.cursor()  paranthese to invoke
# print(type(sqlite3.cursor))  will show you that its is a class called Cursor



# create cursor object, connection object and table object
# cursor.execute('CREATE 

# cursor.execute('CREATE TABLE users(pk INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR);')
# sqlite3 example.db
# .schema
# pk global unique id for every row. so you can't mess with. ordered over time
#    pk is 


# in sqlite repl
#.mode columns
# .headers on   modifying shell for output
# SELECT * FROM users;     
# INTEGER PRIMARY KEY=. Automating far right column
# create custom index. rank ppl for a particular read
# INSERT INTO users(username) VALUES('kenso');     
#	 doing write inside sql repl
#       Write operation
# SELECT * FROM USERS	
# need to create cursor object before can wrap in python


# .q will quit




