import math

def man_dist(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1]) + abs(point1[2]-point2[2]) + abs(point1[3]-point2[3])

def near_constellation(constellation, point1):
    
    for point2 in constellation:
        if man_dist(point1, point2) <= 3:
            #print('dist from', point1, 'to', point2, ':', man_dist(point1, point2), ' <= 3')
            return True
    return False

points = [] # List of 4D points
with open('input.txt', 'r') as file:
    for line in file:
        #line = line[:-1]
        points.append([int(n) for n in line.split(',')])

constellations = []
for point in iter(points):
    found = -1
    i = 0
    while i < len(constellations):
        if near_constellation(constellations[i], point) and found == -1:
            constellations[i].append(point)
            found = i
            i += 1
        elif near_constellation(constellations[i], point):
            constellations[found].append(point)
            constellations[found].extend(constellations[i])
            constellations.remove(constellations[i])
        else:
            i += 1
    if found == -1:
        constellations.append([point]) # Make a new constellation with just the point
print(len(constellations))