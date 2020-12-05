nums = []
with open("input_a.txt", "r") as f:
    for one in f:
        nums.append(int(one))
    f.close()
result = ((x, y) for x in nums for y in nums if x+y == 2020)
for x, y in result:
    print(x * y)

