import sys

def read_file(fname: str) -> list:
    lines = []
    with open(fname) as f:
        for line in f:
            x, y = line.split(": ")[1].split(", ")
    # x
    x_start, x_end = x.split("=")[1].split("..")
    x_start = int(x_start)
    x_end = int(x_end)

    # y
    y_start, y_end = y.split("=")[1].split("..")
    y_start = int(y_start)
    y_end = int(y_end)

    return [x_start, x_end, y_start, y_end]

def main(area: list):
    y0 = abs(area[2]) - 1
    print(y0 * y0 - (y0 - 1) * y0 // 2)

if __name__ == "__main__":
    main(read_file(sys.argv[1]))
