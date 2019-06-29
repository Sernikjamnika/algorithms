import getopt
import operator
import sys
import time

from prepare_list import Preparer
from sorting_class import Sorting

# All statistics in graphs.ipynb jupter notebook;

def main(param):
    try:
        opt, args = getopt.getopt(param, "", ['type=', 'comp=', 'stat='])
    except getopt.GetoptError as err:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    try:
        sortation = {}
        if opt[2][0] == '--stat':
            number_of_repetitions = int(args[0])
            file = open(opt[2][1], "w")
            array = Preparer.prepare_list(number_of_repetitions)
            sortation = {'insert': Sorting.insert_sort,
                         'merge': Sorting.merge_sort,
                         'quick': Sorting.quick_sort,
                         'dual_quick': Sorting.dual_pivot_quick_sort,
                         'hybrid': Sorting.hybrid}
    except IndexError:
        file = open("result.txt", "w+")
        sys.stdout.write("Enter length of array: ")
        length = int(input().strip())
        sys.stdout.write("Enter array: ")
        array = [[int(i) for i in input().split(" ")]]

        if opt[0][1] == 'insert':
            sortation = {'insert': Sorting.insert_sort}
        elif opt[0][1] == 'merge':
            sortation = {'merge': Sorting.merge_sort}
        elif opt[0][1] == 'quick':
            sortation = {'quick': Sorting.quick_sort}
        elif opt[0][1] == 'dualquick':
            sortation = {'dual_quick': Sorting.dual_pivot_quick_sort}
        elif opt[0][1] == 'hybrid':
            sortation = {'hybrid': Sorting.hybrid}
        else:
            assert False, "unhandled option of type"

    try:
        if opt[1][1] == '>=':
            comparator = operator.__ge__
        elif opt[1][1] == '<=':
            comparator = operator.__le__
        else:
            assert False, "unhandled option of comp"
        file.truncate()
        file.write("type,length_of_arr,no_compares,no_swaps,time\n")
        length = len(array)
        for j in range(length):
            for key, value in sortation.items():
                print(str(j / length * 100) + "%")
                file.write(key + ',' + str(len(array[j])) + ',')
                temp = array[j].copy()
                start_time = time.time()
                value(Sorting.get_instance(), temp, comparator, 0, len(array[j]) - 1)
                finish_time = time.time() - start_time
                file.write(Sorting.get_stats() + ',' + str(finish_time) + '\n')
                if not Sorting.check_if_sorted(temp, comparator):
                    print("Not sorted")
                    sys.exit(2)
        file.close()

    except IndexError as err:
        print("Length was given wrong")
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
