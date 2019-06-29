from zad2.Color import Color


class SentinelNode:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.value = ""
        self.color = Color.BLACK

