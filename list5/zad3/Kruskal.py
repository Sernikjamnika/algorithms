from zad1.PriorityQueue import PriorityQueue


class Kruskal:

    def __init__(self, graph):
        self.graph = graph
        self.queue = PriorityQueue()

    def kruskal(self):
        mst_tree = [[] for _ in range(len(self.graph.vertexes))]
        for vertex in self.graph.vertexes:
            self.make_set(vertex)
        self.queue.build_min_heap([edge for array in self.graph.edges for edge in array])
        while self.queue.empty() != 1:
            edge = self.queue.pop()
            if self.find_set(edge.value[0] - 1) is not self.find_set(edge.value[1] - 1):
                mst_tree[edge.value[0] - 1].append(edge)
                self.union(edge.value[0] - 1, edge.value[1] - 1)
        return mst_tree

    @staticmethod
    def make_set(vertex):
        vertex.pre = vertex
        vertex.rank = 0

    def find_set(self, vertex_label):
        vertex = self.graph.vertexes[vertex_label]
        if vertex is not vertex.pre:
            vertex.pre = self.find_set(vertex.pre.value - 1)
        return vertex.pre

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    @staticmethod
    def link(x, y):
        if x.rank > y.rank:
            y.pre = x
        else:
            x.pre = y
            if x.rank == y.rank + 1:
                y.rank += 1

    mst = property(kruskal)
