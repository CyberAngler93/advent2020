import collections
file = "input.txt"


def main():
    count = 0
    with open(file, 'r') as f:
        lines = f.readlines()
        lines.append('\n')
        data, temp = [], ''
        for line in lines:
            if not line.strip() == '':
                temp += '{} '.format(line.strip())
            else:
                data.append(temp[:-1])
                temp = ''
        for group in data:
            string = ""
            join = group.split(" ")
            people = len(join)
            for temp in join:
                string += temp
            str_count = collections.defaultdict(int)
            for char in string:
                str_count[char] += 1
            for key in str_count:
                if str_count[key] == people:
                    count += 1
    print(count)


if __name__ == "__main__":
    main()