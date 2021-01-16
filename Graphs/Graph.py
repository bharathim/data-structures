from LinkedList.LinkedList import LinkedList
from Queues.Queue import Queue
from Stacks.stack import Stack


class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [LinkedList() for _ in range(vertices)]

    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.edges[source].prepend(destination)

    def bfs_traversal(self, start):
        result = []

        queue = Queue()
        queue.enqueue(start)
        visited = {start}

        while not queue.is_empty():
            current_vertex = queue.dequeue()
            result.append(current_vertex)

            adjacent_vertex = self.edges[current_vertex].head
            while adjacent_vertex:
                if adjacent_vertex.data not in visited:
                    visited.add(adjacent_vertex.data)
                    queue.enqueue(adjacent_vertex.data)
                adjacent_vertex = adjacent_vertex.next
        return result

    def dfs_traversal(self, start):
        result = []

        stack = Stack()
        stack.push(start)
        visited = {start}

        while not stack.is_empty():
            current_vertex = stack.pop()
            result.append(current_vertex)
            adjacent_vertex = self.edges[current_vertex].head

            while adjacent_vertex:
                if adjacent_vertex.data not in visited:
                    visited.add(adjacent_vertex.data)
                    stack.push(adjacent_vertex.data)

                adjacent_vertex = adjacent_vertex.next
        return result

    def print_graph(self):
        for i in range(self.vertices):
            print('|{0}'.format(i), end='| => ')
            current = self.edges[i].head
            while current:
                print('[{0}'.format(current.data), end='] -> ')
                current = current.next
            print("None")


if __name__ == "__main__":
    g = Graph(7)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.print_graph()
    print(g.bfs_traversal(1))
    print(g.dfs_traversal(1))
