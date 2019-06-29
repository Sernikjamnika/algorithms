import math
from zad1.PriorityNode import PriorityNode


class GraphNode(PriorityNode):
    def __init__(self, value):
        self.pre = None
        super().__init__(value, math.inf)

