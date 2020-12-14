file = "input.txt"
# file = "small.txt"


def address_gen(mask, value):
    val_bin = f"{value:36b}".replace(' ', '0')
    new_val = []
    for i in range(len(mask)):
        if mask[i] == '0':
            new_val += val_bin[i]
        else:
            new_val += mask[i]
    index_of_x = [index for index, val in enumerate(new_val) if val == 'X']
    count_of_x = new_val.count('X')
    for new in range(pow(2, count_of_x)):
        new_binary = list(f"{new:b}")
        zeroes_2_add = ['0'] * (count_of_x - len(new_binary))
        new_binary = zeroes_2_add + new_binary
        for itter, val in enumerate(new_binary):
            target_idx = index_of_x[itter]
            new_val[target_idx] = val
        yield int(''.join(new_val), 2)


def parse(program):
    mem = {}
    current_mask = ''
    for line in program:
        key, para = line.split(' = ')
        if key == 'mask':
            current_mask = para
        else:
            para = int(para)
            write_to = int(key.strip('mem[]'))
            for address in address_gen(current_mask, write_to):
                mem[address] = para
    return sum(mem.values())


def main():
    with open(file, "r") as f:
        lines = f.read().splitlines()
    print(parse(lines))


if __name__ == "__main__":
    main()
