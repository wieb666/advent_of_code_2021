import sys
from statistics import median


def main(fname):
    x = []
    with open(fname) as f:
        for line in f:
            x.append(line.strip())

    d = {"{": 3, "(": 1, "[": 2, "<": 4}
    scores = []
    for subsystem in x:
        forward = []
        subsystem = [i for i in subsystem]
        score = 0
        for i in subsystem:
            if i == ")":
                if forward.pop() != "(":
                    score += 1
            elif i == "]":
                if forward.pop() != "[":
                    score += 1
            elif i == "}":
                if forward.pop() != "{":
                    score += 1
            elif i == ">":
                if forward.pop() != "<":
                    score += 1
            else:
                forward.append(i)

        if score == 0:
            new_score = 0
            for i in forward[::-1]:
                new_score *= 5
                new_score += d[i]
            scores.append(new_score)

    sorted(scores)
    print(median(scores))

if __name__ == "__main__":
    main(sys.argv[1])
