class Vertex:

    def __init__(self, key):
        self.connected_to = {}
        self.id = key
        self.parent = None
        self.color = 'WHITE'
        self.hop = 0

    def add_neighbor(self, vertex, weight):
        self.connected_to[vertex] = weight

    def get_connected_to(self):
        return self.connected_to.keys()

    def get_adjacent(self, key):
        if key in self.connected_to.keys():
            return self.connected_to[key]
        else:
            return False


class Graph:

    def __init__(self):
        self.vert_list = {}

    def add_edge(self, key1, key2):
        if key1 not in self.vert_list.keys():
            self.vert_list[key1] = Vertex(key1)
        if key2 not in self.vert_list.keys():
            self.vert_list[key2] = Vertex(key2)
        self.vert_list[key1].add_neighbor(self.vert_list[key2], 0)

    def get_vertex(self, key):
        if key in self.vert_list.keys():
            return self.vert_list[key]
        else:
            return None

    def get_vertex_keys(self):
        return self.vert_list.keys()
        
        
def breadth_first_search(g, vs):
    q = [g.get_vertex(vs)]
    while len(q) != 0:
        p = q.pop(0)
        print(p.id)
        for v in p.get_connected_to():
            if v.color == 'WHITE':
                v.color = 'GRAY'
                q.append(v)
                v.parent = p
                v.hop = p.hop+1
        p.color = 'BLACK'


def find_path(g,v,s):
    print(v.id)
    if v.parent == s:
        print(s.id)
        print("Path found")
        return
    if v.parent == None:
        print("No path found")
        return
    find_path(g,v.parent,s)


def depth_first_search(g, s):
    for v in s.get_connected_to():
        if v.color == 'WHITE':
            print(v.id)
            v.color = 'GRAY'
            v.parent = s
            v.hop = s.hop+1
            depth_first_search(g,v)
        v.color = 'BLACK'



g = Graph()
g.add_edge(1,2)
g.add_edge(1,5)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(4,6)
g.add_edge(4,7)
print(g.get_vertex_keys(), g.get_vertex(1))
# breadth_first_search(g,1)
print('-------------------------------')
# find_path(g,g.get_vertex(7),g.get_vertex(1))
print('-------------------------------')
depth_first_search(g,g.get_vertex(1))

        

