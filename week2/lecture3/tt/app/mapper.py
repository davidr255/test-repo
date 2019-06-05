
import sqlite3

class Database:

	def __init__(self):
		print('inside __init__','self:',self)
		self.connection = sqlite3.connect('test.db')
		self.cursor = self.connection.cursor()

	def __enter__(self):
		print('inside __enter__','self:',self)
		return self

	def __exit__(self,type,value,traceback):
		print('inside __exit__','self:',self)
		if self.connection:
			print('inside self.connection')
			if self.cursor:
				print('inside self.cursor')
				self.connection.commit()
				self.cursor.close()
		self.connection.close()

if __name__ == '__main__':
	with Database() as d:
		print('inside of with block')
		# write a crate_table function
		# write a add_column function
		# create tables in an efficienct way
		# add columns in an eff way
		d.cursor.execute('DROP TABLE IF EXISTS stock_keeping_units;')
		d.cursor.execute(
			'''CREATE TABLE stock_keeping_units(
				pk INTEGER PRIMARY KEY AUTOINCREMENT,
				vendor_id INTEGER,
				sku INTEGER
			);'''
			)
		d.cursor.execute(
			'''ADD COLUMN {
	print('outside of with block')
	
