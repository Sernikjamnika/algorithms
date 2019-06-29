from zad2.RBTree import RBTree
import math
import re


class HashMap:
    def __init__(self, length=128):
        self.length_of_hashmap = length
        self.buckets = [[] for _ in range(self.length_of_hashmap)]
        self.lengths = [0 for _ in range(self.length_of_hashmap)]
        self.are_trees = [False for _ in range(self.length_of_hashmap)]
        self.A = (math.sqrt(5) - 1) / 2
        self.nt = 300
        self.number_of_elements = 0
        self.maximum_number_of_elements = 0
        self.prog = re.compile(r'^[^a-zA-Z]*([^ ]*)(?<=[a-zA-Z])[^a-zA-Z]*')

    def hash(self, value):
        number = 0
        for letter in value:
            number += ord(letter)
        fraction = math.modf(number * self.A)[0]
        hash_value = math.floor(self.length_of_hashmap * fraction)
        return int(hash_value)

    def insert(self, value):
        result = self.prog.match(value)
        if result is None:
            value = ""
        else:
            value = result.groups()[0]
        key = self.hash(value)
        if self.lengths[key] + 1 < self.nt:
            # if self.are_trees[key]:
            #     self.change_to_list(key)
            self.__insert_hash_node(key, value)
        else:
            if not self.are_trees[key]:
                self.change_to_rbtree(key)
            self.__insert_rb_node(key, value)

        self.lengths[key] += 1
        self.number_of_elements += 1
        if self.number_of_elements > self.maximum_number_of_elements:
            self.maximum_number_of_elements = self.number_of_elements

    def delete(self, value):
        key = self.hash(value)
        if self.lengths[key] < self.nt:
            self.__delete_hash_node(key, value)
        else:
            self.__delete_rb_node(key, value)

    def __delete_rb_node(self, key, value):
        tree = self.buckets[key]
        if tree.delete(value) == 0:
            self.lengths[key] -= 1
            self.number_of_elements -= 1
        if self.lengths[key] < self.nt:
            self.change_to_list(key)

    def __insert_rb_node(self, key, value):
        self.buckets[key].insert(value)

    def __insert_hash_node(self, key, value):
        array = self.buckets[key]
        for index, element in enumerate(array):
            if element > value:
                array.insert(index, value)
                return
        array.append(value)

    def __delete_hash_node(self, key, value):
        array = self.buckets[key]
        if value in array:
            array.remove(value)
            self.number_of_elements -= 1
            self.lengths[key] -= 1

    def load(self, name_of_file, sep=" "):
        with open(name_of_file, 'r') as file:
            array = file.read().split()
            for value in array:
                for element in value.split(sep):
                    self.insert(element)

    def find(self, value):
        key = self.hash(value)
        if not self.are_trees[key]:
            return self.__find_hash_node(key, value)
        else:
            return self.__find_rb_node(self.buckets[key], value)

    @staticmethod
    def __find_rb_node(tree, value):
        return tree.find(value)

    def __find_hash_node(self, key, value):
        array = self.buckets[key]
        if value in array:
            return 1
        return 0

    def change_to_list(self, key):
        self.are_trees[key] = False
        self.buckets[key] = self.buckets[key].in_order_walk(self.buckets[key].root)

    def change_to_rbtree(self, key):
        self.are_trees[key] = True
        tree = RBTree()
        array = self.buckets[key]
        for element in array:
            tree.insert(element)
        self.buckets[key] = tree

    def minimum(self):
        return None

    def maximum(self):
        return None

    def successor(self):
        return None

    def in_order_walk(self):
        return None


