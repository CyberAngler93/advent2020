nums = []
with open("input_a.txt", "r") as f:
    for one in f:
        nums.append(int(one))
    f.close()
result = ((x, y, z) for x in nums for y in nums for z in nums if x+y+z == 2020)
for x, y, z in result:
    print(x * y * z)
