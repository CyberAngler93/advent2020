total = 0
nums = []
with open("input_a.txt", "r") as f:
    for line in f:
        nums.append(str(line).rstrip())
    f.close()
for line in nums:
    res = line.split(":")
    top = res[0].split(" ")
    string = res[1].lstrip()
    count = top[0].split("-")
    letter = top[1]
    pos1 = int(count[0])
    pos2 = int(count[1])
    if string[pos1 - 1] == letter and string[pos2 - 1] != letter:
        print(f"{string}, {letter}, {pos1}, {pos2}")
        total += 1
        print(total)
    elif string[pos1 - 1] != letter and string[pos2 - 1] == letter:
        print(f"{string}, {letter}, {pos1}, {pos2}")
        total += 1
        print(total)

print(total)

