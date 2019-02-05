class Vertex:

    def __init__(self, key):
        self.connected_to = {}
        self.id = key

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
        
        