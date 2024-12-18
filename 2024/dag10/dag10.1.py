import numpy as np

ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def npath(a, i, j, di, dj, m):
    nn = 0
    if a[i + di, j + dj] == a[i, j] + 1:
        if a[i, j] == 8:
            if (i + di, j + dj) in m:
                return 0
            m.add((i + di, j + dj))    
            return 1
        s = sum([npath(a, i + di, j + dj, dx, dy, m) for (dx, dy) in ds])
        return s
    return 0
        
total = 0
with open('dag10input.txt', encoding='ascii' ) as fp:
    data = fp.readlines()
    dd = []
    dd.append([-1] * (1 + len(data[0])))
    for line in data:
        dd.append([-1,] + [int(c) for c in line.strip()] + [-1,])
    dd.append([-1] * (1 + len(data[0])))
    a = np.array(dd)
    nx, ny = a.shape
    
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            if a[i, j] == 0:
                m = set()
                s = sum([npath(a, i, j, dx, dy, m) for (dx, dy) in ds])
                total += s
                
    print(total)
                