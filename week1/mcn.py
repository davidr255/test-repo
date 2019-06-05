


def check_mcn(a,b,c):
	is_mcn = []
	isnot_mcn = []
	for number in range(0,100):
		for divisor in a,b,c:
			remain = number % divisor
			if remain % divisor == 0:
				is_mcn.append(number)
			else:
				isnot_mcn.append(number)
	print(set(is_mcn))
	print(set(isnot_mcn))

check_mcn(6,9,20)
