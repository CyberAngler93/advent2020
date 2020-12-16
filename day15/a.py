file = "input.txt"
# file = "small.txt"


def main():
    with open(file, "r") as f:
        starting = [int(x) for x in f.readline().split(',')]
    size = len(starting)
    count = 0
    while count < 2020:
        if count >= size:
            last = starting[count - 1]
            last_count = starting.count(last)
            if last_count == 1:
                starting.append(0)
                count += 1
            elif last_count > 1:
                age = []
                for index, num in enumerate(starting):
                    if num == last:
                        age.append(index)
                age = sorted(age)
                new = age[-1] - age[-2]
                starting.append(new)
                count += 1
        else:
            count += 1
    print(starting[-1])

if __name__ == "__main__":
    main()