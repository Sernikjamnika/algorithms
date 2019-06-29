from zad1.PriorityNode import PriorityNode


class KruskalGraphNode:
    def __init__(self, value):
        self.value = value
        self.pre = self
        self.rank = 0
