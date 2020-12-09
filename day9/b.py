file = "input.txt"
# file = "sample.txt"


def counter(nums):
    target = 507622668
    for x in range(0, len(nums)):
        for y in range(0, len(nums)):
            val = sum(nums[x:y])
            if val == target:
                temp = sorted(nums[x:y])
                return temp[0] + temp[len(temp) - 1]
            elif val > target:
                break


def main():
    commands = []

    with open(file, "r") as f:
        for item in f:
            item = item.rstrip()
            commands.append(int(item))
    f.close()
    print(counter(commands[:633]))

if __name__ == "__main__":
    main()