import re
file = 'input.txt'


def filer(data_set):
    count = 0
    eye = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for passport in data_set:
        if passport:
            if 1920 <= int(passport['byr']) <= 2002:
                if 2010 <= int(passport['iyr']) <= 2020:
                    if 2020 <= int(passport['eyr']) <= 2030:
                        hgt, unit = passport['hgt'][:-2], passport['hgt'][-2:]
                        if (unit == 'cm' and 150 <= int(hgt) <= 193) or (
                                unit == 'in' and 59 <= int(hgt) <= 76):
                            if re.match('^#[0-9a-f]{6}$', passport['hcl']):
                                if passport['ecl'] in eye:
                                    if len(passport['pid']) == 9:
                                        count += 1
    print(count)


def main():
    valid_pp = []
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
            temp_dict = {}
            if 'byr' in item and 'iyr' in item and 'eyr' in item and 'hgt' in item and 'hcl' in item and 'ecl' in item and 'pid' in item:
                splits = item.split(" ")
                for pairs in splits:
                    temp = pairs.split(":")
                    temp_dict[temp[0]] = temp[1]
                answer += 1
            valid_pp.append(temp_dict)
        filer(valid_pp)
    f.close()



if __name__ == "__main__":
    main()