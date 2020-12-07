file = "input.txt"


def count_bags(bag_name, list_bags):
    total = 1
    for bags in list_bags:
        if bags[0] == bag_name:
            for bags_inside in bags[1:]:
                if bags_inside == 'no other':
                    return 1
                else:
                    total += int(bags_inside[0]) * count_bags(bags_inside[2:], list_bags)
    return total


def main():
    cleaned_bags = []
    lines = []
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
        item = item.rstrip()
        item = item.split(",")
        cleaned_bags.append(item)
    print(count_bags('shiny gold', cleaned_bags) - 1)


if __name__ == "__main__":
    main()