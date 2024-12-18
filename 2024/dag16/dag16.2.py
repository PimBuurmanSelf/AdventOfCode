import numpy as np
from collections import defaultdict
import sys
    
total = 0
ok = True
maxC = 7036
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
    backw = defaultdict(list)
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
                    if c + 1000 < cost[pn]:
                        backw[pn].clear()
                    backw[pn].append(p)
                    cost[pn] = c
                    if pn != pE:
                        nf.append((c, pn, d))
                elif c == cost[pn]:
                    backw[pn].append(p)
                elif c == cost[pn] + 1000 and pn != pE:
                    if (a[pn[0] + d[1], pn[1] + d[0]] == '#' or a[pn[0] - d[1], pn[1] - d[0]] == '#'):
                        backw[pn].append(p)
                
        if cost[p0] > 1000:
            cost[p0] = 1000
        nf.sort()
        front = nf
        if not front:
            break

    p = pE
    prev = pE
    total = 1
    b = [(pE, prev),]
    found = set()
    while b:
        nb = set()
        if p == p0:
            continue
        for p, prev in b:
            vp = cost[p]
            bp = max([cost[q] for q in backw[p]])
            if bp > vp:
                if bp == cost[prev] - 2:
                    newbp = []
                    for q in backw[p]:
                        if cost[q] == bp:
                            newbp.append(q)
                        elif cost[q] == cost[prev] - 2 or cost[q] == cost[prev] - 1002:
                            newbp.append(q)
                    backw[p] = newbp
                    
            for q in backw[p]:
                if q != p0:
                    found.add(q)
                    nb.add((q, p))
        b = nb

    total = len(found) + 2
    print(total)