from collections import defaultdict

FILENAME = 'traffic.txt'
OUTPUT_STRING = "Room {room_id}, {avg_time:.2f} minute average visit, {npeople} visitor(s) total."


def line_to_dict(line):
    pers_id, room_id, in_out, time = line.split()
    return {
        'pers_id': pers_id,
        'room_id': room_id,
        'in_out': in_out,
        'time': time
    }


def dictlist(filename=FILENAME):
    return map(line_to_dict, open(filename, 'r'))


def visit_data(dictlist):
    # data is a dictionary with room ids as keys that
    # refer to which person ids have been seen in that
    # room and the total exit times - the total entry
    # times for time (it actually doesn't matter who
    # is walking in or out of a room as far as total
    # time spent in there. you can rearrange a long
    # chain of additions and subtractions however you
    # want and it works out that you don't have to care
    # who is walking in or out

    # defaultdict is a variant on dict in the collections
    # module. you create it with an argument that produces
    # the default value for nonexistent keys. this gets
    # you out of a bunch of if ins or convoluted .get
    # constructions

    data = defaultdict(lambda: {'pers_ids': [], 'time': 0})

    for entry in dictlist:
        if entry['pers_id'] not in data[entry['room_id']]['pers_ids']:
            data[entry['room_id']]['pers_ids'].append(entry['pers_id'])

        if entry['in_out'] == 'O':
            data[entry['room_id']]['time'] += int(entry['time'])
        elif entry['in_out'] == 'I':
            data[entry['room_id']]['time'] -= int(entry['time'])

    return data


def print_results(visit_data, output_string=OUTPUT_STRING):
    for room_id in sorted(visit_data, key=int):
        npeople = len(visit_data[room_id]['pers_ids'])
        avg_time = visit_data[room_id]['time']
        print(
            output_string.format(room_id=room_id,
                                 npeople=npeople,
                                 avg_time=avg_time))

if __name__ == "__main__":
    print_results(visit_data(dictlist()))
