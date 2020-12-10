file = "input.txt"
# file = "sample.txt"
# file = "small_sample.txt"


def main():
    one, three = 0, 1
    commands = []
    with open(file, "r") as f:
        for item in f:
            item = item.rstrip()
            commands.append(int(item))
    f.close()
    data = sorted(commands)
    last = 0
    for item in data:
        val = item - last
        last = item
        if val == 1:
            one += 1
        elif val == 3:
            three += 1
    print(one * three)


if __name__ == "__main__":
    main()
