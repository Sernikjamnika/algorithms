from zad1 import BSTTree, BSTNode
from zad2 import RBTree, RBNode
from zad3 import HashMap
import argparse
import time
import sys


def create_structure(name):
    structures = {
        "bst": BSTTree.BSTTree,
        "rbt": RBTree.RBTree,
        "hmap": HashMap.HashMap
    }
    return structures[name]


def make_operations(structures):
    structure = structures()
    number_of_operations = int(input().strip())
    actions = {
        "insert": [structure.insert, 0],
        "delete": [structure.delete, 0],
        "max": [structure.maximum, 0],
        "min": [structure.minimum, 0],
        "inorder": [structure.in_order_walk, 0],
        "find": [structure.find, 0],
        "successor": [structure.successor, 0],
        "load": [structure.load, 0]
    }
    operations = []
    for i in range(number_of_operations):
        operation = input().strip()
        operation = operation.split()
        operations.append(operation)

    for operation in operations:
        if operation[0] in ["max", "min", "successor"]:
            if isinstance(structure, HashMap.HashMap):
                result = actions[operation[0]][0]()
            else:
                result = actions[operation[0]][0](structure.root)
            if result is None:
                print()
            else:
                print(result.value)
        elif operation[0] in ["insert", "delete", "load"]:
            actions[operation[0]][0](operation[1])
        elif operation[0] == "inorder":
            if isinstance(structure, HashMap.HashMap):
                print()
            else:
                print(*actions[operation[0]][0](structure.root))
        else:
            result = actions[operation[0]][0](operation[1])    # find, successor
            if result is None:
                print()
            else:
                print(result)
        actions[operation[0]][1] += 1
    print(number_of_operations, file=sys.stderr)
    for key, value in actions.items():
        print(key, value[1], sep=": ", file=sys.stderr)
    print("Maximum number of elements: ", structure.maximum_number_of_elements, file=sys.stderr)
    print("Number of elements at the end: ", structure.number_of_elements, file=sys.stderr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", nargs=1, metavar="type")
    args = parser.parse_args()
    structures = create_structure(*args.type)
    start = time.time()
    make_operations(structures)
    finish = time.time() - start
    print(finish, file=sys.stderr)

if __name__ == "__main__":
    main()
