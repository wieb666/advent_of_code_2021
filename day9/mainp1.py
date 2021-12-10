import sys

def main(fname):
    x = []
    with open(fname) as f:
        for line in f: 
            x.append(line.strip())
    
    x = [list(i) for i in x]
    x = [[int(num) for num in l[:]] for l in x]
    
    risk = 0
    for i in range(len(x)):
        for  j in range(len(x[0])):
            center = x[i][j]
            try:
                if i-1 < 0:
                    above = 1e100
                else:
                    above = x[i-1][j]
            except IndexError:
                above = center + 1
            try:
                below = x[i+1][j]
            except IndexError:
                below = center + 1
            try:
                if j-1 < 0:
                    left = 1e100
                else:
                    left = x[i][j-1]
            except IndexError:
                left = center + 1
            try:
                right = x[i][j+1]
            except IndexError:
                right = center + 1
            
            if center < above and center < below and center < left and center < right:
                risk += center + 1

    print(risk)

if __name__ == "__main__":
    main(sys.argv[1])
