file = 'input.txt'


def decode(string, upper, lower, upper_char, lower_char):
    res = 0
    for char in string:
        count = upper - lower
        if count == 1:
            if char == lower_char:
                res = lower
            elif char == upper_char:
                res = upper
        elif char == upper_char:
            lower += round(count / 2)
        elif char == lower_char:
            upper -= round(count / 2)
    return res


def main():
    max = 0
    lines = []
    seats = []
    count = 32
    with open(file, "r") as f:
        for line in f:
            lines.append(str(line).rstrip())
        f.close()
    for line in lines:
        row = decode(line[0:7], 127, 0, 'B', 'F')
        col = decode(line[7:len(line)], 7, 0, 'R', 'L')
        seat = row * 8
        seat += col
        seats.append(seat)

    for x in range(0, 900, 1):
        if x not in seats:
            print(x)


if __name__ == "__main__":
    main()