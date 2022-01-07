import sys
import collections

def main(fname: str):
    edges = collections.defaultdict(set)
    with open(fname) as f:
        for line in f:
            src, dst = line.strip().split("-")
            edges[src].add(dst)
            edges[dst].add(src)
    
    all_paths = set()
    todo = [(('start',), False)]
    while todo:
        path, double_cave = todo.pop()
        
        if path[-1] == 'end':
            all_paths.add(path)
            continue
        
        for cand in edges[path[-1]]:
            if cand == 'start':
                continue
            elif cand.isupper() or cand not in path:
                todo.append(((*path, cand), double_cave))
            elif not double_cave and path.count(cand) == 1:
                todo.append(((*path, cand), True))
            
    print(len(all_paths))
    
if __name__ == "__main__":
    main(sys.argv[1])
