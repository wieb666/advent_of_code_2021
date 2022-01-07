import sys


def main(fname):
    x = []
    with open(fname) as f:
        for line in f:
            x.append(line.strip())
    
    score = 0
    for subsystem in x:
        forward = []
        subsystem = [i for i in subsystem]
        for i in subsystem:
            if i == ")":
                if forward.pop() != "(":
                    score += 3
            elif i == "]":
                if forward.pop() != "[":
                    score += 57
            elif i == "}":
                if forward.pop() != "{":
                    score += 1197
            elif i == ">":
                if forward.pop() != "<":
                    score += 25137
            else:
                forward.append(i)
    print(score)

if __name__ == "__main__":
    main(sys.argv[1])
