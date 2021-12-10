import sys
from collections import defaultdict

def main(fname):
    total_score = 0
    with open(fname) as f:
        for line in f:
            line = [x.strip().split() for x in line.strip().split("|")]
            seven_digit_number = [set(),set(),set(),set(),set(),set(),set()]
            d = defaultdict(dict)
            numbers = line[0]
            output = line[1]
            numbers.sort(key=len)

            known = []
            guess = []
            for n in numbers:
                if len(n) in {2, 3, 4, 7}:
                    known.append(n)
                else:
                    guess.append(n)

            for x in known:
                x = set(list(x))
                if len(x) == 2:
                    d[1] = x
                    seven_digit_number[2].update(x)
                    seven_digit_number[5].update(x)
                if len(x) == 3:
                    d[7] = x
                    seven_digit_number[0].update(x.difference(seven_digit_number[2]))
                if len(x) == 4:
                    d[4] = x
                    seven_digit_number[1].update(x.difference(seven_digit_number[2]))
                    seven_digit_number[3].update(x.difference(seven_digit_number[2]))
                if len(x) == 7:
                    d[8] = x
                    for i in seven_digit_number:
                        x = x - i
                    seven_digit_number[4] = x
                    seven_digit_number[6] = x

            for g in guess:
                g = set(list(g))
                if len(g) == 5:
                    if len(seven_digit_number[2]) != 1 and len(seven_digit_number[2] - g) == 0 and len(seven_digit_number[5]) != 1 and len(seven_digit_number[5] - g) == 0:
                        d[3] = g
                    if len(seven_digit_number[1]) != 1 and len(seven_digit_number[1] - g) == 0:
                        d[5] = g
                    if len(seven_digit_number[4]) != 1 and len(seven_digit_number[4] - g) == 0:
                        d[2] = g
                if len(g) == 6:
                    if len(seven_digit_number[3]) != 1 and len(seven_digit_number[3] - g) != 0:
                        d[0] = g
                    if len(seven_digit_number[2]) != 1 and len(seven_digit_number[2] - g) != 0:
                        d[6] = g
                    if len(seven_digit_number[4]) != 1 and len(seven_digit_number[4] - g) != 0:
                        d[9] = g

            score = ''
            for x in output:
                x = list(x)
                x.sort()
                for k,v in d.items():
                    v = list(v)
                    v.sort()
                    if x == v:
                        score += str(k)
            total_score += int(score)

    print(total_score)

if __name__ == "__main__":
    main(sys.argv[1])
