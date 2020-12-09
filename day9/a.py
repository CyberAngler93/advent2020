import itertools
file = "input.txt"
# file = "sample.txt"


def counter(nums):
    pos = 25
    offset = 25
    subset = []
    while True:
        for i in range(pos - offset, pos):
            subset.append(nums[i])
        subset = list(itertools.combinations(subset, 2))
        flag = False
        for x in subset:
            if x[0] + x[1] == nums[pos]:
                flag = True
                break
        if flag:
            pos += 1
            subset.clear()
        elif not flag:
            return nums[pos]


def main():
    commands = []
    with open(file, "r") as f:
        for item in f:
            item = item.rstrip()
            commands.append(int(item))
    f.close()
    print(counter(commands))


if __name__ == "__main__":
    main()
