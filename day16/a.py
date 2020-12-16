file = "input.txt"
# file = "small.txt"


def main():
    nearby = []
    yourtickets = []
    rules = []
    numrange = []
    with open(file, "r") as f:
        starting = [x.rstrip() for x in f.readlines()]

    for index, string in enumerate(starting):
        if string == 'nearby tickets:' or index > 24:
            nearby.append(string)
        if string == 'your ticket:' or 20 < index < 23:
            yourtickets.append(string)
        if index < 20:
            rules.append(string)
    for item in rules:
        items = item.split(':')
        items = items[1].split(' or ')
        for num in items:
            nums = num.split('-')
            for x in range(int(nums[0]), int(nums[1])):
                if x not in numrange:
                    numrange.append(x)
    print(numrange)
    sum = 0
    for ticket in nearby:
        if ticket == 'nearby tickets:':
            continue
        else:
            val = ticket.split(',')
            for x in val:
                x = int(x)
                if x not in numrange:
                    print(x)
                    sum += x
    print(sum)

if __name__ == "__main__":
    main()
