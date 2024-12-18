import numpy as np

ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def reg(c, a, i, j, m):
    if (i, j) not in m and a[i, j] == c:
        m.add((i, j))
        for d in ds:
            reg(c, a, i + d[0], j + d[1], m)
        
def sides(c, a, s):
    f = []

    for i, j in s:
        for d in ds:
            if a[i+d[0], j+d[1]] != c:
                if d[0] != 0:
                    f.append((d, i+d[0], j+d[1]))
                else:
                    f.append((d, j+d[1], i+d[0]))
    f.sort()

    n = 0
    for d in ds:
        g = []
        for dd, i, j in f:
            if dd == d:
                if dd[0] != 0:
                    g.append((i, j))
                else:
                    g.append((j, i))
        n += 1
        p0, p1 = g[0]
        d1, d2 = abs(d[0]), abs(d[1])
        for pp in g[1:]:
            if pp[1] == p1 + d1:
                if pp[0] != p0 + d2:
                    n += 1
            else:
                n += 1
            p0, p1 = pp
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
    
    for c in range(ord('A'), ord('Z') + 1):
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                if a[i, j] == c:
                    s = set()
                    reg(c, a, i, j, s)
                    area = len(s)
                    p = sides(c, a, s)
                    total += area * p
                    for p in s:
                        a[p] = 0
                        
    print(total)
                