with open("input12.txt", "r") as f:
    lines = f.readlines()

class Cave():
    def __init__(self, name):
        self.name = name
        self.connections =[]
        self.is_big = name.isupper()
    
    def add_connection(self, connection):
        self.connections.append(connection)
    
    def get_name(self):
        return self.name
    
    def get_connection_names(self):
        c_names = []
        for c in self.connections:
            c_names.append(c.get_name())
        return c_names
        

def get_cave(cave_list, name):
    for c in cave_list:
        if c.get_name() == name: return c
    return 'no cave'

def find_paths(cave_list, start, end, visited, path, paths):
    if start.is_big == False:
        visited.append(start)
    path.append(start)
    if start == end:
        paths.append(path)
    else:
        for i in start.connections:
            if (len(visited) == len(set(visited)) or len(visited) == len(set(visited))+1) and i.get_name() != 'start': 
                find_paths(cave_list,i,end,visited,path,paths)
    if start.is_big == False:
        visited.remove(start)
    path.remove(start)


caves = []
cave_names = []

for line in lines:
    l = line.strip().split('-')
    for c in l:
        if c not in cave_names:
            cave = Cave(c)
            caves.append(cave)
            cave_names.append(c)
    c1 = get_cave(caves,l[0])
    c2 = get_cave(caves,l[1])
    c1.add_connection(c2)
    c2.add_connection(c1)

s = get_cave(caves,'start')
e = get_cave(caves, 'end')
visited = []
paths = []
path = []
find_paths(caves, s, e, visited, path, paths)
print ('number of paths =',len(paths))