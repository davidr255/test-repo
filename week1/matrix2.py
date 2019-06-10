
with open('testmatrix0.txt') as f:
	for row in f:
		print(row)
		a = row.split()
		b = map(int,a)
		c = sum(b)
		print(c)
#		row_list = list(map(int,row.split(row.strip())))
#		print(row_list)
#		sum = sum(row_list)
#		print(sum)
