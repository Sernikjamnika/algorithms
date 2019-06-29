import random
import sys
import math


class SelectTester:
    def __init__(self):
        self.number_of_comp = 0
        self.number_of_swaps = 0

    @staticmethod
    def test(method, array, begin, length):
        for j in range(10):
            statistics = random.randint(1, length)
            tmp = method(array, begin, length - 1, statistics)
            if statistics != tmp:
                print(statistics, tmp)

    def partition(self, array, begin, end):
        pivot = array[begin]
        sys.stderr.write("pivot = " + str(pivot) + '\n')
        j = begin
        for i in range(begin + 1, end + 1):
            if self.__compare(array[i], pivot):
                j += 1
                self.__swap(array, j, i)
        self.__swap(array, begin, j)
        return j + 1

    def randomized_partition(self, array, begin, end):
        tmp = random.randint(begin, end - 1)
        array[begin], array[tmp] = array[tmp], array[begin]
        return self.partition(array, begin, end)

    def randomized_select(self, array, begin, end, k):
        sys.stderr.write("array = " + str(array) + '\n')
        sys.stderr.write("k = " + str(k) + '\n')
        if begin == end:
            return array[begin]
        current_index = self.randomized_partition(array, begin, end)
        position = current_index - begin
        if k == position:
            # pivot from randomized_partition is k-th statistics
            return array[current_index - 1]
        elif self.__compare(position, k):
            # k is in the left part
            return self.randomized_select(array, current_index, end, k - position)
        else:
            # k is in the right part
            return self.randomized_select(array, begin, current_index - 2, k)

    def __swap(self, array, a, b):
        array[a], array[b] = array[b], array[a]
        sys.stderr.write("swap (" + str(array[a]) + ", " + str(array[b]) + ")\n")
        self.number_of_swaps += 1

    def __compare(self, a, b):
        self.number_of_comp += 1
        sys.stderr.write("comp (" + str(a) + ", " + str(b) + ")\n")
        return a < b

    def __assign(self, array, a, b):
        array[a] = b
        self.number_of_swaps += 1

    def partition_modified(self, array, start, end, pivot):
        iterator = start
        pivot_pos = 0

        while iterator <= end:
            if array[iterator] == pivot:
                pivot_pos = iterator
                break
            iterator += 1

        self.__swap(array, pivot_pos, end)

        new_pivot_pos = start

        iterator = start

        while iterator <= (end - 1):
            if array[iterator] <= pivot:
                self.__swap(array, new_pivot_pos, iterator)
                new_pivot_pos += 1
            iterator += 1

        self.__swap(array, new_pivot_pos, end)
        return new_pivot_pos

    def select(self, array, start, end, k):
        list_of_list = []

        for i in range(start, end + 1, 5):
            if i + 5 >= end:
                list_of_list.append(sorted(array[i:(end + 1)]))
            else:
                list_of_list.append(sorted(array[i:(i + 5)]))
        medians = []

        for lis in list_of_list:
            medians.append(lis[math.floor(len(lis) / 2)])

        meds_length = len(medians)

        if meds_length == 1:
            pivot = medians[0]
        else:
            pivot = self.select(medians, 0, meds_length - 1, meds_length // 2)

        pos = self.partition_modified(array, start, end, pivot)

        if (pos - start) == k - 1:
            return array[pos]
        elif (pos - start) > (k - 1):
            return self.select(array, start, pos - 1, k)
        else:
            return self.select(array, pos + 1, end, (k - pos + start - 1))

        pass




