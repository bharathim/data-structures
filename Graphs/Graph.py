from LinkedList.LinkedList import LinkedList


class Graph(object):
    def __int__(self, vertices):
        self.vertices = vertices
        self.array = [LinkedList() for _ in range(vertices)]

    def add_edge(self, source, destination):
        pass

    def print_graph(self):
        pass
