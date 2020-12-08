import copy
file = "input.txt"


def acc_count(operator_index, data):
    for index in operator_index:
        operation_list = copy.deepcopy(data)
        pos, accumulator = 0, 0
        if operation_list[index][0] == 'jmp':
            operation_list[index][0] = 'nop'
        elif operation_list[index][0] == 'nop':
            operation_list[index][0] = 'jmp'
        while pos < len(operation_list):
            if operation_list[pos][2]:
                break
            if operation_list[pos][0] == 'acc':
                operation_list[pos][2] = True
                accumulator += operation_list[pos][1]
            elif operation_list[pos][0] == 'jmp':
                operation_list[pos][2] = True
                pos += operation_list[pos][1] - 1
            elif operation_list[pos][0] == 'nop':
                operation_list[pos][2] = True
            pos += 1
        if pos >= len(operation_list):
            return accumulator


def main():
    count = 0
    commands = []
    aug_commands_count = []
    with open(file, "r") as f:
        for item in f:
            item = item.rstrip()
            operation, number = item.split(" ")
            commands.append([operation, int(number), False])
            if not operation == 'acc':
                aug_commands_count.append(count)
            count += 1
    f.close()
    print(acc_count(aug_commands_count, commands))


if __name__ == "__main__":
    main()
