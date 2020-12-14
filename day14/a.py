file = "input.txt"
# file = "small.txt"


def main():
    data = {}
    with open(file, "r") as f:
        lines = [line.rstrip() for line in f.readlines()]
    curr_mask = ''
    for line in lines:
        res = line.split(' = ')
        if res[0] == 'mask':
            curr_mask = res[1]
        else:
            res[1] = f"{int(res[1]):36b}".replace(' ', '0')
            temp = list(res[1])
            for index, char in enumerate(list(curr_mask)):
                if char != 'X':
                    if char != res[1][index]:
                        temp[index] = char
            result = "".join(temp)
            result = int(result, 2)
            data[res[0]] = result
    sum = 0
    for key in data:
        sum += data[key]
    print(sum)


if __name__ == "__main__":
 main()