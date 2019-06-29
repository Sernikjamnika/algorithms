from zad1.PriorityNode import PriorityNode


class KruskalEdge(PriorityNode):
    def __init__(self, node_from, node_to, key):
        value = [node_from, node_to]
        super().__init__(value, key)

    def get_node_to(self):
        return self.value[1]

    def get_node_from(self):
        return self.value[0]

    def get_weight(self):
        return self.key

    node_to = property(get_node_to)
    node_from = property(get_node_from)
    weight = property(get_weight)

