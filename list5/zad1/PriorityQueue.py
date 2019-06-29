import math
from .PriorityNode import PriorityNode


class PriorityQueue:
    def __init__(self):
        self.array = []

    @staticmethod
    def get_parent(index):
        return (index + 1) // 2 - 1

    @staticmethod
    def get_left_child(index):
        return 2 * index + 1

    @staticmethod
    def get_right_child(index):
        return 2 * (index + 1)

    def min_heapify(self, index):
        while True:
            left = self.get_left_child(index)
            right = self.get_right_child(index)
            heap_size = len(self.array)
            if left < heap_size and self.array[index].key > self.array[left].key:
                minimum = left
            else:
                minimum = index
            if right < heap_size and self.array[minimum].key > self.array[right].key:
                minimum = right
            # minimum = min([self.array[left], self.array[right], self.array[index]])
            if index == minimum:
                break
            self.array[index], self.array[minimum] = self.array[minimum], self.array[index]
            index = minimum

    def build_min_heap(self, array):
        heap_size = len(array)
        self.array = array
        # od połowy, bo wszystkie inne elementy są liśćmi, więc są kopcami
        for i in range(heap_size // 2, -1, -1):
            self.min_heapify(i)

    def top(self):
        if len(self.array) > 0:
            return self.array[0]
        else:
            return None

    def pop(self):
        heap_size = len(self.array)
        if heap_size > 0:
            minimum, self.array[0] = self.array[0], self.array[heap_size - 1]
            self.array.pop()
            self.min_heapify(0)
            return minimum
        else:
            return None

    def increase_key(self, index, key):
        if key > self.array[index].key:
            return
        self.array[index].key = key
        while index > 0 and self.array[self.get_parent(index)].key > self.array[index].key:
            self.array[index], self.array[self.get_parent(index)] = self.array[self.get_parent(index)], self.array[index]
            index = self.get_parent(index)

    def insert(self, value, key):
        self.array.append(PriorityNode(value, math.inf))
        self.increase_key(len(self.array) - 1, key)

    def print(self):
        [print("( {}, {} ) ".format(element.value, element.key), end=" ") for element in self.array]
        print()

    # złożoność build_min_heap
    # na pierwszy rzut oka jest to O(n*lg(n))
    # jest to poprawne, ale nie do końca dokładne
    # zauważmy, że kopiec ma wysokość floor(lg(n)) i jest w nim co najwyżej ceil(n / 2 ^(h+1)) węzłów o wysokości h
    # oraz fakt, że min_heapify ma złożoność O(h)
    # stąd:
    # sum(from h = 0 to floor(lg(n)), ceil(n/2^(h+1) * O(h)) = O(n * sum(rom h = 0 to floor(lg(n)), h/2^h)
    # natomiast sum(rom h = 0 to inf, h/2^h) = 2
    # stąd  O(n * sum(rom h = 0 to floor(lg(n)), h/2^h) = O(n * sum(rom h = 0 to inf, h/2^h)) = O(n)
    def priority(self, value, key):
        for element in self.array:
            if value == element.value and key < element.key:
                element.key = key
        self.build_min_heap(self.array)

    def empty(self):
        if len(self.array) == 0:
            return 1
        else:
            return 0

    def check_priorities(self, index):
        flag_right = 0
        flag_left = 0
        node = self.array[index]
        if self.get_left_child(index) < len(self.array):
            left = self.array[self.get_left_child(index)]
            if left.key >= node.key:
                flag_left = self.check_priorities(self.get_left_child(index))
            else:
                flag_left = 1
        if self.get_right_child(index) < len(self.array):
            right = self.array[self.get_right_child(index)]
            if right.key >= node.key:
                flag_right = self.check_priorities(self.get_right_child(index))
            else:
                flag_right = 1
        return flag_left or flag_right



