file = "input.txt"
# file = "sample.txt"
# file = "small_sample.txt"


def recursive_counter(data, val, table):
    res = 0
    if data[len(data) - 1] == val:
        return 1
    for x in range(val + 1, val + 4):
        if x in data:
            if x not in table:
                table[x] = recursive_counter(data, x, table)
            res += table[x]
    return res


def main():
    commands = []
    lookup = {}
    with open(file, "r") as f:
        for item in f:
            item = item.rstrip()
            commands.append(int(item))
    f.close()
    data = sorted(commands)
    print(recursive_counter(data, 0, lookup))


if __name__ == "__main__":
    main()

