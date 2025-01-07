import numpy as np
from heapq import heappush, heappop
from collections import defaultdict
    
total = 0
ok = True
#problem = ('dag20ainput.txt', 10)
problem = ('dag20input.txt', 100)
offset = problem[1]
with open(problem[0], encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    dd = []
    for line in data:
        dd.append([c for c in line])
    a = np.array(dd)
    nx, ny = a.shape
    for x in range(nx):
        for y in range(ny):
            if a[x,y] == 'S':
                p0 = (x, y)
            if a[x, y] == 'E':
                pE = (x, y)
                
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cost = np.ones((nx, ny), dtype=int)
    cost *= -1
    p = p0
    cost[p0] = 0
    front = []
    heappush(front, (0, p0))
    path = [p0]
    found = False
    while front and not found:
        c0, p = heappop(front)
        for d in dirs:
            pn = (p[0] + d[0], p[1] + d[1])
            if a[pn] == '#':
                continue
            c = c0 + 1
            if cost[pn] == -1:
                cost[pn] = c
                path.append(pn)
                heappush(front, (c, pn))
                if pn == pE:
                    found = True

    cheats = defaultdict(list)
    for p in path:
        c = cost[p] + offset + 2
        for d in dirs:
            pn = (p[0] + d[0], p[1] + d[1])
            if a[pn] == '#':
                qx, qy = (p[0] + 2 * d[0], p[1] + 2 * d[1])
                if qx >= 0 and qx < nx and qy >= 0 and qy < ny and cost[qx, qy] >= c:
                    cheats[int(cost[qx, qy] + offset) - c].append((p, (qx, qy)))
                
    total = sum([len(cheats[k]) for k in cheats])
    print(total)