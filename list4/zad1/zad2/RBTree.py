from zad2.SentinelNode import SentinelNode
from zad2.Color import Color
from zad2.RBNode import RBNode
import re


class RBTree:
    # find, minimum, maximum, load, findNode, in_order_walk are the same as in zad1

    def __init__(self):
        temp = SentinelNode()
        self.root = temp
        self.sentinel = temp
        self.number_of_elements = 0
        self.maximum_number_of_elements = 0
        self.prog = re.compile(r'^[^a-zA-Z]*([^ ]*)(?<=[a-zA-Z])[^a-zA-Z]*')

    def insert(self, value):
        result = self.prog.match(value)
        if result is None:
            node = RBNode("")
        else:
            node = RBNode(result.groups()[0])
        y = self.sentinel
        x = self.root
        while x is not self.sentinel:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is self.sentinel:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node
        node.left = self.sentinel
        node.right = self.sentinel
        self.number_of_elements += 1
        if self.number_of_elements > self.maximum_number_of_elements:
            self.maximum_number_of_elements = self.number_of_elements
        self.__insert_fix_up(node)

    def __insert_fix_up(self, node):
        while node.parent.color == Color.RED:
            if node.parent is node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == Color.RED:
                    node.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node is node.parent.right:
                        node = node.parent
                        self.rot_left(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.rot_right(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == Color.RED:
                    node.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node is node.parent.left:
                        node = node.parent
                        self.rot_right(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.rot_left(node.parent.parent)
        self.root.color = Color.BLACK

    def delete(self, value):
        node = self.find_node(value)
        if node is not self.sentinel:
            y = node
            original_color = y.color
            if node.left is self.sentinel:
                x = node.right
                self.rb_transplant(node, node.right)
            elif node.right is self.sentinel:
                x = node.left
                self.rb_transplant(node, node.left)
            else:
                y = self.minimum(node.right)
                original_color = y.color
                x = y.right
                if y.parent is node:
                    x.parent = y
                else:
                    self.rb_transplant(y, y.right)
                    y.right = node.right
                    y.right.parent = y
                self.rb_transplant(node, y)
                y.left = node.left
                y.left.parent = y
                y.color = node.color
            if original_color == Color.BLACK:
                self.__delete_fix_up(x)
            self.number_of_elements -= 1
            return 0
        return 1

    def __delete_fix_up(self, node):
        while node is not self.root and node.color == Color.BLACK:
            if node is node.parent.left:
                y = node.parent.right
                if y.color == Color.RED:
                    y.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.rot_left(node.parent)
                    y = node.parent.right
                if y.left.color == Color.BLACK and y.right.color == Color.BLACK:
                    y.color = Color.RED
                    node = node.parent
                else:
                    if y.right.color == Color.BLACK:
                        y.left.color = Color.BLACK
                        y.color = Color.RED
                        self.rot_right(y)
                        y = node.parent.right
                    y.color = node.parent.color
                    node.parent.color = Color.BLACK
                    y.right.color = Color.BLACK
                    self.rot_left(node.parent)
                    node = self.root
            else:
                y = node.parent.left
                if y.color == Color.RED:
                    y.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.rot_right(node.parent)
                    y = node.parent.left
                if y.right.color == Color.BLACK and y.left.color == Color.BLACK:
                    y.color = Color.RED
                    node = node.parent
                else:
                    if y.left.color == Color.BLACK:
                        y.right.color = Color.BLACK
                        y.color = Color.RED
                        self.rot_left(y)
                        y = node.parent.left
                    y.color = node.parent.color
                    node.parent.color = Color.BLACK
                    y.left.color = Color.BLACK
                    self.rot_right(node.parent)
                    node = self.root
        node.color = Color.BLACK

    def rb_transplant(self, node1, node2):
        if node1.parent is self.sentinel:
            self.root = node2
        elif node1 is node1.parent.left:
            node1.parent.left = node2
        else:
            node1.parent.right = node2
        node2.parent = node1.parent

    def rot_right(self, node):
        x = node.left
        node.left = x.right
        if x.right is not self.sentinel:
            x.right.parent = node
        x.parent = node.parent
        if node.parent is self.sentinel:
            self.root = x
        elif node.parent.right is node:
            node.parent.right = x
        else:
            node.parent.left = x
        x.right = node
        node.parent = x

    def rot_left(self, node):
        y = node.right
        node.right = y.left
        if y.left is not self.sentinel:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is self.sentinel:
            self.root = y
        elif node.parent.left is node:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def load(self, name_of_file, sep=" "):
        with open(name_of_file, 'r') as file:
            array = file.read().split()
            for value in array:
                self.insert(value)

    # returns pointer to minimal node in subtree
    def minimum(self, beginning_node=None):
        minimum = beginning_node
        if minimum is not self.sentinel and minimum is not None:
            while minimum.left is not self.sentinel:
                minimum = minimum.left
        if minimum is self.sentinel:
            return None
        return minimum

    # returns pointer to maximal node in subtree
    def maximum(self, beginning_node=None):
        maximum = beginning_node
        if maximum is not self.sentinel:
            while maximum.right is not self.sentinel:
                maximum = maximum.right
        return maximum

    # return 1 or 0 if node with given value exists
    def find(self, value):
        node = self.root
        while node is not self.sentinel and node.value != value:
            if node.value > value:
                node = node.left
            else:
                node = node.right
        if node is self.sentinel:
            return 0
        return 1

    def in_order_walk(self, node):
        array = []
        stack = []
        done = False
        while not done:
            if node is not self.sentinel:
                if node is self.root and node.color == Color.RED:
                    print("root")
                if node.color == Color.RED and node.parent.color == Color.RED:
                    print("parent and child Red")
                if node.color == Color.RED and node.right is not self.sentinel and node.right == Color.RED:
                    print("right red")
                if node.color == Color.RED and node.left is not self.sentinel and node.left == Color.RED:
                    print("left red")
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
        while node is not self.sentinel and node.value != value:
            if node.value > value:
                node = node.left
            else:
                node = node.right
        return node

    def successor(self, node):
        if node is not None:
            if node.right is not None:
                return self.minimum(node.right)
            y = node.parent
            while y is not None and node is y.right:
                node = y
                y = y.parent
            return node
        return None

    def check_black_height(self):
        black_height = 0
        black_heights = []
        node = self.root
        stack = []
        done = False
        while not done:
            if node is not self.sentinel:
                if node.color == Color.BLACK:
                    black_height += 1
                stack.append(node)
                node = node.left
            else:
                if len(stack) > 0:
                    node = stack.pop()
                    if node.right is self.sentinel and node.left is self.sentinel:
                        black_heights.append(black_height)
                    if node.color == Color.BLACK and node.right is self.sentinel:
                        black_height -= 1
                    node = node.right
                else:
                    done = True

        print(set(black_heights))
