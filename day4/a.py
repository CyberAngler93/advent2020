
import copy
file = 'input.txt'


def main():
    key = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    key = sorted(key)
    valid = 0
    with open(file, "r") as f:
        content = f.read()
        lines = content.splitlines()
        data = []
        for line in lines:
            stuff = line.split(" ")
            data.append(stuff)
            print(data)
        raw_data = []
        for lists in data:
            if lists == ['']:
                check_format = []
                for stuff in raw_data:
                    current = stuff.split(":")[0]
                    if current != 'cid':
                        check_format.append(current)
                check_format = sorted(check_format)
                if check_format == key:
                    print(check_format)
                    valid += 1
                raw_data.clear()
            else:
                raw_data = raw_data + lists
        print(valid)


if __name__ == "__main__":
    main()