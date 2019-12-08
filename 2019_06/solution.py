orbits = {}

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    def attach(n):
        self.children.append(n)

def find_child(root, name):
    if root.name == name:
        return True
    for child in root.children:
        if find_child(child, name):
            return True
    return False

def find_depth(root, name):
    if root.name == name:
        return 1
    for child in root.children:
        depth = find_depth(child, name)
        if depth != -1:
            return depth + 1
    return -1

def is_indirectly_connected(orbit1, orbit2):
    return (find_child(orbit1, orbit2.name) or find_child(orbit2, orbit1.name))

def print_children(orbit):
    print('[%s: ' % orbit.name, end='')
    for i, child in enumerate(orbit.children):
        print_children(child)
        if i != len(orbit.children)-1:
            print(', ', end='')
    print(']', end='')

def count_connections(root, weight):
    total = 0
    total += len(root.children) # Direct Orbits
    for child in root.children:
        total += count_connections(child, weight+1) + weight # Indirect Orbits
    return total

COM = Node('COM')
orbits['COM'] = COM

def find_SAN(orbit):
    if orbit.name == 'SAN':
        print('AM SAN:', find_depth(orbit, 'YOU'))
    elif orbit.name == 'YOU':
        print('AM YOU:', find_depth(orbit, 'SAN'))
    else:
        dist = 0
        for child in orbit.children:
            if find_child(child, 'SAN') and find_child(child, 'YOU'):
                find_SAN(child)
            elif find_child(child, 'SAN'):
                dist += find_depth(child, 'SAN')-1
                print('SAN found - dist:', dist)
            elif find_child(child, 'YOU'):
                dist += find_depth(child, 'YOU')-1
                print('YOU found - dist:', dist)
    
with open('input.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        parent, child = line.split(')')
        if parent in orbits and child in orbits:
            orbits[parent].children.append(orbits[child])
        elif parent in orbits:
            child_orbit = Node(child)
            orbits[child] = child_orbit
            orbits[parent].children.append(child_orbit)
        elif child in orbits:
            parent_orbit = Node(parent)
            parent_orbit.children.append(orbits[child])
            orbits[parent] = parent_orbit
        else:
            parent_orbit = Node(parent)
            child_orbit = Node(child)
            parent_orbit.children.append(child_orbit)
            orbits[parent] = parent_orbit
            orbits[child] = child_orbit
#print_children(COM)
find_SAN(COM)