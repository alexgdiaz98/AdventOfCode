def get_coords(line):
    coords = []
    for i in range(line[3]):
        for j in range(line[4]):
            coords.append([line[1] + i, line[2] + j])
    return coords

with open('input.txt', 'r') as file:
    lines = []
    for line in file:
        line = line.strip('#\n').replace('@', ',').replace('x', ',').replace(':', ',')
        lines.append([int(x) for x in line.split(',')])
    coords_once = []
    coords_twice = []
    line_num = 0
    for line in iter(lines):
        print(line_num)
        for coord in iter(get_coords(line)):
            if coord not in coords_once:
                coords_once.append(coord)
            elif coord not in coords_twice:
                coords_twice.append(coord)
        line_num += 1
    for coord in coords_twice:
        coords_once.remove(coord)
    print(coords_once)