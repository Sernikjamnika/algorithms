import time
import sys
from Graph_module.Edge import Edge
from Graph_module.Graph import Graph
from Graph_module.GraphNode import GraphNode
from zad2.Dijkstra import Dijkstra


def parse(edge_data):
    return [int(edge_data[0]), int(edge_data[1]), float(edge_data[2])]


def main():
    number_of_vertexes = int(input().strip())
    number_of_edges = int(input().strip())
    list_of_neighbourhood = [[] for _ in range(number_of_vertexes)]
    for _ in range(number_of_edges):
        tmp_edge = parse(input().strip().split())
        edge = Edge(*tmp_edge)
        list_of_neighbourhood[tmp_edge[0] - 1].append(edge)
    graph = Graph([GraphNode(i + 1) for i in range(number_of_vertexes)], list_of_neighbourhood) #tu jest o
    dijkstra = Dijkstra(graph)
    source = int(input().strip()) - 1  # [1, number_of_vertexes] -> [0, number_of_vertexes-1]
    start = time.time()
    dijkstra.dijkstra(source)
    finish = time.time() - start
    for vertex in graph.vertexes:
        print(vertex.value, vertex.key)
    dijkstra.print_shortest_paths()
    print(finish, file=sys.stderr)


if __name__ == "__main__":
    main()
