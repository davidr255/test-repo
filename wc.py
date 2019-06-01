from collections import OrderedDict

def str_update(input_str):
	newstr1 = input_str.lower()
	newstr2 = newstr1.replace('?','')
	newstr3 = newstr2.replace('"','')
	newstr4 = newstr3.replace('.','')
	newstr5 = newstr4.replace(',','')
	return newstr5

def create_tuple_list(file_name):
	word_list = []
	with open(file_name) as f:
		for row in f:
			newrow = str_update(row)
			word_list.extend(newrow.split())
		word_count = []
		for word in word_list:
			word_count.append(word_list.count(word))
		word_dict = dict(zip(word_list,word_count))
		ordered_dict = sorted((value,key) for (key,value) in word_dict.items())
		return ordered_dict[::-1]
	
def word_stats(file_name,number):
	tuple_list = create_tuple_list(file_name)
	# print(tuple_list)
	for i in range(number):
		print('{}, {}'.format(tuple_list[i][1],tuple_list[i][0]))

word_stats('article.txt',10)
