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
            for temp in join:
                string += temp
            newstr = "".join(collections.OrderedDict.fromkeys(string))
            count += len(newstr)
    print(count)

if __name__ == "__main__":
    main()