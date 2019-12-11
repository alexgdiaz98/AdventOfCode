import math

field = []
with open('input.txt', 'r') as file:
    for line in file:
        field.append(line.strip())
asteroids = []
for i, row in enumerate(field):
    for j, char in enumerate(row):
        if char == '#':
            asteroids.append([j, i])
#print(field, asteroids)
def find_asteroids_in_view(base):
    in_view = []
    for asteroid in iter(asteroids):
        if base != asteroid:
            x_diff = asteroid[0]-base[0]
            y_diff = asteroid[1]-base[1]
            #print(asteroid, asteroid2, x_diff, y_diff)
            if x_diff == 0:
                blocked = False
                i = 0
                while not blocked and i < abs(y_diff)-1:
                    if [int(base[0]), int(base[1] + (i+1) * (y_diff)/abs(y_diff))] in asteroids:
                        blocked = True
                        #print(asteroid, 'to', asteroid2, 'obstructed by', int(asteroid[0]), int(asteroid[1] + (i+1) * (y_diff)/abs(y_diff)))
                    i += 1
                if not blocked:
                    #print(asteroid, 'to', asteroid2, 'unobstructed')
                    in_view.append(asteroid)
            elif y_diff == 0:
                blocked = False
                i = 0
                while not blocked and i < abs(x_diff)-1:
                    if [int(base[0] + (i+1) * (x_diff)/abs(x_diff)), int(base[1])] in asteroids:
                        blocked = True
                        #print(asteroid, 'to', asteroid2, 'obstructed by', int(asteroid[0] + (i+1) * (x_diff)/abs(x_diff)), int(asteroid[1]))
                    i += 1
                if not blocked:
                    #print(asteroid, 'to', asteroid2, 'unobstructed')
                    in_view.append(asteroid)
            else:
                gcd = math.gcd(x_diff, y_diff)
                #print(gcd)
                x_diff /= gcd
                y_diff /= gcd
                blocked = False
                i = 1
                while not blocked and i < gcd:
                    if [int(base[0] + x_diff*i), int(base[1] + y_diff*i)] in asteroids:
                        blocked = True
                        #print(asteroid, 'to', asteroid2, 'obstructed by', int(asteroid[0] + x_diff*i), int(asteroid[1] + y_diff*i))
                    i += 1
                if not blocked:
                    #print(asteroid, 'to', asteroid2, 'unobstructed')
                    in_view.append(asteroid)
    return in_view

def find_200th(base, in_view):
    destroyed = []
    for asteroid in iter(in_view):
        angle = math.degrees(math.atan2(asteroid[1]-base[1], asteroid[0]-base[0]))
        destroyed.append([angle, asteroid])
    destroyed.sort()
    #print('\n'.join([str(i) for i in destroyed]))
    counter = 0
    found_90 = False
    for i in iter(destroyed):
        if found_90:
            counter += 1
            #print(counter, i)
            if counter == 200:
                return i
        elif i[0] == -90:
            found_90 = True
            counter += 1
            #print(counter, i)
    for i in iter(destroyed):
        counter += 1
        #print(counter, i)
        if counter == 200:
            return i 
    

base = [22, 28]
val200 = find_200th(base, find_asteroids_in_view(base))
print(val200[1][0] * 100 + val200[1][1])
