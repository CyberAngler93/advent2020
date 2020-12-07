import time
file = "input.txt"


def count_bags(bag_name, all_bags):
    total = 1
    for bags in all_bags:
        if bags[0] == bag_name:
            for bags_inside in bags[1:]:
                if bags_inside == 'no other':
                    return 1
                else:
                    total += int(bags_inside[0]) * count_bags(bags_inside[2:], all_bags)
    return total


def main():
    start = time.time()
    cleaned_bags = []
    with open(file, "r") as f:
        for item in f:
            item = item.replace(" contain ", ",")
            item = item.replace(".", "")
            item = item.replace(" bags", "")
            item = item.replace(" bag", "")
            item = item.replace(", ", ",")
            item = item.rstrip()
            item = item.split(",")
            cleaned_bags.append(item)
        f.close()
    print(count_bags('shiny gold', cleaned_bags) - 1)
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()