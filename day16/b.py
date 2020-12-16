import re
import math
file = "input.txt"
# file = "small.txt"


def main():
    with open(file, "r") as f:
        puzzle_input = [x.rstrip() for x in f.readlines()]
    rules, names, valid_val, poss, fin, ticket, depart = [], [], [], {}, {}, [], []
    for cur in puzzle_input:
        nearby = re.search(r"^([a-z ]+): ([\d]+)-([\d]+) or ([\d]+)-([\d]+)", cur)
        if nearby is not None:
            rules.append([int(x) for x in nearby.groups()[1:]])
            names.append(nearby.groups()[0])
        nearby = re.search(r"^[\d,]+$", cur)
        if nearby is not None:
            cur = [int(x) for x in cur.split(",")]
            all_valid = True
            for x in cur:
                valid = False
                for rule in rules:
                    if rule[0] <= x <= rule[1]:
                        valid = True
                    if rule[2] <= x <= rule[3]:
                        valid = True
                if not valid:
                    all_valid = False
            if all_valid:
                valid_val.append(cur)
    for valid_pos in range(len(valid_val[0])):
        for rule_pos in range(len(rules)):
            all_valid = True
            for x in [z[valid_pos] for z in valid_val]:
                valid = False
                if rules[rule_pos][0] <= x <= rules[rule_pos][1]:
                    valid = True
                if rules[rule_pos][2] <= x <= rules[rule_pos][3]:
                    valid = True
                if not valid:
                    all_valid = False
                    break
            if all_valid:
                if names[rule_pos] not in poss:
                    poss[names[rule_pos]] = set()
                poss[names[rule_pos]].add(valid_pos)
    ticket = valid_val[0]
    while True:
        temp = {}
        for poss_key, pos_val in poss.items():
            for x in pos_val:
                temp[x] = temp.get(x, []) + [poss_key]
        if sum([len(x) for x in temp.values()]) == 0:
            break
        for temp_key, temp_val in temp.items():
            if len(temp_val) == 1:
                fin[temp_key] = temp_val[0]
                poss[temp_val[0]] = set()
    for valid_pos in range(len(ticket)):
        if fin[valid_pos].startswith("departure"):
            depart.append(ticket[valid_pos])
    print(math.prod(depart))


if __name__ == "__main__":
    main()
