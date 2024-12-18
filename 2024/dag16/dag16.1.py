import numpy as np
    
total = 0
ok = True
with open('dag16input.txt', encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    dd = []
    for line in data:
        dd.append([c for c in line])
    a = np.array(dd)
    nx = a.shape[0]
    ny = a.shape[1]
    for i in range(nx):
        for j in range(ny):
            if a[i,j] == 'S':
                p0 = (i, j)
            if a[i,j] == 'E':
                pE = (i, j)
                
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cost = np.zeros((nx, ny), dtype=int)
    p = p0
    d = (0, 1)
    front = [(0, p0, d)]
    found = False
    while front:
        nf = []
        for c0, p, d0 in front:
            for d in dirs:
                pn = (p[0] + d[0], p[1] + d[1])
                if a[pn] == '#':
                    continue
                c = c0 + 1
                if d != d0:
                    c += 1000
                if cost[pn] == 0 or c < cost[pn]:
                    cost[pn] = c
                    if pn != pE:
                        nf.append((c, pn, d))
                    if pn == pE:
                        found = True
        nf.sort()
        front = nf
        if not front:
            break

    total = cost[pE]
    print(total)