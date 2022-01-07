from collections import Counter, defaultdict
import sys

def read_file(fname: str):
    template = None
    poly_d = defaultdict()
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if "->" in line:
                x, y = line.split('->')
                poly_d[x.strip()] = y.strip()
            elif line:
                template = line.strip()
    return template, poly_d

def main(fname: str):
    
    template, poly_d = read_file(fname)
    print(template)
    n = 2
    
    for i in range(10):
        chunks = [template[i:i+n] for i in range(0, len(template), 1) if len(template[i:i+n]) == 2]
        
        new_template = ""
        for chunk in chunks:
            new = chunk[0] + poly_d[chunk]
            new_template += new
        new_template += chunk[1]
        template = new_template

    a = Counter(template)
    most = a.most_common()[0][1]
    least = a.most_common()[-1][1]
    
    print(most - least)

if __name__ == "__main__":
    main(sys.argv[1])

#TODO The for loop is killing it.. stops after 18 loops

