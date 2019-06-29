import time
import sys
from Graph_module.Edge import Edge
from Graph_module.Graph import Graph
from Graph_module.GraphNode import GraphNode
from zad3.Kruskal import Kruskal
from zad3.KruskalEdge import KruskalEdge
from zad3.KruskalGraphNode import KruskalGraphNode
from zad3.Prim import Prim
from zad4.euler_walk import euler_walk
from zad4.minimal_walk import minimal_walk
from zad4.radomized_walk import randomized_walk


def parse(edge_data):
    return [int(edge_data[0]), int(edge_data[1]), float(edge_data[2])]


def main():
    number_of_vertexes = int(input().strip())
    number_of_edges = number_of_vertexes * (number_of_vertexes - 1) // 2
    list_of_neighbourhood = [[] for _ in range(number_of_vertexes)]
    for _ in range(number_of_edges):
        tmp_edge = parse(input().strip().split())
        edge = KruskalEdge(*tmp_edge)
        rev_edge = KruskalEdge(*tmp_edge[1::-1], tmp_edge[2])
        list_of_neighbourhood[tmp_edge[0] - 1].append(edge)
        list_of_neighbourhood[tmp_edge[1] - 1].append(rev_edge)
    graph = Graph([KruskalGraphNode(i + 1) for i in range(number_of_vertexes)], list_of_neighbourhood)
    start = time.time()
    print(*randomized_walk(graph), time.time() - start)
    start = time.time()
    print(*minimal_walk(graph), time.time() - start)
    start = time.time()
    prim = Prim(graph)
    tree_prim = prim.prim()
    print(*euler_walk(tree_prim), time.time() - start)
    start = time.time()
    kruskal = Kruskal(graph)
    tree_kruskal = kruskal.kruskal()
    print(*euler_walk(tree_kruskal), time.time() - start)




if __name__ == "__main__":
    main()
