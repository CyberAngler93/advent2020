file = "input.txt"
# file = "small.txt"


def main():
    with open(file, "r") as f:
        starting = [int(x) for x in f.readline().split(',')]
    starting.reverse()
    numbers, last = {}, None
    for index in range(30000000):
        if starting:
            last = starting.pop()
            if last not in numbers:
                numbers[last] = [index]
            else:
                numbers[last].append(index)
        else:
            if len(numbers[last]) == 1:
                last = 0
            else:
                last = numbers[last][-1] - numbers[last][-2]
            if last in numbers:
                numbers[last].append(index)
            else:
                numbers[last] = [index]
    print(last)


if __name__ == "__main__":
    main()
