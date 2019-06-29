import re
from .Color import Color


class RBNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = Color.RED
