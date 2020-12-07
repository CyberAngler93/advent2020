import collections
from string import digits
file = "input.txt"


def main():
    cleaned_bags = []
    gold_count = []
    data, temp, lines = [], '', []
    with open(file, "r") as f:
        for line in f:
            lines.append(str(line).rstrip())
        f.close()
    for item in lines:
        item = item.replace(" contain ", ",")
        item = item.replace(".", "")
        item = item.replace(" bags", "")
        item = item.replace(" bag", "")
        item = item.replace(", ", ",")
        remove_digits = str.maketrans('', '', digits)
        item = item.translate(remove_digits)
        item = item.rstrip()
        item = item.split(",")
        cleaned_bags.append(item)

    for listy in cleaned_bags:
        for bags in listy:
            if bags.lstrip() == 'shiny gold':
                gold_count.append(listy[0])
    res = []
    while True:
        res_len = len(res) - 1
        for listy in cleaned_bags:
            for items in listy[1:]:
                if items.lstrip() in gold_count:
                    gold_count.append(listy[0])
        [res.append(x) for x in gold_count if x not in res]
        if res_len == len(res) - 1:
            print(res_len)
            break


if __name__ == "__main__":
    main()