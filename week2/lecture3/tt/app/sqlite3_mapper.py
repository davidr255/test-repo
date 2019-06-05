
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
#		self.cursor.close()

if __name__ == '__main__':
	with Database() as d:
		print('inside of with block')
	print('outside of with block')
	
