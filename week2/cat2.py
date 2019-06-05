


class Animal:
	def __init__(self,name):
		self.pulse = 'has a pulse'

class Mammal(Animal):
	def __init__(self,name):
		self.fur = 'has fur'
		Animal.__init__(self,name)

	def print_features(self,name):
		print('A '+ name + ' ' + self.pulse+' and ' +self.fur)

lion = Mammal('lion')
lion.print_features('lion')
