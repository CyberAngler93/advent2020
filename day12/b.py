file = "input.txt"
# file = "sample.txt"
# file = "small_sample.txt"
import copy

def main():
    commands = []
    with open(file, "r") as f:
        for item in f:
            item = item.rstrip()
            commands.append(item)
    f.close()
    current_x, current_y = 0, 0
    way_x, way_y = 10, 1
    for item in commands:
        val = int(item[1:])
        if item[0] == 'N':
            way_y += val
        if item[0] == 'S':
            way_y -= val
        if item[0] == 'E':
            way_x += val
        if item[0] == 'W':
            way_x -= val
        if item[0] == 'L':
            temp = copy.deepcopy(way_x)
            if val == 90:
                way_x = way_y * -1
                way_y = temp
            elif val == 180:
                way_x = way_x * -1
                way_y = way_y * -1
            elif val == 270:
                way_x = way_y
                way_y = temp * -1
        if item[0] == 'R':
            temp = copy.deepcopy(way_x)
            if val == 90:
                way_x = way_y
                way_y = temp * -1
            elif val == 180:
                way_x = way_x * -1
                way_y = way_y * -1
            elif val == 270:
                way_x = way_y * -1
                way_y = temp
        if item[0] == 'F':
            current_y += val * way_y
            current_x += val * way_x

    print(abs(current_y) + abs(current_x))


if __name__ == "__main__":
    main()