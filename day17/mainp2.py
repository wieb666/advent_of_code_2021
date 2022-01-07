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
    x1 = area[0]
    x2 = area[1]
    y1 = area[2]
    y2 = area[3]
    
    total = 0
    for x in range(1, x2 + 1):
        for y in range(y1, abs(y1)):
            vx, vy = x, y
            x_p = y_p = 0
            for _ in range(2 * abs(y1) + 1):
                x_p += vx
                y_p += vy
                vx = max(vx - 1, 0)
                vy -= 1

                if y1 <= y_p <= y2 and x1 <= x_p <= x2:
                    total += 1
                    break
                elif y_p < y1 or x_p > x2:
                    break
    print(total)

if __name__ == "__main__":
    main(read_file(sys.argv[1]))
