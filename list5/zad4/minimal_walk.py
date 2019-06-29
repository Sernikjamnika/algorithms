import random
import sys


def minimal_walk(graph):
    k = 0
    W = 0
    memory = 0
    source = graph.vertexes[0]
    memory += sys.getsizeof(source)
    visited = [False for _ in range(len(graph.vertexes))]
    visited[source.value - 1] = True
    memory += sys.getsizeof(visited)
    edge = None
    for vertex_edges in graph.edges:
        vertex_edges.sort(key=lambda x: x.weight)
    while not all(visited):
        for tmp_edge in graph.edges[source.value - 1]:
            if not visited[tmp_edge.node_to - 1]:
                edge = tmp_edge
                break
        print(source.value, file=sys.stderr, end=" -> ")
        source = graph.vertexes[edge.node_to - 1]
        visited[edge.node_to - 1] = True
        k += 1
        W += edge.weight
    print(source.value, file=sys.stderr)
    memory += sys.getsizeof(edge)
    memory += sys.getsizeof(W)
    memory += sys.getsizeof(k)
    return k, W, memory
