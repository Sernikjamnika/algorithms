import math
import sys
from zad1.PriorityQueue import PriorityQueue


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.queue = PriorityQueue()
        # self.vertexes = vertexes  # from 0 to number_of_vertexes - 1
        # self.list_of_neighbourhood = list_of_neighbourhood # from 0 to number_of_vertexes - 1

    # def weight(self, u_index, v_label):
    #     for edge in self.graph.edges[u_index]:
    #         if edge.node_to == v_label:
    #             return edge.weight

    # def search_edge(self, node_from_value, node_to_value):
    #     for edge in self.graph.edges[node_from_value - 1]:
    #         if edge.node_to == node_to_value:
    #             return edge

    def dijkstra(self, source):
        self.initialize_single_source(source)
        self.queue.build_min_heap(self.graph.vertexes.copy())
        while self.queue.empty() != 1:
            node_u = self.queue.pop()

            for edge in self.graph.edges[node_u.value - 1]:
                node_v = self.graph.vertexes[edge.node_to - 1]
                self.relax(node_u, node_v, edge.weight)

    def relax(self, node_u, node_v, weight):
        new_distance = node_u.key + weight
        if node_v.key > new_distance:
            self.queue.priority(node_v.value, new_distance)
            node_v.key = new_distance
            node_v.pre = node_u.value

    # def relax(self, u_index, v_index):
    #     node_v = self.graph.vertexes[v_index]
    #     node_u = self.graph.vertexes[u_index]
    #     new_distance = node_u.key + self.weight(u_index, v_index + 1)
    #     if node_v.key > new_distance:
    #         self.queue.priority(v_index + 1, new_distance)
    #         node_v.key = new_distance
    #         node_v.pre = u_index + 1

    def initialize_single_source(self, source):
        for vertex in self.graph.vertexes:
            vertex.key = math.inf
            vertex.pre = None
        self.graph.vertexes[source].key = 0

    def print_shortest_paths(self):
        for vertex in self.graph.vertexes:
            while vertex is not None:
                if vertex.pre is None:
                    print(vertex.value, vertex.value, 0, file=sys.stderr)
                    vertex = vertex.pre
                else:
                    predecessor = self.graph.vertexes[vertex.pre - 1]
                    # print(vertex.value, vertex.pre, self.weight(vertex.pre - 1, vertex.value), file=sys.stderr, end=" -> ")
                    print(vertex.value, predecessor.value, vertex.key - predecessor.key, file=sys.stderr, end=" -> ")
                    vertex = predecessor
                    # vertex = self.graph.vertexes[vertex.pre - 1]


