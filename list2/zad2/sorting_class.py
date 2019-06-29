from threading import Lock
import sys
from math import floor
import random


class Sorting:
    __singleton_lock = Lock()
    __instance = None
    number_of_swaps = 0
    number_of_compares = 0

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            with cls.__singleton_lock:
                if not cls.__instance:
                    cls.__instance = cls()
        cls.__instance.number_of_compares = 0
        cls.__instance.number_of_swaps = 0
        return cls.__instance

    @classmethod
    def get_stats(cls):
        if cls.__instance:
            return str(cls.__instance.number_of_swaps) + ',' + str(cls.__instance.number_of_compares)
        return None

    def quick_sort(self, array, comp, begin, end):
        # condition for the fact if our partition is more than one element
        if begin < end:
            # choose pivot (let it be the beginning of our array)
            # better if it was randomly chosen like in random quicksort
            index = random.randint(begin, end)
            x = array[index]
            self.__swap(array, begin, index)
            i = begin - 1
            # move all elements smaller than pivot to the "right side" of the array
            # we start from 2nd element of array (or subarray) and go to the end
            for j in range(begin, end + 1):
                if self.__compare(array[j], x, comp):
                    i += 1
                    self.__swap(array, i, j)
            # move pivot to its final destination
            self.__swap(array, begin, i)
            # quick sort for the "left side" of the array
            Sorting.quick_sort(self, array, comp, begin, i - 1)
            # quick sort for the "right side" of the array
            Sorting.quick_sort(self, array, comp, i + 1, end)
        return array

    def merge_sort(self, array, comp, begin, end):
        if begin < end:
            middle = int(floor((begin + end) / 2))
            # merge sort for the left side of the list
            Sorting.merge_sort(self, array, comp, begin, middle)
            # merge sort for the right side of the list
            Sorting.merge_sort(self, array, comp, middle+1, end)
            # and now merging procedure
            Sorting.__merge(self, array, comp, begin, middle, end)
        return array

    def insert_sort(self, array, comp, begin, end):
        # starting from second place coz we at first nothing is to be compared with
        for i in range(begin + 1, end + 1):
            temp = array[i]
            j = i - 1
            # while value before temp (with smaller index in array) gives true from comparator
            # and index is greater than or equal zero
            # swap values
            while j >= begin and self.__compare(temp, array[j], comp):
                self.__assign(array, j + 1, array[j])
                j -= 1
            self.__assign(array, j + 1, temp)

    def __merge(self, array, comp, begin, middle, end):
        # lets break list into two temporary arrays
        left = array[begin: middle + 1]
        right = array[middle + 1: end + 1]

        counter = begin
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if self.__compare(left[i], right[j], comp):
                self.__assign(array, counter, left[i])
                i += 1
            else:
                self.__assign(array, counter, right[j])
                j += 1
            counter += 1

        if i <= len(left):
            while i < len(left):
                self.__assign(array, counter, left[i])
                counter += 1
                i += 1
        else:
            while j < len(right):
                self.__assign(array, counter, right[j])
                counter += 1
                j += 1

    def dual_pivot_quick_sort(self, array, comp, begin, end):
        if begin < end:
            index = random.randint(begin, end)
            array[begin], array[index] = array[index], array[begin]
            index = random.randint(begin, end)
            while array[begin] == array[index]:
                index = random.randint(begin, end)
            array[end], array[index] = array[index], array[end]

            if array[begin] > array[end]:
                pivot_left = array[end]
                pivot_right = array[begin]
            else:
                pivot_left = array[begin]
                pivot_right = array[end]
            i = begin + 1  # last element of left subarray
            k = end - 1  # first element of right subarray
            j = i  # limit of partitoning
            d = 0  # helps to decide which compare should be first with right or left pivot
            # loop until limitation of middle subarray and right subarray will meet
            while j <= k:
                if d >= 0:
                    if self.__compare(array[j], pivot_left, comp):
                        self.__swap(array, i, j)
                        i += 1  # our pivot move further
                        j += 1  # we move further
                        d += 1  # there is one more element at the left side
                    else:
                        if self.__compare(array[j], pivot_right, comp):
                            j += 1  # array[j] stays at place so will be at the middle
                        else:
                            self.__swap(array, j, k)
                            k -= 1  # limitation of right subarray went left
                            d -= 1  # one more element in right subarray
                else:
                    if self.__compare(pivot_right, array[k], comp):
                        k -= 1  # same as higher
                        d -= 1
                    else:
                        if self.__compare(array[k], pivot_left, comp):
                            # rotates 3 elements array[k] lands in left subarray and it is last element of it
                            # array[j] is rotated to be the first to check from right side
                            # array[i] becomes first to be checked from left side
                            self.__swap3(array, k, j, i)
                            i += 1
                            d += 1
                        else:
                            self.__swap(array, j, k)
                        j += 1
            # here pivots are placed at their destined place
            self.__assign(array, begin, array[i - 1])
            self.__assign(array, i - 1, pivot_left)
            self.__assign(array, end, array[k + 1])
            self.__assign(array, k + 1, pivot_right)
            # use dual pivot quick sort for left, right and middle subarray
            self.dual_pivot_quick_sort(array, comp, begin, i - 2)
            self.dual_pivot_quick_sort(array, comp, i, k)
            self.dual_pivot_quick_sort(array, comp, k + 2, end)

    def hybrid(self, array, comp, begin, end):
        if begin < end:
            middle = int(floor((begin + end) / 2))
            # if size of subarray is lesser or equal 22 (experimentally chosen)
            if end - begin + 1 <= 22:
                Sorting.insert_sort(self, array, comp, begin, end)

            else:
                # merge sort for the left side of the list
                Sorting.hybrid(self, array, comp, begin, middle)
                # merge sort for the right side of the list
                Sorting.hybrid(self, array, comp, middle + 1, end)
                # and now merging procedure
                Sorting.__merge(self, array, comp, begin, middle, end)
        return array

    # in this version output to stderr was erased no to make too much mess

    def __swap(self, array, a, b):
        array[a], array[b] = array[b], array[a]
        self.number_of_swaps += 1

    def __compare(self, a, b, comp):
        self.number_of_compares += 1
        return comp(a, b)

    def __assign(self, array, a, b):
        array[a] = b
        self.number_of_swaps += 1

    def __swap3(self, array, a, b, c):
        array[a], array[b], array[c] = array[b], array[c], array[a]
        self.number_of_swaps += 3

    @staticmethod
    def check_if_sorted(array, comp):
        for i in range(len(array) - 1):
            if not comp(array[i], array[i+1]):
                print(array[i + 1], array[i])
                return False
        return True

