import sys
import random
from Selector import SelectTester


def writeout(array, result):
    for i in range(len(array)):
        if array[i] == result:
            print('[', end='')
            print(array[i], end='')
            print(']', end=' ')
        else:
            print(array[i], end=" ")
    print()
def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-r', nargs=1, type=int, metavar='N', help='Length of array with random values')
    # parser.add_argument('-p')
    argument = sys.argv[1]
    length = int(input("Enter length: ").strip())
    statistics = int(input("Enter searched k-th statistics: ").strip())
    array = []
    if argument == '-r':
        array = [random.randint(0, length) for _ in range(length)]
    elif argument == '-p':
        array = [i for i in range(1, length + 1)]
        random.shuffle(array)
    tester = SelectTester()
    result = tester.select(array, 0, length - 1, statistics)
    writeout(array, result)
    tester = SelectTester()
    result = tester.randomized_select(array, 0, length - 1, statistics)
    writeout(array, result)


if __name__ == "__main__":
    main()
