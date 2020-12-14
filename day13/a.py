import math
file = "input.txt"
# file = "sample.txt"



def main():
    with open(file, "r") as f:
        lines = f.readlines()
    time = int(lines[0].rstrip())
    buses = lines[1].replace('x', '')
    buses = buses.split(',')
    print(buses)
    print(time)
    max = 0
    final = 0
    for bus in buses:
        if bus:
            val = time / int(bus)
            lower = math.floor(val)
            dif = val - lower
            if dif > max:
                max = dif
                final = int(bus)
                print((math.ceil(val) * int(bus) - time) * int(bus))


if __name__ == "__main__":
    main()