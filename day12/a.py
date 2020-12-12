file = "input.txt"
# file = "sample.txt"
# file = "small_sample.txt"


def main():
    commands = []
    with open(file, "r") as f:
        for item in f:
            item = item.rstrip()
            commands.append(item)
    f.close()
    current_facing = 'E'
    current_x, current_y = 0, 0
    for item in commands:
        val = int(item[1:])
        print(current_y, current_x, current_facing, val, item[0])
        if item[0] == 'N':
            current_y += val
        if item[0] == 'S':
            current_y -= val
        if item[0] == 'E':
            current_x += val
        if item[0] == 'W':
            current_x -= val
        if item[0] == 'L':
            if val == 90:
                if current_facing == 'N':
                    current_facing = 'W'
                elif current_facing == 'E':
                    current_facing = 'N'
                elif current_facing == 'S':
                    current_facing = 'E'
                elif current_facing == 'W':
                    current_facing = 'S'
            if val == 180:
                if current_facing == 'N':
                    current_facing = 'S'
                elif current_facing == 'E':
                    current_facing = 'W'
                elif current_facing == 'S':
                    current_facing = 'N'
                elif current_facing == 'W':
                    current_facing = 'E'
            if val == 270:
                if current_facing == 'N':
                    current_facing = 'E'
                elif current_facing == 'E':
                    current_facing = 'S'
                elif current_facing == 'S':
                    current_facing = 'W'
                elif current_facing == 'W':
                    current_facing = 'N'
        if item[0] == 'R':
            if val == 90:
                if current_facing == 'N':
                    current_facing = 'E'
                elif current_facing == 'E':
                    current_facing = 'S'
                elif current_facing == 'S':
                    current_facing = 'W'
                elif current_facing == 'W':
                    current_facing = 'N'
            if val == 180:
                if current_facing == 'N':
                    current_facing = 'S'
                elif current_facing == 'E':
                    current_facing = 'W'
                elif current_facing == 'S':
                    current_facing = 'N'
                elif current_facing == 'W':
                    current_facing = 'E'
            if val == 270:
                if current_facing == 'N':
                    current_facing = 'W'
                elif current_facing == 'E':
                    current_facing = 'N'
                elif current_facing == 'S':
                    current_facing = 'E'
                elif current_facing == 'W':
                    current_facing = 'S'
        if item[0] == 'F':
            if current_facing == 'N':
                current_y += int(item[1:])
            if current_facing == 'S':
                current_y -= int(item[1:])
            if current_facing == 'E':
                current_x += int(item[1:])
            if current_facing == 'W':
                current_x -= int(item[1:])
    print(abs(current_y) + abs(current_x))


if __name__ == "__main__":
    main()