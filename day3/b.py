file = 'input.txt'


def tree_check(x, y, lines):
    tree = 0
    pos = 0
    for line in lines[::y]:
        if line[pos] == '#':
            tree += 1
        pos += x
        if pos >= len(line):
            pos = pos - len(line)
    return tree


def main():
    lines = []
    result = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    with open(file, "r") as f:
        for line in f:
            lines.append(str(line).rstrip())
        f.close()
    for run, rise in slopes:
        result.append(tree_check(run, rise, lines))
    tree_total = 1
    for val in result:
        tree_total = val * tree_total
    print(tree_total)


if __name__ == "__main__":
    main()