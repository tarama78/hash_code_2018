import linecache

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
            'start' : int(line[4]),
            'end' : int(line[5])
        });
        i += 1
    return [ret1, ret2]
