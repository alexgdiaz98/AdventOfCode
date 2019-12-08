def print_image(layer):
    for row in layer:
        for val in row:
            if val != 0:
                print(val, end='')
            else:
                print(' ', end='')
        print()

with open('input.txt', 'r') as file:
    final_layer = [[2]*25 for j in range(6)]
    layer = []
    row = []
    WIDTH = 25
    HEIGHT = 6
    while True:
        c = file.read(1)
        if not c:
            break
        if c == '\n':
            continue
        row.append(int(c))
        if len(row) == WIDTH:
            layer.append(row)
            if len(layer) == HEIGHT:
                for i, row_layer in enumerate(layer):
                    for j, val in enumerate(row_layer):
                        if val != 2 and final_layer[i][j] == 2:
                            final_layer[i][j] = val
                layer = []
            row = []
    print_image(final_layer)