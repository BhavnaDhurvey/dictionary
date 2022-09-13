def wut(data):
    s = 0
    for dic in data:
        for i,value in dic.items():
            if value == "True":
                s += 1
    return s

data = [{'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'}, 
        {'id': 3, 'success': True, 'name': 'Alex'}]
wutewa = data
wut(wutewa)

print(data)

data = [{'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'}, 
        {'id': 3, 'success': True, 'name': 'Alex'}]

print(data['id'][0])