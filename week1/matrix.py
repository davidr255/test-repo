


def read_matrix(filename):
	with open(filename) as f:
		return [[int(column) for column in row.split()] for row in f]

def sums(filename):
	return sum(i) for i in read_matrix(filename)	



print(read_matrix('testmatrix0.txt'))
print(sums('testmatrix0.txt']
