from sympy.ntheory.modular import crt
file = "input.txt"
# file = "sample.txt"
# file = "small_sample.txt"

def main():
    t, *busses = [int(x) for x in open(file).read().replace('x', '1').replace('\n', ',').split(',')]
    m, r = zip(*((b, b - i) for i, b in enumerate(busses) if b > 1))
    print(crt(m, r)[0])


if __name__ == "__main__":
    main()