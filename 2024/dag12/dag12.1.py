import numpy as np

ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def reg(c, a, i, j, m):
    if (i, j) not in m and a[i, j] == c:
        m.add((i, j))
        for d in ds:
            reg(c, a, i + d[0], j + d[1], m)
        
def perim(c, a, s):
    n = 0
    for i, j in s:
        n += len([d for d in ds if a[i+d[0], j+d[1]] != c])
    return n
    
total = 0
with open('dag12input.txt', encoding='ascii' ) as fp:
    data = fp.read().rstrip().split()
    dd = []
    dd.append([0] * (2 + len(data[0])))
    for line in data:
        dd.append([0,] + [ord(c) for c in line.strip()] + [0,])
    dd.append([0] * (2 + len(data[0])))
    a = np.array(dd)
    nx, ny = a.shape
    
    for cc in range(ord('A'), ord('Z') + 1):
        c = np.str_(cc)
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                if a[i, j] == c:
                    s = set()
                    reg(c, a, i, j, s)
                    area = len(s)
                    p = perim(c, a, s)
                    total += area * p
                    for p in s:
                        a[p] = 0
                        
    print(total)
                