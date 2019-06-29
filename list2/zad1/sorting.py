import getopt
import operator
import sys
import time

from sorting_class import Sorting


def main(param):
    try:
        opt, args = getopt.getopt(param, "", ['type=', 'comp='])
    except getopt.GetoptError as err:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)
    sys.stdout.write("Enter length of array: ")
    length = int(input().strip())
    sys.stdout.write("Enter array: ")
    array = [int(i) for i in input().split(" ")]
    try:
        if opt[1][1] == '>=':
            comparator = operator.__gt__
        elif opt[1][1] == '<=':
            comparator = operator.__lt__
        else:
            assert False, sys.stdout.write("unhandled option of comp\n" +
                                           "possible comps: \"<=\"|\">=\"\n")

        if opt[0][1] == 'insert':
            start_time = time.time()
            Sorting.get_instance().insert_sort(array, comparator, 0, length - 1)
            finish_time = time.time()
        elif opt[0][1] == 'merge':
            start_time = time.time()
            Sorting.get_instance().merge_sort(array, comparator, 0, length - 1)
            finish_time = time.time()
        elif opt[0][1] == 'quick':
            start_time = time.time()
            Sorting.get_instance().quick_sort(array, comparator, 0, length - 1)
            finish_time = time.time()
        else:
            assert False, sys.stdout.write("unhandled option of type\n" +
                                           "possible types: insert|merge|quick|dualquick|hybrid\n")
        sys.stderr.write('Time [s]:' + str(finish_time - start_time) + '\n')
        sys.stderr.write('Number of swaps {}\nNumber of compares {}\n'
                         .format(Sorting.get_instance().number_of_swaps,
                                 Sorting.get_instance().number_of_compares))
        if Sorting. check_if_sorted(array, comparator):
            print("Sorted!")
        else:
            print("Not sorted :c")
        print('Number of sorted elements ' + str(len(array)))
        print(array)

    except IndexError as err:
        print(err)
        print("Length was given wrong")
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
