file = "input.txt"
# file = "sample.txt"


def count_occupied(r, c, grid, rows, cols, deltas):
    count = 0
    for i, j in deltas:
        xi, xj = r + i, c + j
        if 0 <= xi < rows and 0 <= xj < cols and grid[xi][xj] == '#':
            count += 1
    return count


def check_occupied(lines, rows, cols, deltas, thresh=4):
    while True:
        valid = True
        temp_grid = [r.copy() for r in lines]
        for i, r in enumerate(temp_grid):
            for j, c in enumerate(r):
                count = count_occupied(i, j, temp_grid, rows, cols, deltas)
                if c == 'L' and count == 0:
                    lines[i][j] = '#'
                elif c == '#' and count >= thresh:
                    lines[i][j] = 'L'
                valid &= (r[j] == lines[i][j])
        if valid:
            break
    count = 0
    for i in range(rows):
        for j in range(cols):
            if lines[i][j] == '#':
                count += 1
    print(count)


def main():
    with open(file, "r") as f:
        lines = [line.rstrip() for line in f.readlines()]
        lines = [list(line) for line in lines]
    rows, cols = len(lines), len(lines[0])
    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    check_occupied(lines, rows, cols, deltas)


if __name__ == "__main__":
    main()
