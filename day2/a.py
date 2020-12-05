import collections
total = 0
words = []
with open("input_a.txt", "r") as f:
    for word in f:
        words.append(str(word).rstrip())
    f.close()
for word in words:
    counter = collections.defaultdict(int)
    res = word.split(":")
    top = res[0].split(" ")
    string = res[1].lstrip()
    count = top[0].split("-")
    letter = top[1]
    minimum = count[0]
    maximum = count[1]
    for char in string:
        counter[char] += 1
    if int(minimum) <= counter[letter] <= int(maximum):
        total += 1
print(total)

