from zad1.BSTNode import BSTNode
import re


class BSTTree:
    def __init__(self, root=None):
        self.root = root
        self.number_of_elements = 0
        self.maximum_number_of_elements = 0
        self.prog = re.compile(r'^[^a-zA-Z]*([^ ]*)(?<=[a-zA-Z])[^a-zA-Z]*')

    def insert(self, value):
        result = self.prog.match(value)
        if result is None:
            node = BSTNode("")
        else:
            node = BSTNode(result.groups()[0])
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node
        self.number_of_elements += 1
        if self.number_of_elements > self.maximum_number_of_elements:
            self.maximum_number_of_elements = self.number_of_elements

    def delete(self, value):
        node = self.find_node(value)
        if node is not None:
            if node.left is None:
                self.transplant(node, node.right)
            elif node.right is None:
                self.transplant(node, node.left)
            else:
                successor = self.minimum(node.right)
                if successor.parent is not node:
                    self.transplant(successor, successor.right)
                    successor.right = node.right
                    successor.right.parent = successor
                self.transplant(node, successor)
                successor.left = node.left
                successor.left.parent = successor
            self.number_of_elements -= 1

    def transplant(self, node, transplanted):
        if node.parent is None:
            self.root = transplanted
        elif node is node.parent.right:
            node.parent.right = transplanted
        else:
            node.parent.left = transplanted
        if transplanted is not None:
            transplanted.parent = node.parent

    def load(self, name_of_file, sep=" "):
        with open(name_of_file, 'r') as file:
            array = file.read().split()
            for value in array:
                self.insert(value)

    # returns pointer to minimal node in subtree
    @staticmethod
    def minimum(beginning_node):
        minimum = beginning_node
        if minimum is not None:
            while minimum.left is not None:
                minimum = minimum.left
        return minimum

    # returns pointer to maximal node in subtree
    @staticmethod
    def maximum(beginning_node=None):
        maximum = beginning_node
        if maximum is not None:
            while maximum.right is not None:
                maximum = maximum.right
        return maximum

    # return 1 or 0 if node with given value exists
    def find(self, value):
        node = self.root
        while node is not None and node.value != value:
            if node.value > value:
                node = node.left
            else:
                node = node.right
        if node is None:
            return 0
        return 1

    # returns pointer to successor
    def successor(self, node):
        if node is not None:
            if node.right is not None:
                return self.minimum(node.right)
            y = node.parent
            while y is not None and node is y.right:
                node = y
                y = y.parent
        return node


    # returns values after in_order_walk in array
    @staticmethod
    def in_order_walk(node):
        array = []
        stack = []
        done = False
        while not done:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                if len(stack) > 0:
                    node = stack.pop()
                    array.append(node.value)
                    node = node.right
                else:
                    done = True
        return array

    # returns pointer to searched node
    def find_node(self, value):
        node = self.root
        while node is not None and node.value != value:
            if node.value > value:
                node = node.left
            else:
                node = node.right
        return node

    # just for me
    def __rebuild_tree(self, array, begin, end, parent=None):
        if end < begin:
            return None
        middle = (begin + end) // 2
        node = BSTNode(array[middle])
        node.right = self.__rebuild_tree(array, middle + 1, end, node)
        node.left = self.__rebuild_tree(array, begin, middle - 1, node)
        node.parent = parent
        return node

    def balance(self):
        array = []
        self.in_order_walk(self.root, array)
        self.root = self.__rebuild_tree(array, 0, len(array) - 1)






