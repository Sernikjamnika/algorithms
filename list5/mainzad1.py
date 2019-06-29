from zad1.PriorityQueue import PriorityQueue


def make_operations(structures):
    structure = structures()
    number_of_operations = int(input().strip())

    actions = {
        "insert": structure.insert,
        "pop": structure.pop,
        "top": structure.top,
        "priority": structure.priority,
        "empty": structure.empty,
        "print": structure.print
    }

    operations = []
    for i in range(number_of_operations):
        operation = input().strip()
        operation = operation.split()
        operations.append(operation)

    for operation in operations:
        if operation[0] in ["insert", "priority"]:
            actions[operation[0]](int(operation[1]), int(operation[2]))
        elif operation[0] in ["top", "pop"]:
            result = actions[operation[0]]()
            if result is not None:
                print(result.value)
            else:
                print()
        elif operation[0] == "empty":
            print(actions[operation[0]]())
        else:
            actions[operation[0]]()


def main():
    make_operations(PriorityQueue)


if __name__ == "__main__":
    main()
