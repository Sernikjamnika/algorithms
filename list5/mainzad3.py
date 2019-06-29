import argparse
import time
from Graph_module.Graph import Graph
from Graph_module import Edge
from Graph_module.GraphNode import GraphNode
from zad3.Kruskal import Kruskal
from zad3.KruskalEdge import KruskalEdge
from zad3.KruskalGraphNode import KruskalGraphNode
from zad3.Prim import Prim


def parse(edge_data):
    return [int(edge_data[0]), int(edge_data[1]), float(edge_data[2])]


def get_operations(name):
    algorithms = {
        "prim": {
            "edge": Edge,
            "vertex": GraphNode,
            "algorithm_object": Prim,
        },
        "kruskal": {
            "edge": KruskalEdge,
            "vertex": KruskalGraphNode,
            "algorithm_object": Kruskal,
        }
    }
    return algorithms[name]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prim", action="store_true")
    parser.add_argument("-k", "--kruskal", action="store_true")
    args = parser.parse_args()
    if args.prim:
        operations = get_operations("prim")
    else:
        operations = get_operations("kruskal")
    number_of_vertexes = int(input().strip())
    number_of_edges = int(input().strip())
    list_of_neighbourhood = [[] for _ in range(number_of_vertexes)]
    for _ in range(number_of_edges):
        tmp_edge = parse(input().strip().split())
        edge = operations["edge"](*tmp_edge)
        edge_rev = operations["edge"](*tmp_edge[1::-1], tmp_edge[2])
        list_of_neighbourhood[tmp_edge[0] - 1].append(edge)
        list_of_neighbourhood[tmp_edge[1] - 1].append(edge_rev)
    graph = Graph([operations["vertex"](i + 1) for i in range(number_of_vertexes)], list_of_neighbourhood)
    algorithm = operations["algorithm_object"](graph)
    tree = algorithm.mst
    total_weight = 0
    for list_of_neighbours in tree:
        for edge in list_of_neighbours:
            print(edge.node_from, edge.node_to, edge.weight)
            total_weight += round(edge.weight, 5)
    print(round(total_weight, 5))


if __name__ == "__main__":
    main()
