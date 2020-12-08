file = "input.txt"


def acc_count(operations):
    pos, accumulator = 0, 0
    while True:
        if len(operations[pos]) == 3:
            return accumulator
        if operations[pos][0] == "nop":
            operations[pos].append(1)
            pos += 1
        elif operations[pos][0] == "jmp":
            operations[pos].append(1)
            pos += int(operations[pos][1])
        elif operations[pos][0] == "acc":
            operations[pos].append(1)
            accumulator += int(operations[pos][1])
            pos += 1


def main():
    commands = []
    with open(file, "r") as f:
        for item in f:
            item = item.rstrip()
            items = item.split(" ")
            commands.append(items)
    f.close()
    print(acc_count(commands))


if __name__ == "__main__":
    main()
