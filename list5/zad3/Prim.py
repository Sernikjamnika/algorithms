import math

from Graph_module import Edge
from zad1.PriorityQueue import PriorityQueue
import sys


def find_edge(edges, node_to):
    for edge in edges:
        if edge.node_to == node_to:
            return edge


class Prim:
    def __init__(self, graph):
        self.graph = graph
        self.queue = PriorityQueue()

    def prim(self, source=1):
        mst_tree = [[] for _ in range(len(self.graph.vertexes))]
        self.initialize_single_source(source)
        self.queue.build_min_heap(self.graph.vertexes.copy())
        visited = [0 for _ in range(len(self.graph.vertexes))]

        while self.queue.empty() != 1:
            vertex = self.queue.pop()
            visited[vertex.value - 1] = 1
            if vertex.pre is not None:
                tree_edge = find_edge(self.graph.edges[vertex.pre - 1], vertex.value)
                mst_tree[tree_edge.node_from - 1].append(tree_edge)
            for edge in self.graph.edges[vertex.value - 1]:
                vertex_neighbour = self.graph.vertexes[edge.node_to - 1]
                if visited[edge.node_to - 1] == 0 and edge.weight < vertex_neighbour.key:
                    self.queue.priority(vertex_neighbour.value, edge.weight)
                    vertex_neighbour.pre = vertex.value
                    vertex_neighbour.key = edge.weight
        return mst_tree

    def print_shortest_paths(self):
        total_weight = 0
        for vertex in self.graph.vertexes:
            if vertex.pre is None:
                print(vertex.value, vertex.value, 0)
            else:
                predecessor = self.graph.vertexes[vertex.pre - 1]
                # print(vertex.value, vertex.pre, self.weight(vertex.pre - 1, vertex.value), file=sys.stderr, end=" -> ")
                print(vertex.value, predecessor.value, vertex.key)
                # vertex = self.graph.vertexes[vertex.pre - 1]
                total_weight += vertex.key
        print(total_weight)

    mst = property(prim)

    def initialize_single_source(self, source):
        for vertex in self.graph.vertexes:
            vertex.key = math.inf
            vertex.pre = None
        self.graph.vertexes[source - 1].key = 0
