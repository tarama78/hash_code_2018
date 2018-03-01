import linecache

#python3 main.py

def parse(filename):
    line = linecache.getline(filename, 1)
    line = line.split(' ')
    ret1 = {
            'row' : int(line[0]),
            'col' : int(line[1]),
            'nb_car' : int(line[2]),
            'ride' : int(line[3]),
            'bonus' : int(line[4]),
            'step' : int(line[5])
            }
    line_read = 'seksek'
    ret2 = []
    i = 2
    while line_read != '':
        line_read = linecache.getline(filename, i)
        if line_read == '':
            break
        line = line_read.split(' ')
        ret2.append({
            'x1' : int(line[0]),
            'y1' : int(line[1]),
            'x2' : int(line[2]),
            'y2' : int(line[3]),
            'e_start' : int(line[4]),
            'l_fin' : int(line[5]),
            'use' : False
        });
        i += 1
    return [ret1, ret2]


def get_min(info, x, y):
    len_min = 2000000000
    index_path = -1
    for i in range(len(info[1])):
       if (info[1][i]['use'] == True):
            continue
       len_path = abs(x - info[1][i]['x1']) + abs(y - info[1][i]['y1']) + abs(info[1][i]['x1'] - info[1][i]['x2']) + abs(info[1][i]['y1'] - info[1][i]['y2']) + info[1][i]['e_start']
       if (len_path > info[1][i]['l_fin']):
           continue
       if (len_path < len_min):
           len_min = len_path
           index_path = i
    return [index_path, len_min]


def test(filename):
    info = parse(filename)

    for i in range(info[0]['nb_car']):
        if (len(info[1]) == 0):
            break
        min = get_min(info, 0, 0)
        steps = min[1]
        tab_steps = []
        while (info[1][min[0]]['l_fin'] > steps):
            tab_steps.append(min[0])
            x = info[1][min[0]]['x2']
            y = info[1][min[0]]['y2']
            info[1][min[0]]['use'] = True
            if (len(info[1]) == 0):
                break
            min = get_min(info, x, y)
            steps += min[1]
        print(len(tab_steps), end=' ')
        for i in tab_steps:
            print(i, end=' ')
        print()
