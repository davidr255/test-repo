

class Animal():

	def __init__(self, pulse):
		self.pulse = 'HasPulse'


class Mammal(Animal):
	
	def __init__(self, fur):
		self.fur = 'HasFur'
		Animal.__init__(self,'HasPulse')

	def print_features(self):
		print(pulse + 'and '+fur)


Semba = Mammal('ok')


if __name__ == '__main__':
	print(Animal()))
