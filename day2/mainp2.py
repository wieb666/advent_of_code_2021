import sys

def main(fname):
    horizontal, depth, aim = 0, 0, 0
    with open(fname) as f:
        for line in f:
            line = line.strip().split()
            value =int(line[1])
            if line[0] == "forward":
                horizontal += value
                depth += value * aim
            elif line[0] == "up":
                aim -= value
            elif line[0] == "down":
                aim += value
    print(horizontal * depth)

if __name__ == "__main__":
    main(sys.argv[1])
