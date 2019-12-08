pos1 = [[0,0]]
pos2 = [[0,0]]
intersections = [[266, 0], [444, 0], [913, 0], [1124, 481], [1128, 421], [887, 421], [887, 281], [1128, 281], [-640, 0], [-198, -389], [-198, -527], [-198, -858], [-141, -982], [-53, -982], [150, -982], [151, -1037], [151, -1149], [181, -1600], [243, -1600], [341, -1600], [370, -1600], [423, -1552], [423, -1337], [1280, -163], [913, 42], [634, -93], [634, -112], [844, -636], [917, -636], [917, -311], [844, -311], [444, -251], [266, -251], [-266, -389], [-266, -527], [-266, -858], [-428, -1166], [-753, -1372], [-761, -1419], [-799, -1419], [-1664, -1165], [-1664, -1105], [-1272, -1105], [-1272, -1165], [-799, -1493], [-761, -1493], [-428, -1493], [-307, -1615], [-307, -1679], [-307, -1866], [-1, -2218], [-573, -2792], [-996, -2873], [-2787, -2502], [-2643, -2406], [-2522, -2096], [-2875, -1857], [-6218, -3404], [-6396, -3404], [-6396, -3443], [-6268, -3224], [-6396, -2932], [-6419, -2857], [-6529, -5243], [-6759, -5243], [-6759, -5421], [-6865, -6114], [-6885, -6518], [-6551, -6761], [-6511, -6072], [-6865, -5865], [-7214, -6518], [-7892, -6193], [-7726, -6171], [-7281, -6171], [-7107, -6518], [-8622, -6875], [-8622, -7018]]
arr = []
arr2 = []
with open('input.txt', 'r') as file:
    i = 0
    for line in file:
        if i == 0:
            arr.extend(line.split(','))
            i = 1
        else:
            arr2.extend(line.split(','))

def man_dist(pos):
    return abs(pos[0]) + abs(pos[1])

def get_positions(position, move):
    if move[0] == 'U':
        return [[position[0], position[1] + x+1] for x in range(int(move[1:]))]
    elif move[0] == 'D':
        return [[position[0], position[1] - x-1] for x in range(int(move[1:]))]
    elif move[0] == 'R':
        return [[position[0] + x+1, position[1]] for x in range(int(move[1:]))]
    elif move[0] == 'L':
        return [[position[0] - x-1, position[1]] for x in range(int(move[1:]))]
    else:
        return []

int1 = {}
int_visited = []
count1 = 1
count2 = 1
for move in arr:
    for pos in get_positions(pos1[-1], move):
        if pos in intersections and pos not in int_visited:
            int1[str(pos)] = count1
            int_visited.append(pos)
        count1 += 1
    pos1.extend(get_positions(pos1[-1], move))
    
combined = None
min_combined = -1

for move in arr2:
    for pos in get_positions(pos2[-1], move):
        if pos in intersections and combined == None:
            combined = pos
            min_combined = int1[str(pos)] + count2
        elif pos in intersections and int1[str(pos)] + count2 < min_combined:
            combined = pos
            min_combined = int1[str(pos)] + count2
        count2 += 1
    pos2.extend(get_positions(pos2[-1], move))

print(len(pos1), len(pos2))
print(combined, min_combined)