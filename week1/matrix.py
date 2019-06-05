from collections import defaultdict

FILENAME = 'testmatrix0.txt'
f = FILENAME

def read_matrix(filename):
	with open(filename) as f:
		return [[int(column) for column in row.split()] for row in f]

def sums(filename):
	##print('Row Sums: '+' '.join(str(e) for e in [sum(item) for item in matrix]))
	row_sums = [sum(item) for item in matrix]
	print('Row Sums: '+' '.join(str(e) for e in row_sums))
	##print('Column Sums: '+' '.join(str(e) for e in [sum(item) for item in list(zip(*matrix))]))
	##col_sums = [sum(item) for item in list(zip(*matrix))]
	col_list = list(zip(*matrix))
	col_sums = [sum(item) for item in col_list]
	print('Column Sums: '+' '.join(str(e) for e in col_sums))
	return row_sums, col_sums, col_list

def transpose(input):
	col_matrix = [[] for i in range(len(input[0]))]
	for row in range(len(input)):
		for item in range(len(matrix)):
			col_matrix[i].append(matrix[row][item])

def sums_matrix(filename):
	row_sums, col_sums, col_list = sums(filename)
	row_dict = dict(zip(row_sums,matrix))
	for key in sorted(row_dict):
		row = row_dict[key]
		print(' '.join(str(item) for item in row))
	col_dict = dict(zip(col_sums,col_list))
	for key in sorted(col_dict):
		row2 = [col_dict[key]]
		for i in range(4):
			row3 =[row2(i)]
		print(' '.join(str(item) for item in row3))
#	print(row_list)
#	for key,value in sorted(row_dict.keys()):
#	row_dict =  sorted(row_dict.keys())
#	print(row_dict)
#		print(value)
#	print(i for i in row_list)


matrix = read_matrix(f)
sums(f)
sums_matrix(f)

