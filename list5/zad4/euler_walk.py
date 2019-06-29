import sys

from zad3.KruskalEdge import KruskalEdge


def euler_walk(tree):
    k = 0
    W = 0
    memory = 0
    current_vertex = 1
    tree_copy = [edges.copy() for edges in tree]
    for edges in tree:
        for edge in edges:
            tree_copy[edge.node_to - 1].append(KruskalEdge(edge.node_to, edge.node_from, edge.weight))
    memory += sys.getsizeof(current_vertex)
    memory += sys.getsizeof(tree_copy)
    visited = [0 for _ in range(len(tree_copy))]
    number_of_visited = 1
    print(current_vertex, file=sys.stderr, end="")
    while number_of_visited < len(tree):
        tree_copy[current_vertex - 1].sort(key=lambda x: visited[x.node_to - 1])
        current_edge = tree_copy[current_vertex - 1][0]
        if visited[current_edge.node_to - 1] == 1:
            visited[current_edge.node_from - 1] = 2
        elif visited[current_edge.node_to - 1] == 0:
            visited[current_edge.node_from - 1] = 1
            k += 1
            W += current_edge.weight
            number_of_visited += 1
        print(" ->", current_edge.node_to, file=sys.stderr, end="")
        current_vertex = current_edge.node_to
    return k, W, memory























        # edge = stack.pop()
        # print(" ->", edge.node_to, file=sys.stderr, end="")
        # current = edge.node_to
        # tree_copy[edge.node_from - 1].remove(edge)
        # visited[edge.node_from] = 1
        # k += 2
        # if len(tree_copy[current - 1]) > 0:
        #     for element in tree_copy[current - 1]:
        #         stack.append(element)
        #         W += 2 * element.weight
        # else:
        #     while len(tree_copy[current - 1]) == 0:
        #         current = pres[current - 1]
        #         print(" ->", current, file=sys.stderr, end="")

    memory += sys.getsizeof(edge)
    memory += sys.getsizeof(W)
    memory += sys.getsizeof(k)
    return k, W, memory
