import numpy as np
import sys
import argparse
import random
import operator
import time


class BinSearchTester:

    def __init__(self, equal_function=np.equal, order_function=np.greater):
        self.N_REP = 0
        self.equal_function = equal_function
        self.order_function = order_function
        self.invoke = 0

    def __bin_search(self, x, array, begin, finish):
        self.invoke += 1
        if begin <= finish:
            middle = (finish + begin) // 2
            if self.__is_equal(array[middle], x):
                return 1
            elif self.__compare(array[middle], x):
                return self.__bin_search(x, array, begin, middle - 1)
            else:
                return self.__bin_search(x, array, middle + 1, finish)
        else:
            return 0

    def concrete_test_bin_search(self, x, array, begin=0, finish=None):
        self.N_REP = 0
        array = np.array(array)
        if finish is None:
            finish = array.size - 1
        return self.__bin_search(x, array, begin, finish)

    def __is_equal(self, x, y):
        self.N_REP += 1
        return self.equal_function(x, y)

    def __compare(self, x, y):
        self.N_REP += 1
        return self.order_function(x, y)

    def randomized_test_bin_search(self, rep=1000, begin=0, finish=None):
        results = [["Length", "Accuracy", "Compares", "Time", "Comp to invoke"]]
        if finish is None:
            flag = 0
        else:
            flag = 1
        for length in range(900000, 1000000):
            array = np.sort(np.array([random.randint(0, length) for _ in range(length)]))
            success, summed_time, self.N_REP, self.invoke = 0, 0, 0, 0
            if flag == 0:
                finish = array.size - 1
            for _ in range(rep):
                searched = random.randint(0, length)
                begin_time = time.time()
                tmp = self.__bin_search(searched, array, begin, finish)
                summed_time += time.time() - begin_time
                if tmp == 1:
                    success += 1
            print([length, success / rep, self.N_REP / rep, summed_time / rep, self.N_REP / self.invoke])
        return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('searched', nargs=1, type=int, metavar="searched")
    parser.add_argument('integers', nargs="+", type=int, metavar="arr")
    args = parser.parse_args()
    tester = BinSearchTester()
    print(tester.concrete_test_bin_search(*args.searched, args.integers))
    print("liczba porownan", tester.N_REP)
    #print('\n'.join(str(element) for element in tester.randomized_test_bin_search()))


if __name__ == "__main__":
    main()


