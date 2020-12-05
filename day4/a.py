file = 'input.txt'


def main():
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
        answer = 0
        for item in data:
            if 'byr' in item and 'iyr' in item and 'eyr' in item and 'hgt' in item and 'hcl' in item and 'ecl' in item and 'pid' in item:
                answer += 1

        print(answer)
    f.close()


if __name__ == "__main__":
    main()