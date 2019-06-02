import collections

FILENAME = 'traffic.txt'


dictlist = []
with open('traffic.txt') as f:
	for row in f:
		pers_id,room_id,in_out,time = row.split()
		dict = {'pers_id':pers_id,'room_id':room_id,
			'in_out':in_out,'time':time}
		dictlist.append(dict)

masterdict = {}
roomlist = []
for entry in dictlist:
	roomlist.append(entry['room_id'])
uniq_roomlist = sorted(set(roomlist))
for entry in uniq_roomlist:
	masterdict.update({entry:''})
for key in masterdict:
	time = 0
	visit_count = 0
	for item in dictlist:
		if key == item['room_id'] and item['in_out'] == 'O':
			time += int(item['time'])
			visit_count += 1
		if key == item['room_id'] and item['in_out'] == 'I':
			time -= int(item['time'])
	average = time / visit_count
	masterdict.update({key:{'time':time,'vist_count':visit_count,'average':average}})
uniq_roomlist = sorted(list(map(int, uniq_roomlist)))
for i in uniq_roomlist:
	for item in masterdict:
		average = int(masterdict[str(i)]['average'])
		visit_count = masterdict[str(i)]['vist_count']
	print("Room {}, {} minute avg visit, {} visitors".format(i,average,visit_count))





#	for item in dictlist:
#		if dictlist['room_id'] == entry:
#			masterdict.update({entry:item})



